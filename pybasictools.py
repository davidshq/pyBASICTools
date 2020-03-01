# Python BASIC Tools

# Open File and Print Contents
with open('/workspaces/python/pyBASICTools/CWSTRAT.BAS', 'rt') as basfile:
    bascontents = basfile.read()
    print(bascontents)