import sys

f = open(sys.argv[1], 'r')
count = 0

# Counting each line as it is read
for line in f:
    count += 1

print "Number of lines: ",count
