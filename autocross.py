# We will first have to read the provided grid
# It will work as follow :
# autocross.py -g <Path to grid>

# Imports
# -> sys allows us to use system calls
import sys
# Testing if a file exist ; later opening it.
from pathlib import Path
# Regular Expressions are life
import re


# This function will create the grid
def fcreate(grid_id):
    gridfile = open(grid_id['grid'], "r")
    # Here, we're going through the entire file, getting the values we need.
    # Still working on a pretty way to make the dictionary !
    for line in gridfile:
        if "width" in line:
            grid_id['width'] = re.sub('[A-z]', '', line).strip()
        if "height" in line:
            grid_id['height'] = re.sub('[A-z]', '', line).strip()
        if "rows" in line:
            # Get all the rows values until something else ? Or EOF
        if "columns" in line:
            # Get all the columns values until something else ? Or EOF
    # end of the for
    gridfile.close()
    return grid_id
    pass


# This function will be used to display the current grid.
def fdisplay(grid):
    return
    pass


# This function will be used to solve the current grid. Main function I guess !
def fsolve(grid):
    return
    pass


# I'll change the arg getter to put it in here later.
def fname(arglist):
    return
    pass


# Script's body. Most of the code will happen in the functions
def main(argv):
    # Here we define what will be the grid file we'll open.
    # We also define all of the variables used to define the grid in itself
    grid = ''
    width = 0
    height = 0
    rows = dict()
    columns = dict()
    goal = 0
    grid_id = {'grid': grid, 'width': width, 'height': height, 'rows': rows, 'columns': columns, 'goal': goal}
    # Define - end
    if argv[1] == '-g':
        # We now have to test if the file exists.
        is_file = Path(argv[2])
        if not is_file.is_file():
            print("File doesn't exist !")
            pass
        else:
            # Getting the specified file.
            grid_id['grid'] = argv[2]
            print("The file " + grid_id['grid'] + " exists. Now creating the grid.")
            # We will now create the grid by reading the given file
            grid_id = fcreate(grid_id)
            print("width = " + grid_id['width'])
            pass
    else:
        print('Wrong option ! Please use -g to specify the grid you want to open.')
        pass


# Now we run it !
if __name__ == '__main__':
    main(sys.argv)
