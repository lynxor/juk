import os
from os import listdir
from os.path import isfile, join, walk
import subprocess
import tempfile
from helpers import *

class Player:
	def __init__(self, id, folder, interactive=False):
		self.id = id
		self.folder = folder
		self.log = join(folder, "out.log")
		self.game_state_file = join(folder, "game.state")
		self._exec = "./run"
		self.score = 0
		self.pill = True  # keep track of the pill? Maybe later
		self.score_unchanged = 0
		self.interactive = interactive

	def state(self):
		with open(self.game_state_file, 'r') as content_file:
			return content_file.read()

	def move(self):	
		old_state = self.state()
		LOG = open(self.log, 'w')
		prev_path = os.getcwd()

		#make the move
		os.chdir(self.folder)
		# print prev_path + " " + os.getcwd()
		# print self.game_state_file
		# process = subprocess.Popen(["bash", "-c", self._exec +" "+ self.game_state_file ], stdout=LOG, stderr=LOG)
		if not self.interactive:
			process = subprocess.Popen([ self._exec, self.game_state_file ], stdout=LOG, stderr=LOG)
			output = process.communicate()[0]
		else:
			self.move_interactive(old_state)

		os.chdir(prev_path)
		new_state = self.state()
		self.update_score(old_state, new_state)
		return new_state

	def move_interactive(self, current_state):
		print "Your move: (W,A,S,D) "
		move = str(raw_input()).upper()
		pos = position("A", current_state)  #AGAIN, always A
		x = pos[0]
		y = pos[1]
		if move == "W":
			new_pos = (x, (y - 1) if y > 0 else HEIGHT - 1) 
		elif move == "S":
			new_pos = (x, (y + 1) if y < HEIGHT - 1 else 0)
		elif move == "A":
			new_pos = (x - 1 if x > 0 else WIDTH -1, y) 
		elif move == "D":
			new_pos = (x + 1 if x < WIDTH -1 else 0, y)

		if self.valid_pos( new_pos, current_state):
			new_state = set_value(new_pos, "A", current_state)
			new_state = set_value(pos, " ", new_state)
			self.write_state(new_state)
		else:
			print "Invalid move specified"
			self.move_interactive(current_state)



	def valid_pos(self, pos, state ):
		print str(pos)
		x = pos[0]
		y = pos[1]
		if not ((x >= 0 and x <= WIDTH - 1 ) and (y >= 0 and y <= HEIGHT)) :
			print "Out of bounds : " + str(pos)
			return False
		elif value_at(pos, state) == WALL:
			print "That is a wall"
			return False
		return True

	def update_score(self, old_state, new_state):
		# print "UPDATING SCORES "+ self.id+ " " +old_state + new_state

		#NB ALWAYS LOOK FOR A - player is always A
		newidx = index("A", new_state) 
		if old_state[newidx] ==  PILL:
			self.score += 1
			self.score_unchanged = 0

		elif old_state[newidx] ==  BONUS_PILL:
			self.score += 10
			self.score_unchanged = 0
		else:
			self.score_unchanged += 1


	def write_state(self, status):
		print self.game_state_file
		with open(self.game_state_file, "w") as the_file:
			the_file.write(str(status))


class Game:

	def __init__(self, playerA, playerB, initial):
		self.playerA = playerA
		self.playerB = playerB
		self.initial = initial
		self.playerA.write_state(initial)

	def swop_symbols(self, state):
		state = state.replace("A", "C")
		state = state.replace("B", "A")
		return state.replace("C", "B")

	def game_over(self, state):
		return (not has_pill(state)) or (self.playerA.score_unchanged >= MAX_IDLE_MOVES and self.playerB.score_unchanged >= MAX_IDLE_MOVES)

	def winner(self):
		if self.playerA.score > self.playerB.score:
			return self.playerA.id
		elif self.playerB > self.playerA.score:
			return self.playerB.id
		else:
			return None;

	def print_score(self):
		print "\n********** Scores: A - " + str(self.playerA.score) + "| B - " + str(self.playerB.score) + " *******\n\n\n"

	def start(self):
		# for a in range(1):
		print "Initial State\n" + self.initial
		while True:
			if self.game_over(self.playerA.state()):
				break

			self.playerA.move()
			self.playerB.write_state( 
				self.swop_symbols( self.playerA.state() ) )
			print "\nMoved player A \n" + self.playerA.state() 
			self.print_score()

			if self.game_over(self.playerB.state()):
				break
			
			self.playerB.move()
			self.playerA.write_state( 
				self.swop_symbols(self.playerB.state() ) )
			print "\nMoved player B \n" + self.playerA.state() 
			self.print_score()

		winner = self.winner()
		print "Draw" if winner == None else "Congrats player " + winner


   

