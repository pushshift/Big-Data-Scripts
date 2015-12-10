#!/usr/bin/env python

# Sample of turning JSON to CSV using python
# Adjust fields as needed

import sys
import csv
import json

try:
  filename = sys.argv[1]
except IndexError:
  sys.exit("Please specify a plain text file (i.e. sample.txt)")

with open(filename, "r") as ins:
    output = csv.writer(sys.stdout)
    output.writerow(["subreddit","timestamp","score","author"])
    for line in ins:
        j = json.loads(line)
        output.writerow([ j['subreddit'],j['created_utc'],j['score'],j['author'] ])
