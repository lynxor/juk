

WIDTH = 19
HEIGHT = 22
PILL = "."
BONUS_PILL = "*"
WALL = "#"
MAX_IDLE_MOVES = 50

#NBNBNBNB Remember to add 1 to index calculations because of \n 


def position(playerId, state):
	return pos_from_index(index(playerId, state))

def index(playerId, state):
	return state.index(playerId)
	
def pos_from_index(index):
	print "index is " + str(index)
	x = index % (WIDTH + 1)
	y = index / (WIDTH + 1)
	return (x,y)

def ind_from_pos(pos):
	return pos[1] * (WIDTH  + 1) + pos[0]

def has_pill(state):
	return "." in state or "*" in state

def value_at(pos, state):
	return state[ind_from_pos(pos)]

def set_value(pos, value, state):
	l_state = list(state)
	l_state[ind_from_pos(pos)] = value
	return "".join(l_state)