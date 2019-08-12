import re
import pathlib

def read_match_content(path, pattern):
	matches = list()
	with open(path, 'r', errors='ignore') as f:
		content = f.readlines()
		matched_content = [l for l in content if re.search(pattern, l)]
		for c in matched_content:
			idx = content.index(c) + 1
			matches.append("{}:{:d}: {}".format(path, idx, c))
	return matches