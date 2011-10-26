def loadDic(lang = "en"):
	"""Load file lang_dict.txt and pick a word from it at random"""
	# import random library to make choice
	from random import choice
	# Read dictionary line by line and turn into list
	dictionary = open(lang+"_dict.txt").readlines()
	# return random entry with \n (new line) character stripped and made lower-case (this could be changed if dictionary is double checked for desired case, or case is made non-important by letter guesser aspect of program)
	return choice(dictionary).rstrip().lower()
