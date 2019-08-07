import argparse

ap = argparse.ArgumentParser(description="Implement the Linux cat command in python. Reads/concatenate files passed to it and prints it to stdout.")
ap.add_argument("files", metavar='F', type=str, nargs="+")

args = vars(ap.parse_args())

files = args["files"]

for file in files:
	with open(file, 'r') as f:
		print(f.read())
