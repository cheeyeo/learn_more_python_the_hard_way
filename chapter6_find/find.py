import argparse
import pathlib
import os

ap = argparse.ArgumentParser()
ap.add_argument("directory", type=str, help="Directory to search in")

group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("-n", "--name", type=str, help="Name of files. Please quote wildcards else it gets expanded in the shell...")
group.add_argument("-t", "--type", type=str, help="Type of files")

# ap.add_argument("action", type=str, help="Action to take")
args = vars(ap.parse_args())

if args["name"] != None:
	files = pathlib.Path(args["directory"]).rglob(args["name"])
	for f in files:
		print(os.path.abspath(f))
elif args["type"] != None:
	if args["type"] not in ["d", "f"]:
		print("Unknown type: {}".format(args["type"]))
		exit(1)
	files = pathlib.Path(args["directory"]).rglob("*")
	for f in files:
		if args["type"] == "d" and f.is_dir():
			print(os.path.abspath(f))
		if args["type"] == "f" and f.is_file():
			print(os.path.abspath(f))