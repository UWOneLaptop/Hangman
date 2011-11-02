#!/usr/bin/env python

'''
Change
	def __init__(self): 
for
	def __init__(self, controller):
	self.controller = controller


Functions you'll find interesting:
	self.set_counter() updates the variable that counts the guesses left
	self.display_guesses_left() updates the GUI with the counter of guesses left
	self.set_word() updates the GUI with the word we are guessing
	self.reset_game() restarts all the GUI elements on new game, win, and loose
	self.key_pressed_event() gets triggered when a key is pressed on the keyboard or the screen, this should update the model via the controller (line 114, use self.controller)
'''

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os
from gettext import gettext as _

class HangManGUI:
	controller = None
	
	def display_guesses_left(self):
		print "Display number of guesses left"
		self.state_box.get_children()[0].set_text(_("Guesses left: ")+str(self.counter))
	
	def set_word(self, string):
		print "Display choosing letters"
		self.state_box.get_children()[2].set_text(string)
	
	def set_counter(self, counter):
		if counter >-1:
			print "Setting counter " + str(counter)
			self.counter = counter
			self.display_guesses_left()
			if counter == 6:
				self.state_box.get_children()[1].set_from_file("images/state_0.png")
			elif counter == 5:
				self.state_box.get_children()[1].set_from_file("images/state_1.png")
			elif counter == 4:
				self.state_box.get_children()[1].set_from_file("images/state_2.png")
			elif counter == 3:
				self.state_box.get_children()[1].set_from_file("images/state_3.png")
			elif counter == 2:
				self.state_box.get_children()[1].set_from_file("images/state_4.png")
			elif counter == 1:
				self.state_box.get_children()[1].set_from_file("images/state_5.png")
			elif counter == 0:
				self.state_box.get_children()[1].set_from_file("images/state_6.png")
	
	def new_game(self, widget, data=None):
		# confirm the creation of a new game
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Start a new game??"))
		dialog.set_title("Are you sure you want to start a new game?")
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES: # call reset_game()
			print "Creating new game"
			#look for current/changed difficulty level in self.difficulty_menu.get_active()
			self.reset_game()
	
	def win(self):
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Start a new game??"))
		dialog.set_title(_("Good job!, you just saved your life"))
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES: # call reset_game()
			print "Win"
			self.reset_game()
	
	def pass_away(self):
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Start a new game??"))
		dialog.set_title("Game over!, try again.")
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES: # call reset_game()
			print "Creating new game"
			self.reset_game()
	
	def reset_game(self):
		'''
		Resets the following class attributes:
		1. word_label
		2. chosen_letters_label
		3. state_image
		4. hint_label
		'''
		print "Resetting game"
		self.set_counter(6)
		self.state_box.get_children()[2].set_text("??????")
		self.main_box.get_children()[2].set_text(_("Hint: Please, press any key to play."))
		self.selected_letters = [""] * self.num_buttons
		self.letters_to_select = self.letters[:]
		self.display_letters_selected()
		self.display_letters_to_select()
	
	def key_pressed_event(self, widget, event, keyname=False):
		if keyname == False :
			keyname = gtk.gdk.keyval_name(event.keyval)
			keyname = keyname.upper()

		# update selected letters
		if (keyname in self.letters):
			letter_index = self.letters.index(keyname)
			self.selected_letters[letter_index] = keyname
			if self.letters_to_select[letter_index] != False:
				# removing hint
				self.main_box.get_children()[2].set_text("")
				print keyname + " key detected"
				# do something with the controller
				self.key_pressed_callback(keyname)

		# update the GUI
		self.display_letters_selected()
		self.display_letters_to_select()

	def delete_event(self, widget, event=None, data=None):
		print "destroy signal occurred"
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Are you sure you want to exit?"))
		dialog.set_title("Hang-man 1.0")
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES:
			gtk.main_quit()
			return False
		else:
			return True
	
	def display_letters(self, table, reference_table):
		'''
		Just a way to follow DRY for the below two methods, display_letters_to_select and display_letters_selected

		table: the gtk table, either letters_to_select_table or letters_selected_table
		reference_table: the reference table, either letters_to_select or letters_selected
		'''
		letter_button = None
		for i in xrange(30):
			row = i / 6
			col = i % 6
			if (reference_table[i] >= "A" and reference_table[i] <= "Z"):
				letter_button = gtk.Button(self.letters[i])
			       	letter_button.connect("clicked", self.key_pressed_event, False, self.letters[i])
		       	else:
	       			letter_button = gtk.Button(" ")
			table.attach(letter_button, col, col+1, row, row+1)

	def display_letters_to_select(self):
		if (self.letters_to_select_table):
			children = self.letters_to_select_table.get_children()
			for child in children:
				self.letters_to_select_table.remove(child)
		else:
			self.letters_to_select_table = gtk.Table(5, 6, True)
		
		self.display_letters(self.letters_to_select_table, self.letters_to_select)
		self.letters_to_select_table.queue_draw_area(0,0,-1,-1)
		self.letters_to_select_table.show_all()
	
	def display_letters_selected(self):
		if (self.letters_selected_table):
			children = self.letters_selected_table.get_children()
			for child in children:
				self.letters_selected_table.remove(child)
		else:
			self.letters_selected_table = gtk.Table(5, 6, True)

		self.display_letters(self.letters_selected_table, self.selected_letters)
		self.letters_selected_table.queue_draw_area(0,0,-1,-1)
		self.letters_selected_table.show_all()


	def __init__(self, callback):
		""" Accepts a callback function to call when a key is pressed """
		self.key_pressed_callback = callback
		self.counter = 6;
		self.new_game_button = gtk.Button(_("New Game"))
		self.exit_button = gtk.Button(_("Exit"))
		self.main_box = gtk.VBox(False, 0)
		self.game_box = gtk.HBox(False, 0)
		self.top_box = gtk.HBox(False, 0)
		self.state_box = gtk.VBox(False, 0)
		self.difficulty_menu = gtk.combo_box_entry_new_text()
		self.difficulty_menu.append_text("Difficulty level")
		self.difficulty_menu.append_text("Easy")
		self.difficulty_menu.append_text("Medium")
		self.difficulty_menu.append_text("Difficult")
		self.difficulty_menu.set_active(0)
		self.num_buttons = 30
		
		self.letters_selected_table = None
		self.letters_to_select_table = None

		self.letters = ["A", "B", "C", "D", " ", " ", "E", "F", "G", "H", " ", " ", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
		self.state_image = gtk.image_new_from_file('images/state_0.png')
		self.word_label = gtk.Label("??????")
		self.hint_label = gtk.Label(_("Hint: Please, press any key to play."))
		self.chosen_letters_label = gtk.Label("Chosen letters: ")
		self.guesses_left = gtk.Label(_("Guesses left: ")+str(self.counter))
		self.letters_selected_table = None
		self.letters_to_select_table = None
		self.selected_letters = [""] * self.num_buttons
		self.letters_to_select = self.letters[:]
		self.display_letters_selected()
		self.display_letters_to_select()
		
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Hang Man')
		self.window.connect("delete_event", self.delete_event)
		self.window.connect('key_press_event', self.key_pressed_event)
		
		self.top_box.pack_start(self.new_game_button, False, False, 0)
		self.top_box.pack_start(self.difficulty_menu, False, False, 0)
		self.top_box.pack_end(self.exit_button, False, False, 0)
		
		self.state_box.pack_start(self.guesses_left, True, True, 0)
		self.state_box.pack_start(self.state_image, True, True, 0)
		self.state_box.pack_start(self.word_label, True, True, 0)
		
		self.game_box.pack_start(self.letters_to_select_table, True, True, 0)
		self.game_box.pack_start(self.state_box, True, True, 0)
		self.game_box.pack_start(self.letters_selected_table, True, True, 0)
		
		self.main_box.pack_start(self.top_box, False, True, 0)
		self.main_box.pack_start(self.game_box, True, True, 0)
		self.main_box.pack_start(self.hint_label, True, True, 0)
		
		self.window.add(self.main_box)
		
		self.window.show_all()

	def main(self):
		gtk.main()

if __name__ == "__main__":
	HangMan = HangManGUI()
	HangMan.main()
'''
guess another letter
glowing if not available
sounds
	option to turn off
	clapping hands
	woa woa woa woaaaaaa
toggle for displaying hints yes/ no
'''
