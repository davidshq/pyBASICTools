# Python BASIC Tools

# Imports
import os

# Empty List to Contain Lines of BASIC Code
baslist = []

# Get the current working directory
cwd = os.getcwd()

# Open our code file
with open(f'{cwd}/pyBASICTools/CWSTRAT.BAS', 'rt') as basfile:
    # Copy each line into our list (baslist)
    for line in basfile:
        baslist.append(line)

# Search for instances of SUB
index = 0 # current index in list
prev = 0 # previous index in list


while index < len(baslist):
    charindex = 0 # current index in string
    charprev = 0 # previous index in string
    currentstr = baslist[index] # the string we are searching
    searchstr = "SUB animate"
    while charindex < len(currentstr): # While there are still more characters in the string
        foundstr = currentstr.find(searchstr, charindex) # Find our substring beginning at charindex.
        if foundstr == -1: # If searchstr doesn't exist in currentstr
            break # Go to next iteration of loop
        foundchar = foundstr - charprev
        print_result = "Found at " + str(foundchar) + " character on line " + str(index + 1) + "."
        print(print_result) # Print location of substring
        charprev = foundstr + len(searchstr) # Add length of substring to the location substring begins at  
        charindex += len(searchstr)  # Set charindex to location substring ends at
    prev = index
    index = index + 1