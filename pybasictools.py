# Python BASIC Tools


baslines = []

# Open File and Print Contents
with open('/workspaces/python/pyBASICTools/CWSTRAT.BAS', 'rt') as basfile:
    for basline in basfile:
        baslines.append(basline)
    for baselement in baslines:
        # When outputting, remove the newline character
        print(baselement, end='')