#!/usr/bin/python

import sys,pprint

sys.path.append('../gexf')
from wrapper_gexf import WrapperGexf

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def usage():
    print("./visualizer -i <ID> -s <Search_String> -f <file to update>")

def getID(search_string):
    return 0

wrapper = WrapperGexf()

myargs = getopts(sys.argv)

if '-i' in myargs: 
    paper_id = myargs['-i']
    wrapper.setID(paper_id)
elif '-s' in myargs:
    search_string = myargs['-s']
    print "Searching for:", myargs['-s']
    paper_id = getID(search_string)
    wrapper.setID(paper_id)
else:
    print "Paper ID or a Search String must be provided"
    usage()
    sys.exit()
   
if '-f' in myargs: 
    old_file = myargs['-f']
    print "Updating File: ", myargs['-f']

wrapper.populate()
