from HangManGUI import *
from hangman_model import *
from display_output import *

class hangman_controller:
	"""The controller of the MVC design pattern.  Handles events from the 
	user interface and does light logic.  Keeps track of the state of the
	game.   Passes big computations to the Model"""

	def start_game_event(self, widget, data = None):
		self.start_game()
		self.view.new_game(widget)

	def start_game(self):
		"""starts a new game using the specified dictionary"""
		"""code for game until end of game..."""
		dictionary = "en_dict.txt" # get the dict from the view
		self.word = self.model.generate_word( dictionary ).lower()
		self.display_string = display_output( self.word )
		self.picked.clear()
		# reset the view
		print "pssssst word is " + self.word

	def next_letter(self, letter):
		"""called when the user picks their next letter.  Will update
		the view with the results (good letter?  bad letter?  you win?
		you LOSE? (good DAY sir!))"""
		letter = str(letter).lower()
		if self.isInvalid( letter ) or self.isRepeat( letter ):
			return
		# Letter is good to check!
		if letter in self.word :
			self.goodletter( letter )
		else:
			self.badletter( letter )
		self.picked.add( letter )
		print "picked so far " + str(self.picked)

	def isInvalid(self, letter):
		print 'ordinal of ' + letter + ' is ' + str(ord(letter))
		return ord(letter) < 97 or ord(letter) > 122

	def isRepeat(self, letter):
		print letter + ' already picked? ' + str(letter in self.picked)
		return letter in self.picked

	def goodletter(self, letter):
		print letter + " is good"
		temp = self.word
		a = []
		for n in range (0, len(temp)):
			if letter == temp[n]:
				a.append(n)
		self.display_string.accept( letter, a )
		
		shown_word = self.display_string.string()
		# update the UI's displayed word
		self.view.set_word(shown_word)
		if shown_word == self.word :
			# win the game !
			self.view.win()

	def badletter(self, letter):
		print letter + " is bad"
		count = self.view.counter - 1
		self.view.set_counter(count) 
		if count == 0 :
			# end the game !
			self.view.pass_away()

	def exit(self, widget, data=None):
		print "Exiting"
		return self.view.delete_event(widget)

	def main(self):
		self.start_game()
		self.view.main()

	def __init__(self):
		"""Initializes the game with the specified view class as the 
		user interface, and the specified model class as the backend"""
		self.view = HangManGUI(self.next_letter) # pass in a callback for keypresses
		self.model = hangman_model()
		self.display_string = None
		self.picked = set()
		self.word = None

		self.view.new_game_button.connect("clicked", self.start_game_event, None)
		self.view.exit_button.connect("clicked", self.exit, None)
		
		self.main()

if __name__ == "__main__":
	""" Initialize the entire game """
	controller = hangman_controller()
	""" A test script to make sure our stuff compiles """
	#controller.start_game("dks")
