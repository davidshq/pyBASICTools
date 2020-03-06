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
    charindex = 0 # current index in string
    charprev = 0 # previous index in string
    currentstr = baslist[index] # the string we are searching
    searchstr = "SUB animate"
    while charindex < len(currentstr): # While there are still more items in the list
        foundstr = currentstr.find(searchstr, charindex) # Find our substring beginning at lineindex.
        if foundstr == -1: # If it doesn't exist
            break # Go to next iteration of loop
        foundchar = foundstr - charprev
        print_result = "Found at " + str(foundchar) + " character on line " + str(index + 1) + "."
        print(print_result) # Print location of substring
        charprev = foundstr + len(searchstr) # Add length of substring to the location substring begins at  
        charindex += len(searchstr)  # Set lineindex to location substring ends at
    prev = index
    index = index + 1