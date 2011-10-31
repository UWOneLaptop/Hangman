from HangManGUI import *
from hangman_model import *
from display_output import *

class hangman_controller:
	"""The controller of the MVC design pattern.  Handles events from the 
	user interface and does light logic.  Keeps track of the state of the
	game.   Passes big computations to the Model"""

	def start_game(self, widget, data = None):
		"""starts a new game using the specified dictionary"""
		"""code for game until end of game..."""
		dictionary = "en_dict.txt" # get the dict from the view
		self.word = self.model.generate_word( dictionary )
		self.display_string = display_output( self.word )
		self.picked.clear()
		# reset the view
		self.view.new_game(widget)
		print "pssssst word is " + self.word

	def next_letter_event(self, widget, event, keyname=False):
		if keyname == False :
			keyname = gtk.gdk.keyval_name(event.keyval)
			keyname = keyname.upper()

		# update selected letters
		if (keyname in view.letters):
			letter_index = view.letters.index(keyname)
			view.selected_letters[letter_index] = keyname
			if view.letters_to_select[letter_index] != False:
				# removing hint
				view.main_box.get_children()[2].set_text("")
				print keyname + " key detected"
				view.next_letter(keyname.lower())

		view.display_letters_selected()
		view.display_letters_to_select()

	def next_letter(self, letter):
		"""called when the user picks their next letter.  Will update
		the view with the results (good letter?  bad letter?  you win?
		you LOSE? (good DAY sir!))"""
		print letter + " next, "
		if self.isInvalid( letter ) or self.isRepeat( letter ):
			return
		# Letter is good to check!
		if letter in self.word :
			self.goodletter( letter )
		else:
			self.badletter( letter )
		self.picked.add( letter )

	def isInvalid(self, letter):
		letter = letter.lower()
		print 'ord of ' + letter + ' is ' + str(ord(letter))
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
			i = None # temp to compile

	def badletter(self, letter):
		print letter + " is bad"
		count = self.view.counter - 1
		self.view.set_counter(count) 
		if count == 0 :
			# end the game !
			i = None # temp to compile

	def exit(self, widget, data=None):
		print "Exiting"
		return self.view.delete_event(widget)

	def __init__(self, view, model):
		"""Initializes the game with the specified view class as the 
		user interface, and the specified model class as the backend"""
		self.view = view
		self.model = model
		self.display_string = None
		self.picked = set()
		self.word = None

		view.new_game_button.connect("clicked", self.start_game, None)
		view.exit_button.connect("clicked", self.exit, None)

if __name__ == "__main__":
	""" Initialize the entire game """
	hangman = HangManGUI()
	model = hangman_model()
	controller = hangman_controller(hangman, model)
	hangman.main()
	""" A test script to make sure our stuff compiles """
	#controller.start_game("dks")
	controller.next_letter("d")
	controller.next_letter("d")
