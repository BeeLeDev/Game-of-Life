import random

'''
Milestones:

1. Build a data structure to store the board state *
2. “Pretty-print” the board to the terminal *
3. Given a starting board state, calculate the next one
4. Run the game forever

################

Extensions:

1. Save interesting starting positions to files and add the ability to reload them into your Life
2. Improve the User Interface
3. Change the rules of Life
''' 

def random_state(width, height):
    '''Returns a board with 0's and 1's randomly assigned'''

    # create multi-dimensional array
    board_state = [[0 for _ in range(width)] for _ in range(height)]

    # randomize the states
    for col in range(width):
        for row in range(height):
            # 0 dead
            # 1 alive
            board_state[row][col] = random.randint(0, 1)
    return board_state

def render(board_state):
    '''Renders the board to the terminal'''

    for _ in range(len(board_state[0]) + 1):
        print('-', end='')
    print('-')

    for row in board_state:
        print('|', end='')
        for x in row:
            if (x == 1):
                print('#', end='')
            else:
                print(' ', end='')
        print('|')

    for _ in range(len(board_state[0]) + 2):
        print('-', end='')
    print()

def next_board_state(board_state):
    '''Given the initial board state, calculate and return next board state'''

    row = len(board_state)
    col = len(board_state[0])

    # create a new board to store the next state
    new_board_state = [[0 for _ in range(col)] for _ in range(row)]

    for x in range(row):
        for y in range(col):
            live_neighbors = 0

            # iterate through neighboring cells
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # skip the current cell
                    if i == 0 and j == 0:
                        continue

                    # calculates the indices of neighboring cell
                    # modulus arithmetic allows us to wrap around, so the top row will check the bottom row
                    ni = (x + i) % row
                    nj = (y + j) % col

                    # checks if the neighboring cell is alive
                    if board_state[ni][nj] == 1:
                        live_neighbors += 1

            # apply the rules
            #1. any live cell with 0 or 1 live neighbors becomes dead, because of under population
            #2. any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
            #3. any live cell with more than 3 live neighbors becomes dead, because of overpopulation
            #4. any dead cell with exactly 3 live neighbors becomes alive, by reproduction
            if board_state[x][y] == 1:
                # rule 1 and rule 3
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board_state[x][y] = 0
                # rule 2
                else:
                    new_board_state[x][y] = 1
            else:
                # rule 4
                if live_neighbors == 3:
                    new_board_state[x][y] = 1

    return new_board_state

