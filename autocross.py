# We will first have to read the provided grid
# It will work as follow :
# autocross.py -g <Path to grid>
# TODO: FIX THE ERROR WHEN THERE'S NO ARG
# TODO: Edit funcs to make them return 0 or 1 (0 on success, 1 on fail)
# TODO: make a dynamic display function, like "press 1 for finished state, 2 for current"
# TODO: Make a "dot" class that contains the (x, y) coordinates and the status of the dot maybe ? ("x" or "o")
# TODO: Complete flignify; creates 2 dict() with the rows and columns (taken from the "reach" var)
# TODO: Complete the "obvious algorithm" list in order to make the solving job easier.
# ^ Where do we go from here ? Algorithms or AI ?

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


# This function will be used to display the current grid, but in the current solved state.
def fdisplaycurrent(grid_id):
    # Vars we need.
    # Basically the same thing as below.
    width = grid_id['width']
    height = grid_id['height']
    reach = grid_id['reach']
    # Vars we need to navigate
    idx = 0
    pos = width
    posp = 0
    # How big the grid is
    heav = height * width
    # Dab on the haters
    print("#" + width*'*')
    # Display loop
    for i in range(1, int(len(reach)/width)+1):
        print("*", end='')
        # We have to go through the goal step by step
        for j in range(posp, pos):
            if reach[idx] == '1':
                # Print but without a new line
                print('x', end='')
            else:
                # Print but without a new line again
                print('o', end='')
            idx = idx + 1
        pass
        print()
        posp = pos
        pos = pos + width
    return
    pass


# This function will be used to display the current grid, but finished.
def fdisplaysolved(grid_id):
    # Displaying the grid's width
    # Go through the width; display what you gotta display: go to next line.
    # Getting the vars we need from the initialized grid
    width = grid_id['width']
    height = grid_id['height']
    goal = grid_id['goal']
    # Vars we need to navigate
    idx = 0
    pos = width
    posp = 0
    # How big the grid is
    heav = height * width
    # Dab on the haters
    print("#" + width*'*')
    # Display loop
    for i in range(1, int(len(goal)/width)+1):
        print("*", end='')
        # We have to go through the goal step by step
        for j in range(posp, pos):
            if goal[idx] == '1':
                # Print but without a new line
                print('x', end='')
            else:
                # Print but without a new line again
                print('o', end='')
            idx = idx + 1
        pass
        print()
        posp = pos
        pos = pos + width
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


# Where d stands for distinct.
# Here we'll "split" the reach in lines and columns.
def flignify(linesd, columnsd):
    return
    pass


# Can't .strip a dict, so I'm doing it here
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
            fdisplaysolved(grid_id)
            pass
    else:
        print('Wrong option ! Please use -g to specify the grid you want to open.')
        pass


# Now we run it !
if __name__ == '__main__':
    main(sys.argv)
