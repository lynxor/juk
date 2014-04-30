

WIDTH = 19
HEIGHT = 22
PILL = "."
BONUS_PILL = "*"
MAX_IDLE_MOVES = 50

def position(playerId, state):
	return posFromIndex(getIndex(playerId, state))

def index(playerId, state):
	return state.index(playerId)
	
def posFromIndex(index):
	x = index % WIDTH
	y = index / WIDTH
	return (x,y)

def has_pill(state):
	return "." in state or "*" in state