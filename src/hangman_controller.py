class hangman_controller:
	"""The controller of the MVC design pattern.  Handles events from the 
	user interface and does light logic.  Keeps track of the state of the
	game.   Passes big computations to the Model"""

	def __init__(self, view):
		"""Initializes the game with the specified user interface as
		the view"""

	def start_game(self, dictionary):
		"""starts a new game using the specified dictionary"""

	def guess_letter(self, letter):
		"""called when the user picks their next letter.  Will update
		the view with the results (good letter?  bad letter?  you win?
		you LOSE? (good DAY sir!))"""
