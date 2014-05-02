from helpers import *

with open("initial.state", "r") as file:
	state_str = file.read()
	state = parse_state(state_str)
	# print str(state)
	# print position("A", state)
	# print position("B", state)
	print str(clone_state(state))
	print serialize_state(clone_state(state))



