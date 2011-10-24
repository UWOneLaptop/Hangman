	def contains(self, letter):
		picked.add(letter)
		if letter in word:
			self.goodletter(letter)
		else:
			self.badletter(letter)
