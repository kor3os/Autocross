# We will first have to read the provided grid
# It will work as follow :
# autocross.py -g <Path to grid>

#Imports
# -> sys allows us to use system calls
import sys
# Testing if a file exist ; later opening it.
from pathlib import Path
#This function will be used to display the current grid.
def fdisplay(grid):
	return
	pass
# This function will be used to solve the current grid. Main function I guess !
def fsolve(grid):
	return
	pass
# I'll change the arg getter to put it in here later.
def fname(arglist):
	pass
# Script's body. Most of the code will happen in the functions
def main(argv):
	# Here we define what will be the grid file we'll open.
	grid = ''
	if argv[1] == '-g':
		# We now have to test if the file exists. Yes, using 'break' is bad.
		is_file = Path(argv[2])
		if not is_file.is_file():
			print("File doesn't exist !")
			pass
		else:
		# Getting the specified file.
			grid = argv[2]
			print(grid)
			pass
	else:
		print('Wrong option ! Please use -g to specify the grid you want to open.')
		pass

# Now we run it !
if __name__ == '__main__':
	main(sys.argv)
