'''
Reads a tree bank of binary parse trees and finds a 
list of all productions along with their probabilities

Author: Ali Ahmed
'''


from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from tree import Tree
from collections import defaultdict
import sys
import six

bin_tree = sys.argv[1]
grammar = sys.argv[2]
infile = open(bin_tree,'r')
outfile = open(grammar,'w')
freqs = defaultdict(int)
condCounts = defaultdict(int)

for line in infile:
    line = line.strip()

    t = Tree.parse(line)
    prods = t.getProductions()

    for (x,y) in prods:
        freqs[(x,y)] += 1
        condCounts[x] += 1

for (x,y), freq in six.iteritems(freqs):
    p = freq / condCounts[x]
    outfile.write("%s -> %s # %.4f" % (x,y,p))
    outfile.write('\n')

