class hangman_controller:
	"""The controller of the MVC design pattern.  Handles events from the 
	user interface and does light logic.  Keeps track of the state of the
	game.   Passes big computations to the Model"""

	def __init__(self, view, model):
		"""Initializes the game with the specified view class as the 
		user interface, and the specified model class as the backend"""

	def start_game(self, dictionary):
		"""starts a new game using the specified dictionary"""

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