import argparse
import pathlib
import os
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument("directory", type=str, help="Directory to search in")
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("-n", "--name", type=str, help="Name of files. Please quote wildcards else it gets expanded in the shell...")
group.add_argument("-t", "--type", type=str, help="Type of files")
ap.add_argument("-a", "--action", type=str, help="Action to take")

args = vars(ap.parse_args())

# Store found entries in list if action specified
items = list()

if args["name"] != None:
	files = pathlib.Path(args["directory"]).rglob(args["name"])
	for f in files:
		path = os.path.abspath(f)
		if args["action"] != None:
			items.append(path)
		else:
			print(path)
elif args["type"] != None:
	if args["type"] not in ["d", "f"]:
		print("Unknown type: {}".format(args["type"]))
		exit(1)
	files = pathlib.Path(args["directory"]).rglob("*")
	for f in files:
		path = os.path.abspath(f)
		if args["type"] == "d" and f.is_dir():
			if args["action"] != None:
				items.append(path)
			else:
				print(path)
		if args["type"] == "f" and f.is_file():
			if args["action"] != None:
				items.append(path)
			else:
				print(path)

if len(items) > 0 and args["action"] != None:
	cmd, params = args["action"].split(" ")
	for item in items:
		process = subprocess.run([cmd, params, item], check=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(process.stdout)
