import argparse
import sys
from utils import has_input
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--count", action="store_true", help="Show prefix of occurences.")

args = vars(ap.parse_args())

# Use dict to store each item...
occurences = dict()

if has_input(sys.stdin):
	infile = sys.stdin
else:
	print('Need standard input data to work.')
	exit(1)

data = infile.readlines()

for d in data:
	d = d.strip()
	count = occurences.get(d, 0)
	count += 1
	occurences[d] = count

for k, v in occurences.items():
	line = ""
	if args["count"]:
		line += "{:7d} ".format(v)
	line += k
	print(line)