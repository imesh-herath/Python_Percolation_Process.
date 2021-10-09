from tabulate import tabulate   # Import tabulate module
from random import choice as rn # Import choice function from random module
import sys

import package.process

# Get console Arguments into list
arg = sys.argv					
size = arg[1].split('x')


# Get column size and row size from above list and convert it into Integer 
row=int(size[0])
col=int(size[1])


#row = int(input('r'))
#col = int(input('c'))


if not(2<col<10) or not(2<row<10):			#Check if grid size within the limit
	print('Error Occurred, Enter the values between 3x3 to 9x9')
	quit()


chrs = list(range(10,100))		# Create a list that contains random numbers from 10 to 99
chrs.extend(["  "]*10)			# Add 10 spaces to end of above list


grid = []						# Create empty list for store grid


filename=input('Enter name for file: ')  	# input a name for the text file
filename=filename+'.txt'					# Convert the code to a text file

package.process.percolation_func(row,col,grid,chrs,rn,filename)