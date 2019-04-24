#!/usr/bin/env python

''' simplified PARSEVAL.
    author: David Chiang <chiang@isi.edu>, Liang Huang <lhuang@isi.edu>
'''

from __future__ import absolute_import
from __future__ import print_function
import sys
import six
from six.moves import zip
logs = sys.stderr

import itertools, collections
from tree import Tree

if __name__ == "__main__":
    try:
        _, parsefilename, goldfilename = sys.argv
    except:
        print("usage: evalb.py <parse-file> <gold-file>\n", file=logs)
        sys.exit(1)

    matchcount = parsecount = goldcount = 0

    for parseline, goldline in zip(open(parsefilename), open(goldfilename)):
        goldtree = Tree.parse(goldline)
        goldbrackets = goldtree.label_span_counts()    
        goldcount += len(goldbrackets)

        if parseline.strip() == "NONE": # parsing failure
            continue
        parsetree = Tree.parse(parseline)
        parsebrackets = parsetree.label_span_counts()
        parsecount += len(parsebrackets)

        for bracket, count in six.iteritems(parsebrackets):
            matchcount += min(count, goldbrackets[bracket])

    print("%s\t%d brackets" % (parsefilename, parsecount))
    print("%s\t%d brackets" % (goldfilename, goldcount))
    print("matching\t%d brackets" % matchcount)

