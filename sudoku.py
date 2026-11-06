import random
# Board size (N x N)
N = 9

# to be placed
rows = [x for x in range(N)]

# placeholder for a board
board = [[0 for _ in range(N)] for _ in range(N)]

def display_board(): 
    for kk in range(N):
        print(board[kk])

# Place the first number. (WLOG -- 1)
# For every number, and every row, we will have a forbidden columns list. 
# For row 0, no forbidden column 
# For row 1, the columns that are in the square are forbidden. 
# For row 2, the columns in the square and previously occupied columns are forbidden

# We will maintain a dictionary called forbidden for every row. 

forbidden = dict.fromkeys(rows)
occupied = dict.fromkeys(rows)
# The values of this dictionary will be lists. 

# Columns get forbidden by 
# Occupancy 
# Dynamic due to rules. 

# Initialize forbidden
for f in forbidden:
    forbidden[f] = []
for f in occupied:
    occupied[f] = []
# num is the number to be placed. 
# We can randomize the order later. 

for num in range(1, 5): 
    # place for every row
    for r in range(N): 
        # Pick a column from the open columns
        openc = [x for x in range(N) if x not in forbidden[r] and x not in occupied[r]]; 
        if not openc: 
            input('problem')
            # need to backtrack
        c = random.choice(openc)
        board[r][c] = num    
        occupied[r].append(c);
        # For all columns
        for j in range(r, N):
            forbidden[j].append(c)
        #print(c, forbidden)

    for r in range(N):
        forbidden[r].clear() 


display_board()




