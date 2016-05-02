import sys
import os

x = 0
for files in os.walk('.'):
   for fname in files:
       if fname.endswith('.txt') :
           x = x + 1
print ("number of text files: %s", count)
