# Python BASIC Tools


baslines = []

# Open File and Print Contents
with open('/workspaces/python/pyBASICTools/CWSTRAT.BAS', 'rt') as basfile:
    for basline in basfile:
        baslines.append(basline)
    
    print(baslines)