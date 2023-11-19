from life import *

#--------------------------

board = random_state(50, 50)
render(board)

while (True):
    board = next_board_state(board)
    render(board)

