# Python BASIC Tools

# Empty List to Contain Lines of BASIC Code
baslist = []

# Open Source File and Print Contents
with open('/workspaces/python/pyBASICTools/CWSTRAT.BAS', 'rt') as basfile:
    # Copy each line into baslist.
    for line in basfile:
        baslist.append(line)

# Search for instances of SUB
index = 0 # current index in list
prev = 0 # previous index in list


while index < len(baslist):
    lineindex = 0 # current index in string
    lineprev = 0 # previous index in string
    str = baslist[index] # first string to search from baslines
    substr = "SUB animate" # substring we are looking for
    while lineindex < len(str): # While there are still more items in the list
        found = str.find(substr, lineindex)
        if found == -1:
            lineindex = lineindex + 1
            break
        print(" " * (found - lineprev) + "e", end='') # Print location of substring
        lineprev = found + len(substr) 
        lineindex += len(substr)
    prev = index
    index = index + 1