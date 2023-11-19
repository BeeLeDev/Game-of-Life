from life import *

#--------------------------

board = random_state(5, 5)
render(board)
new_board = next_board_state(board)
render(new_board)

