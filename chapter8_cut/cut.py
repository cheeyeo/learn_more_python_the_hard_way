import argparse
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument("command", type=str, help="Command to generate input for processing")
ap.add_argument("-d", "--delmiter", type=str, help="Delimiter character")
ap.add_argument("-f", "--fields", type=str, help="Number of fields to retrive data on. e.g. 1-5")

args = vars(ap.parse_args())

cmd, *params = args["command"].split()
cmd_args = list()
cmd_args.append(cmd)
if len(params) > 0:
	cmd_args.extend([param for param in params])

try:
	output = list()
	process = subprocess.run(cmd_args, check=True, stdout=subprocess.PIPE, universal_newlines=True)
	input = process.stdout
	input = input.split("\n")
	for i in input:
		i = i.split(args["delmiter"])
		start, end = args["fields"].split("-")
		res = i[int(start)-1:int(end)]
		res = ' '.join(res)
		output.append(res)
	output = [o for o in output if len(o) > 1]
	for o in output:
		print(o)
except FileNotFoundError as err:
	print("Command is invalid.")
	print(err)
