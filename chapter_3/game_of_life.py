# Conways game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of cells
next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

#Main program loop
while True:
    print('\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

    # Print current cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pass
            print(current_cells[x][y], end='')
        print()
    
    # Calculate next cells based off current cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            coord_pairs = [
                [left_coord, above_coord],
                [x, above_coord],
                [right_coord, above_coord],
                [left_coord, y],
                [right_coord, y],
                [left_coord, below_coord],
                [x, below_coord],
                [right_coord, below_coord]
            ]

            # Count number of living neighbors around a cell
            num_neighbors = 0
            for coords in coord_pairs:
                if current_cells[coords[0]][coords[1]] == '#':
                    num_neighbors += 1
            
            if current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            elif current_cells[x][y] == '#' and not (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = ' '
    time.sleep(0.5)
                