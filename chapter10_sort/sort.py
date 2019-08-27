import sys
import argparse
import io
from utils import read_lines, has_stdin

ap = argparse.ArgumentParser()
# Add file input option here. Note that the positional argument is optional as it uses nargs=?
ap.add_argument("file", nargs="?", help="File to sort on.")
ap.add_argument("-r", "--reverse", action="store_true", help="Reverse sort.")
ap.add_argument("-f", "--ignore_case", action="store_true", help="Ignore case.")
args = vars(ap.parse_args())

if has_stdin(sys.stdin):
	target = sys.stdin
else:
	target = args["file"]

if target is None:
	print("You need to pass in either a file or stdin.")
	exit(1)

if isinstance(target, io.TextIOWrapper):
	lines = target.readlines()
else:
	lines = read_lines(target)

case_opts = None
if args["ignore_case"]:
	case_opts = str.casefold

sorted_lines = sorted(lines, key=str.casefold, reverse=args["reverse"])
for sl in sorted_lines:
	print(sl.strip())