class hangman_model:
	"""the Model component of the MVC design pattern.  This handles any
	deep ginormous computations and database operations."""

	def __init__(self):
		# Define the different dictionaries
		return None

	def generate_word(self, dictionary):
		"""takes the specified dictionary file and selects a random
		word from it.  Returns the choosen word."""
		return self.loadDic()

	def loadDic(self, lang = "en"):
		"""Load file lang_dict.txt and pick a word from it at random"""
		# import random library to make choice
		from random import choice
		# Read dictionary line by line and turn into list
		filename = lang+'_dict.txt'
		dictionary = open(filename).readlines()
		# return random entry with \n (new line) character stripped and made lower-case (this could be changed if dictionary is double checked for desired case, or case is made non-important by letter guesser aspect of program)
		return choice(dictionary).rstrip().lower()
