#!/usr/bin/env python

'''
This file defines a function which reads the MSCOCO's annotation
from its JSON file format and stores captions separately
in order to use them for the training.
'''

#To read MSCOCO's annotations stored as JSON file
import json

#To tokenize sentences into words
import nltk 

def MSCOCO_json_file_reader(file_place):

	#Open JSON file and read the data
	f = open(file_place, 'r')
	jsonData = json.load(f)
	f.close()

	#Storage for captions and their respective ids
	captions={}
	caption_id_to_words={}
	caption_id_to_image_id={}

	#Iteration over all the ~4.2L captions
	for caption_data in jsonData['annotations']:
		caption_id=caption_data['id']
		image_id=caption_data['image_id']
		caption=caption_data['caption']

		#Delete the period ('.') at the end of sentences.
		caption=caption.replace('\n', '').strip().lower()
		if caption[-1]=='.': 
			caption=caption[0:-1]

		#Addition of Start of Sentence <SOS> tag
		caption_tokens=['<SOS>']

		#Tokenizing sentence into words
		caption_tokens += nltk.word_tokenize(caption)
	
		#Addition of Start of Sentence <SOS> tag
		caption_tokens.append("<EOS>")
		caption_length=len(caption_tokens)

		#Adding the tokenized words into an array
		if caption_length in captions:
			captions[caption_length].add(caption_id)
		else:
			captions[caption_length]=set([caption_id])

		caption_id_to_words[caption_id]=caption_tokens
		caption_id_to_image_id[caption_id]=image_id
	
	#Returns the following:
	#captions - an array storing captions according to the length
	#caption_id_to_words - an array storing caption id along with its captions
	#caption_id_to_image_id - an array storing caption id along with the image id
	return captions,caption_id_to_words,caption_id_to_image_id
