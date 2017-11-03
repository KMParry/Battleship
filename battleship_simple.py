import sys
import random

class board():

	def __init__(self):
		
		self.grid = []
		self.ships={}

	def create_board(self):

		self.grid = [['0' for x in range(10)] for y in range(10)]
		self.ships={}
	
	def print_board(self):
		
		for i in range(len(self.grid)):		
			print self.grid[i]
		
	def add_ship(self,row, col, direction, size, symbol):
		
		# check input		
		if row not in range(1,10):
			print "Row format is incorrect. Try numeric value in range (1,10)."
			return 0
		if col not in range(1,10):
			print "Column format is incorrect. Try numeric value in range (1,10)."
			return 0
		if size not in range(1,10):
			print "Ship size format is incorrect. Try numeric value in range (1,10)."
			return 0
		if symbol == 'H' or symbol == 'M' or symbol == '0':
			print "Choose a different symbol, excluding 'H' or 'M' or '0'"
			return 0

		if direction == 'h':

			if col-1 + size -1 > 9:
				print "Your ship is out of bounds!"
				return 0
	
			for j in range(col -1, col -1 + size):
				if self.grid[row-1][j] != '0':
					print "This spot is occupied."
					return 0
			
			for j in range(col -1, col -1 + size):
				self.grid[row-1][j] = str(symbol)
		
			self.ships.update({symbol:size})
			return 1

		if direction=='v':
			
			if row - 1 + size -1 > 9:
				print "Your ship is out of bounds!"
				return 0
	
			for i in range(row-1, row-1 + size):
				if self.grid[i][col-1] != '0':
					print "This spot is occupied."
					return 0
			
			for i in range(row-1, row-1 + size):
				self.grid[i][col-1] = str(symbol)	

			self.ships.update({str(symbol):size})
			return 1

	def check_if_sunk(self,elem):
		
		if self.ships[elem] == 0:
			return 1
		else:
			return 0

	def check_if_winner(self):
		
		count = 0
	
		for ship, vals in self.ships.iteritems():
			count += vals 
	
		if count == 0:
			return 1
		else:
			return 0

	def attack(self, row, col):
		
		# check input
		if row not in range(1,10):
			print "Row format is incorrect. Try numeric value in range (1,10)."
			return 0
		if col not in range(1,10):
			print "Column format is incorrect. Try numeric value in range (1,10)."
			return 0
		
		# check value of the board
		elem = self.grid[row-1][col-1]		

		if elem =="H" or elem == "M":
			print "Already Taken"
			return 1
		elif elem == "0":
			print "Miss"
			self.grid[row-1][col-1]="M"
			return 1
		elif elem != '0' and elem !="H" and elem !="M":
			print "Hit"
			
			self.grid[row-1][col-1] = "H"
			self.ships[elem] -= 1

			if self.check_if_sunk(elem):
				print "Sunk"
			if self.check_if_winner():
				print "Win"
			return 1	
		
	
def main():

	
	user_board = board()
	user_board.create_board()
	print "\n Initial board"
	user_board.print_board()

	print "\n++++++ Unit test 1 ++++++"
	print "Add a single ship"
	success=user_board.add_ship(1,1,'v',3,'X')
	user_board.print_board()
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"


	print "\n+++++++ Unit test 2 +++++++"
	print "Check overlapping points..."
	user_board.create_board()
	success=user_board.add_ship(1,1,'v',3,'X')
	success=user_board.add_ship(2,4,'h',4,'B')
	success=user_board.add_ship(9,4,'h',2,'C')
	success=user_board.add_ship(7,4,'v',3,'A')
	user_board.print_board()
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"
	
	print "\n+++++++ Unit test 3 +++++++"
	print "Try adding a ship out of bounds."
	user_board.create_board()
	success=user_board.add_ship(1,1,'v',3,'X')
	success=user_board.add_ship(2,10,'h',4,'B')
	user_board.print_board()
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"

	print "\n+++++++ Unit test 4 +++++++"
	print "Try adding a non-numeric value for row/col/size and bad symbol"
	user_board.create_board()
	success=user_board.add_ship('a',1,'v',3,'X')
	success=user_board.add_ship(2,'f','h',4,'B')
	success=user_board.add_ship(2,1,'h',10,'B')
	success=user_board.add_ship(2,1,'h','f','B')
	success=user_board.add_ship(2,1,'h',4,'H')
	success=user_board.add_ship(2,1,'h',4,3)
	user_board.print_board()
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"
	
	print "\n+++++++ Unit test 5 +++++++"
	print "Test a single attack."
	user_board.create_board()
	success = user_board.add_ship(1,1,'v',3,'X')
	success = user_board.add_ship(2,2,'h',4,'B')
	user_board.print_board()
	success = user_board.attack(1,1) 
	user_board.print_board()
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"
	
	print "\n+++++++ Unit test 6 +++++++"
	print "Test a series of attacks to win."
	user_board.create_board()
	success = user_board.add_ship(1,1,'v',3,'X')
	user_board.print_board()
	success = user_board.attack(1,1) 
	success = user_board.attack(2,1) 
	success = user_board.attack(3,1) 
	if success:
		print "Test passed"
	else:
		print "Test failed"
	print "++++++++++++++++++++++++++++++++++++++++"

if __name__ == "__main__":

	main()	
