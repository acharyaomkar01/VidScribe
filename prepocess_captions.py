#!/usr/bin/env python

'''
This program preprocesses the caption into pickle file.
Main purpose is to tokenize, make lower case, and filter out low frequent vocaburaries.
Note tokenize and  make lower case is done by a function (MSCOCO_json_file_reader) in another file MSCOCO.py.
'''

from MSCOCO_reader import MSCOCO_json_file_reader
from gensim import corpora
import pickle

file_place = '../data/MSCOCO/annotations/captions_train2014.json'
train_captions,train_caption_id2tokens,train_caption_id2image_id = MSCOCO_json_file_reader(file_place)

#Removes words occuring less than 5 times
texts=train_caption_id2tokens.values()
dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=5, no_above=1.0)
dictionary.compactify()
index2token = dict((v, k) for k, v in dictionary.token2id.iteritems())
ukn_id=len(dictionary.token2id)
index2token[ukn_id]='<UKN>'

with open('../work/index2token.pkl', 'w') as f:
	pickle.dump(index2token,f)

train_caption_id2sentence={}
for (caption_id,tokens) in train_caption_id2tokens.iteritems():
	sentence=[]
	for token in tokens:
		if token in dictionary.token2id:
			sentence.append(dictionary.token2id[token])
		else:
			sentence.append(ukn_id)            
	train_caption_id2sentence[caption_id]=sentence

#Save preprocessed captions.
with open('../work/preprocessed_train_captions.pkl', 'w') as f:
	pickle.dump((train_captions,train_caption_id2sentence,train_caption_id2image_id),f)
