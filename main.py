import time
from life import *

#--------------------------

board = random_state(100, 50)
render(board)

while (True):
    board = next_board_state(board)
    render(board)
    time.sleep(0.5)