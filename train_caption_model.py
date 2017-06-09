#!/usr/bin/env python

'''
This file is used for training of LSTM caption generation model.
'''

import chainer 
import argparse
import numpy as np
import chainer.functions as F
from chainer import cuda
from chainer import Function, FunctionSet, Variable, optimizers, serializers
import pickle
import random

#Training using GPU
gpu_id=0

#Path to save the models and optimizers with loss
savedir='../experiment1/'

#Arguments
parser = argparse.ArgumentParser(description=u"caption generation")
parser.add_argument("-g", "--gpu",default=gpu_id, type=int, help=u"GPU ID.CPU is -1")
parser.add_argument("-d", "--savedir",default=savedir, type=str, help=u"The directory to save models and log")
args = parser.parse_args()
gpu_id=args.gpu
savedir=args.savedir

#GPU Setting
if gpu_id >= 0:
	xp = cuda.cupy 
	cuda.get_device(gpu_id).use()
else:
	xp=np

#Prepare Data
print("loading preprocessed data")

with open('../work/index2token.pkl', 'r') as f:
	index_to_token = pickle.load(f)

with open('../work/preprocessed_train_captions.pkl', 'r') as f:
	train_captions,train_caption_id_to_sentence,train_caption_id_to_image_id = pickle.load(f)

with open('../work/img_features/train_image_id2feature.pkl', 'r') as f:
	train_image_id_to_feature = pickle.load(f)

#LSTM Model Preparation
feature_dimension=1024
no_of_units = 512
vocabulary_size=len(index_to_token)

model = chainer.FunctionSet()
model.img_feature2vec=F.Linear(feature_dimension, no_of_units)
model.embed=F.EmbedID(vocabulary_size, no_of_units)
model.l1_x=F.Linear(no_of_units, 4 * no_of_units)
model.l1_h=F.Linear(no_of_units, 4 * no_of_units)
model.out=F.Linear(no_of_units, vocabulary_size)

#Parameter Initialization
for param in model.params():
	data = param.data
	data[:] = np.random.uniform(-0.1, 0.1, data.shape)

#set forget bias 1
model.l1_x.b.data[2*no_of_units:3*no_of_units]=np.ones(model.l1_x.b.data[2*no_of_units:3*no_of_units].shape).astype(xp.float32)
model.l1_h.b.data[2*no_of_units:3*no_of_units]=np.ones(model.l1_h.b.data[2*no_of_units:3*no_of_units].shape).astype(xp.float32)

#To GPU
if gpu_id >= 0:
	model.to_gpu()

def forward_one_step(cur_word, next_word, state, volatile=False):
	x = chainer.Variable(cur_word, volatile)
	t = chainer.Variable(next_word, volatile)
	h0 = model.embed(x)
	h1_in = model.l1_x(F.dropout(h0)) + model.l1_h(state['h1'])
	c1, h1 = F.lstm(state['c1'], h1_in)
	y = model.out(F.dropout(h1)) 
	state = {'c1': c1, 'h1': h1}
	loss = F.softmax_cross_entropy(y, t)
	return state, loss

def forward_one_step_for_image(img_feature, first_word, state, volatile=False):
	x = chainer.Variable(img_feature)
	t = chainer.Variable(first_word, volatile)
	h0 = model.img_feature2vec(x)
	h1_in = model.l1_x(F.dropout(h0)) + model.l1_h(state['h1'])
	c1, h1 = F.lstm(state['c1'], h1_in)
	y = model.out(F.dropout(h1))
	state = {'c1': c1, 'h1': h1}
	loss = F.softmax_cross_entropy(y, t)
	return state, loss

def forward(img_feature,sentences, volatile=False):
	state = {name: chainer.Variable(xp.zeros((batchsize, no_of_units),dtype=xp.float32),volatile) for name in ('c1', 'h1')}
	loss = 0
	first_word=sentences.T[0]
	state, new_loss = forward_one_step_for_image(img_feature, first_word,state, volatile=volatile)
	loss += new_loss
    
	for cur_word, next_word in zip(sentences.T, sentences.T[1:]):
		state, new_loss = forward_one_step(cur_word, next_word,state, volatile=volatile)
		loss += new_loss
	return loss

optimizer = optimizers.Adam()
optimizer.setup(model)

#Trining Setting
normal_batchsize=256
grad_clip = 1.0
num_train_data=len(train_caption_id_to_image_id)

#Begin Training
print 'Training has been started..'

for epoch in xrange(200):

	print 'Epoch %d' %epoch
	batchsize=normal_batchsize
	caption_ids_batches=[]
	for caption_length in train_captions.keys():
		caption_ids_set=train_captions[caption_length]
		caption_ids=list(caption_ids_set)
		random.shuffle(caption_ids)
		caption_ids_batches+=[caption_ids[x:x + batchsize] for x in xrange(0, len(caption_ids), batchsize)]   
	random.shuffle(caption_ids_batches)

	training_bacthes={}
	for i, caption_ids_batch in enumerate(caption_ids_batches):
		images = xp.array([train_image_id_to_feature[train_caption_id_to_image_id[caption_id]] for caption_id in caption_ids_batch],dtype=xp.float32)
		sentences = xp.array([train_caption_id_to_sentence[caption_id] for caption_id in caption_ids_batch],dtype=xp.int32)
		training_bacthes[i]= (images,sentences)

	sum_loss = 0
	for i, batch in training_bacthes.iteritems():
		images=batch[0]
		sentences=batch[1]

        sentence_length=len(sentences[0])
        batchsize=normal_batchsize
        if len(images) != batchsize:
		batchsize=len(images) 

        optimizer.zero_grads()
        loss = forward(images,sentences)
        print loss.data
        with open(savedir+"real_loss.txt", "a") as f:
		f.write(str(loss.data)+'\n') 
        with open(savedir+"real_loss_per_word.txt", "a") as f:
		f.write(str(loss.data/sentence_length)+'\n') 

        loss.backward()
        optimizer.update()        
        sum_loss += loss.data * batchsize
    
	serializers.save_hdf5(savedir+"/caption_model"+str(epoch)+'.chainer', model)
	serializers.save_hdf5(savedir+"/optimizer"+str(epoch)+'.chainer', optimizer)

	mean_loss     = sum_loss / num_train_data
	with open(savedir+"mean_loss.txt", "a") as f:
		f.write(str(loss.data)+'\n')
