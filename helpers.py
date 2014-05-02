

WIDTH = 19
HEIGHT = 22
PILL = "."
BONUS_PILL = "*"
WALL = "#"
MAX_IDLE_MOVES = 50
CENTER_POS = (9,10)

def parse_state(state_string):
	# print(list(state_string))
	return [list(row) for row in state_string.split("\r\n")]  #WTF windows \r\n

def serialize_state(state):
	return "\r\n".join(["".join(row) for row in state])

def position(playerId, state):
	for (n, row) in enumerate(state):
		if playerId in row:
			return (row.index(playerId), n) 		

def has_pill(state):
	flat_state = flatten(state)
	return "." in flat_state or "*" in flat_state

def value_at(pos, state):
	x = pos[0]
	y = pos[1]

	return state[y][x]

def set_value(pos, value, state):
	# print "SETTING VALUE" + str(value) + " st " +str(state)
	x = pos[0]
	y = pos[1]
	state[y][x] = value
	return state

def flatten(state):
	return [item for sublist in state for item in sublist]

def swop_symbols(state):
	apos = position("A", state)
	bpos = position("B", state)

	set_value(apos, "B", state)
	set_value(bpos, "A", state)
	return state

def clone_state(state):
	return [list(row) for row in state]

