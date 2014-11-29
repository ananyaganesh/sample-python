import sys

# Checking if there are arguments
if len(sys.argv) == 1:
    print "No parameters given"

# If there are, then print them
else:
    print "No. of parameters is: ",len(sys.argv)-1
    print sys.argv[1:]
