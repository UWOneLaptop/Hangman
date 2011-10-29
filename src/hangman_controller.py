class hangman_controller:
	"""The controller of the MVC design pattern.  Handles events from the 
	user interface and does light logic.  Keeps track of the state of the
	game.   Passes big computations to the Model"""
	
	def __init__(self, view, model):
		"""Initializes the game with the specified view class as the 
		user interface, and the specified model class as the backend"""
		self.picked = set()
		self.word = None


	def start_game(self, dictionary):
		"""starts a new game using the specified dictionary"""
		"""code for game until end of game..."""
		self.picked.clear

	def guess_letter(self, letter):
		"""called when the user picks their next letter.  Will update
		the view with the results (good letter?  bad letter?  you win?
		you LOSE? (good DAY sir!))"""
		
	def goodletter(self, letter):
		temp = display_output.word
		a = []
		for n in range (0, len(temp)):
			if letter == temp[n]:
				a.append(n)
		display_output.accept(self, letter, a)

	def isValid(self, letter):
		letter = letter.lower()
		if(ord(letter) < 97 or ord(letter) > 122):
			return False
		else:
			return not self.isRepeat(letter)

	def isRepeat(self, letter):
		if(letter in self.picked):
			return True
		else:
			return False		

