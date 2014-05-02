#!/bin/python2

import os
from os import listdir
import re
import argparse
import signal
from processes import *
from helpers import *


signal.signal(signal.SIGINT, signal.SIG_DFL)
verbose = False

parser = argparse.ArgumentParser(description='Bots in')


parser.add_argument("-v", "--verbose", dest="verbose", help="Be verbose.")
parser.add_argument("player1", help='Player 1 exec.')
parser.add_argument("player2", help='Player 2 exec.')
parser.add_argument("-i", "--initial", dest="initial", help="Initial state.", default="./initial.state")
parser.add_argument("-iA", "--interactiveA", action="store_true", dest="interactiveA", default=False, help="player A interactive or not")
parser.add_argument("-iB", "--interactiveB", action="store_true", dest="interactiveB", default=False, help="player B interactive or not")

args = parser.parse_args()

if args.player1 != None and args.player2 != None:
	player1 = Player("A", args.player1, args.interactiveA)
	player2 = Player("B", args.player2, args.interactiveB)


	with open(args.initial) as initial_state_file:
		state = str(initial_state_file.read())
		game = Game(player1, player2,  state)
		game.start()

	



