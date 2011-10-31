class display_output:
	"""A class to show and modify displayed output"""

	def __init__(self, word):
		"""Initialize output to a ? for every character in the word"""
		self.output = ["?" for char in word]
	
	def accept(self, letter, indexes):
		"""Change each ? at the index specified to letter given"""
		for num in indexes:
			self.output[num] = letter
	
	def string(self):
		"""Call display_output.string() to show a string to the outside world"""
		return "".join(self.output)
