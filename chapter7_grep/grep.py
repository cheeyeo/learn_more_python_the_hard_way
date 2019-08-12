import argparse
import re
import pathlib
import os
from utils import read_match_content

ap = argparse.ArgumentParser()
ap.add_argument("pattern", type=str, help="Pattern to look for.")
ap.add_argument("files", type=str, help="Files to look for pattern. Can be regular filename, directory, or wildcard. Need quotes to escape wildcard. e.g. 'mydir/*.py' or '*.py'")
args = vars(ap.parse_args())

search_pattern = re.compile(args["pattern"])

path, filenames = os.path.split(args["files"])
files = pathlib.Path(path).rglob(filenames)

# To solve the issue of sub-dirs, we split the dirs and files into 2 distinct lists and iterate over the dirs list individually
dirs = list()
single_files = list()

for f in files:
	if f.is_dir():
		dirs.append(f)
	if f.is_file():
		single_files.append(f)

matches = list()

for dir in dirs:
	inner_files = pathlib.Path(dir).rglob("*")
	for f in inner_files:
		if f.is_file():
			path = os.path.abspath(f)
			matched_content = read_match_content(path, search_pattern)
			matches.extend(matched_content)

for file in single_files:
	path = os.path.abspath(file)
	matched_content = read_match_content(path, search_pattern)
	matches.extend(matched_content)

for m in matches:
	print(m)