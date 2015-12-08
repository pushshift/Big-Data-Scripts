#!/usr/bin/env python

import os.path
import sys
import bz2
import gzip
import zipfile 
import json

def file_type(filename):
    magic_dict = {
    	"\x1f\x8b\x08": "gz",
    	"\x42\x5a\x68": "bz2",
    	"\x50\x4b\x03\x04": "zip"
    }
    max_len = max(len(x) for x in magic_dict)
    with open(filename) as f:
        file_start = f.read(max_len)
    for magic, filetype in magic_dict.items():
        if file_start.startswith(magic):
            return filetype
    return "unknown"

try:
  filename = sys.argv[1]
except IndexError:
  sys.exit("Please specify a filename (i.e. sample.bz2)")

if not os.path.isfile(filename):
  sys.exit("File doesn't exist")

# What type of compression (or default to standard open)
filetype = file_type(filename)
if filetype == "bz2":
  uncompress = bz2.BZ2File
elif filetype == "gz":
  uncompress = gzip.open
elif filetype == "zip":
  sys.exit("zip file support is not implemented yet.")
else:
  uncompress = open

subreddits = {}
with uncompress(sys.argv[1], "r") as file:
  for line in file:
    j = json.loads(line)
    if not j['subreddit'] in subreddits:
      subreddits[j['subreddit']] = 1
    else:
      subreddits[j['subreddit']] += 1

# Create tuples from the dictionary and sort by first element
subreddits_view = [ (v,k) for k,v in subreddits.iteritems() ]
subreddits_view.sort(reverse=True)
for v,k in subreddits_view:
    print "%s: %d" % (k,v)  


