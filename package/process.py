from tabulate import tabulate   # Importing tabulate module
from random import choice as rn # Import choice function from random module

def percolation_func(row,col,grid,chrs,rn,filename):

    #+++++++++++++++++++ Process of the grids ++++++++++++++++++++++++++++++++

    for x in range(row):
        ROW = [rn(chrs) for i in range(col)]	# Create a row using choice function
        grid.append(ROW)			# Add that row into grid


    #++++++++++++++++++ Process of the 'OK', 'NO' ++++++++++++++++++++++++++++

    kn = []								# This list store OK or NO for each column in grid

    for x in range(col):
        # List for store column in grid
        column = []
        for y in grid:
            column.append(y[x])
            
        if '  ' in column:
            kn.append(' NO')
        else: 
            kn.append(' OK')
    #print(grid)
    #print(kn)
            
    #+++++++++++++++++++ Process of the text file ++++++++++++++++++++++++++++

    with open(filename, 'w') as file:
        gr = tabulate(grid,tablefmt='grid')		# Create grid with tabulate function 
        # Write the grid into text file
        file.write(gr)
        file.write('\n')
        # Write OK or NO
        for x in kn:
            file.write(' '+x+' ')

        
    #++++++++++++++++++++ Output +++++++++++++++++++++++++++++++++++++++++++++

    print(gr)						# output of the grid
    for x in kn:					# output of the OK or NO
        print(' '+x, end=' ')
