import sys
import re
import string
from utils import read_lines

expression = sys.argv[1]
targets = sys.argv[2:]

# Note: Actual sed usage also takes input from stdin i.e. try to read from sys.stdin

# Check format of expression
# If s/*** => search and replace
search_replace = re.compile(r's\/.*\/.*\/g', re.I+re.S)
res = search_replace.match(expression)
if res != None:
	expr = res.group()
	expr = expr.split('/')
	replacement = expr[1:3]
else:
	print('Expression is not defined. Only supports s/.*/g for now.')
	exit(1)

for target in targets:
	lines = read_lines(target)
	for line in lines:
		# replace string with expression
		new_line = re.sub(replacement[0], replacement[1], line)
		print(new_line)