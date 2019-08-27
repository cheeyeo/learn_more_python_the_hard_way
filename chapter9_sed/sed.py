import sys
import re
import string
from utils import read_lines, has_input
import io

expression = sys.argv[1]

if has_input(sys.stdin):
	targets = [sys.stdin]
else:
	targets = sys.argv[2:]

if len(targets) < 1:
	print('You need to pass in either a file or stdin.')
	exit(1)

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
	if isinstance(target, io.TextIOWrapper):
		lines = target.readlines()
	else:
		lines = read_lines(target)

	for line in lines:
		# replace string with expression
		new_line = re.sub(replacement[0], replacement[1], line)
		print(new_line)