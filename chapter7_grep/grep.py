import argparse
import re
import pathlib
import os

ap = argparse.ArgumentParser()
ap.add_argument("pattern", type=str, help="Pattern to look for.")
ap.add_argument("files", type=str, help="Files to look for pattern. Can be regular filename, directory, or wildcard. Need quotes to escape wildcard.")
args = vars(ap.parse_args())

search_pattern = re.compile(args["pattern"])

path, filenames = os.path.split(args["files"])
files = pathlib.Path(path).rglob(filenames)
matches = []
for file in files:
	path = os.path.abspath(file)

	if file.is_dir():
		files = pathlib.Path(path).rglob("*")
		for f in files:
			path = os.path.abspath(f)
			with open(path, 'r') as f:
				content = f.readlines()
				matched_content = [l for l in content if re.search(search_pattern, l)]
				for c in matched_content:
					idx = content.index(c) + 1
					matches.append("{}:{:d}: {}".format(path, idx, c))
	elif file.is_file():
		with open(path, 'r') as f:
			content = f.readlines()
			matched_content = [l for l in content if re.search(search_pattern, l)]
			for c in matched_content:
				idx = content.index(c) + 1
				matches.append("{}:{:d}: {}".format(path, idx, c))

for m in matches:
	print(m)