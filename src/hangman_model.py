class hangman_model:
	"""the Model component of the MVC design pattern.  This handles any
	deep ginormous computations and database operations."""

	def new_dictionary(self, dictionary):
		"""takes the specified dictionary file and selects a random
		word from it.  Returns the choosen word."""
