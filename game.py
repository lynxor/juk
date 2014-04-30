#!/bin/python2

import os
from os import listdir
import re
import argparse
import signal
from processes import *


signal.signal(signal.SIGINT, signal.SIG_DFL)
verbose = False

parser = argparse.ArgumentParser(description='Bots in')


parser.add_argument("-v", "--verbose", dest="verbose", help="Be verbose.")
parser.add_argument("player1", help='Player 1 exec.')
parser.add_argument("player2", help='Player 2 exec.')
parser.add_argument("-i", "--initial", dest="initial", help="Initial state.", default="./initial.state")

args = parser.parse_args()

if args.player1 != None and args.player2 != None:
	player1 = Player("A", args.player1)
	player2 = Player("B", args.player2)


	with open(args.initial) as initial_state_file:
		state = str(initial_state_file.read())
		game = Game(player1, player2,  state)
		game.start()

	



