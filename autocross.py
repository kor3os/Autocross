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
    # Just wanna clear out the warnings
    width, height, reach, goal = '', '', '', ''
    idx_cols, idx_rows = 0, 0
    rows, columns = dict(), dict()
    lines = gridfile.readlines()

    for i, line in enumerate(lines):
        if "width" in line:
            width = re.sub('[A-z]', '', line).strip()
            pass
        if "height" in line:
            height = re.sub('[A-z]', '', line).strip()
            pass
        if "rows" in line:
            # Get all the rows values until something else ? Or EOF
            idx_rows = i
            pass
        if "columns" in line:
            # Get all the columns values until something else ? Or EOF
            idx_cols = i
            pass
        if "goal" in line:
            goal = re.sub('[A-z"]', '', line).strip()
            pass
    # end of the for
    # We now have to get the values we want !
    grid_id['width'] = int(width)
    grid_id['height'] = int(height)
    # It was too annoying to strip a dict in a dict so I made a quick and simple function
    grid_id['rows'] = lines[idx_rows+1:idx_rows+1+grid_id['height']]
    stripdict(grid_id['rows'])
    grid_id['columns'] = lines[idx_cols+1:idx_cols+1+grid_id['width']]
    stripdict(grid_id['columns'])
    # Reach = goal with zeros
    grid_id['reach'] = re.sub('[1]', '0', goal)
    grid_id['goal'] = goal
    # We now close the file and return what we created !!
    gridfile.close()
    return grid_id
    pass


# This function will be used to display the current grid.
def fdisplay(grid_id):

    return
    pass


# This function will be used to solve the current grid. Main function I guess !
def fsolve(grid_id):
    return
    pass


# I'll change the arg getter to put it in here later.
def fname(arglist):
    return
    pass


def stripdict(dico):
    i = 0
    while i < len(dico):
        dico[i] = dico[i].strip()
        i += 1
    return dico
    pass


# Script's body. Most of the code will happen in the functions
def main(argv):
    # Here we define what will be the grid file we'll open.
    # We also define all of the variables used to define the grid in itself
    # This is the file leading to the grid
    grid = ''
    # Width of the grid
    width = 0
    # Height of the grid
    height = 0
    # The rows' hints
    rows = dict()
    # The columns' hints
    columns = dict()
    # Same length as goal, contains only zeros at first
    # Compared to goal while solving, and evolves depending on which case you fill in
    reach = 0
    # The final goal; bool value of the case where 0 = empty and 1 = filled in
    goal = 0
    # This is a dictionary containing all of the values we need to display or solve the grid !
    grid_id = {
        'grid': grid, 'width': width, 'height': height, 'rows': rows, 'columns': columns, 'reach': reach, 'goal': goal
    }
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
            pass
    else:
        print('Wrong option ! Please use -g to specify the grid you want to open.')
        pass


# Now we run it !
if __name__ == '__main__':
    main(sys.argv)
