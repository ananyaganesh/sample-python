import string
import sys

f = open(sys.argv[1], 'r')
wdict = {}

# Storing each word as key and count as value
# If key isn't found, value is returned as 0
# Value is incremented by 1 for each occurrence
for line in f:
    for word in line.split():
        word = word.translate(None,'?!.').lower()
        wdict[word] = wdict.get(word, 0) + 1

for word, count in wdict.items():
    print word, count

print "The unique words are: "

for word, count in wdict.items():
    if count == 1:
        print word
        
        
        
