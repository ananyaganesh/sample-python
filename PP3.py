import sys

f = open(sys.argv[1], 'r')
count = 0

# Split the line on white space
# and increment count
for line in f:
    for word in line.split():
        count += 1

print "No. of words is: ", count
            
