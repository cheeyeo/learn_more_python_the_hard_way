import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--flaga", action="store_true", help="Turns flag a on")
ap.add_argument("-b", "--flagb", action="store_true", help="Turns flag b on")
ap.add_argument("-c", "--flagc", action="store_true", help="Turns flag c on")
ap.add_argument("-d", "--var1", help="Sets variable 1")
ap.add_argument("-e", "--var2", help="Sets variable 2")
ap.add_argument("-f", "--var3", help="Sets variable 3")
# adds positional argument
ap.add_argument("wildcard", nargs="+")

args = vars(ap.parse_args())
print(args)

var1 = None
var2 = None
var3 = None

if args["flaga"]:
	print("Flag a is switched on!")
if args["flagb"]:
	print("Flag b is switched on!")
if args["flagc"]:
	print("Flag c is switched on!")

if args["var1"]:
	var1 = args["var1"]
if args["var2"]:
	var2 = args["var2"]
if args["var3"]:
	var3 = args["var3"]

print("Var1: {}\nVar2: {}\nVar3: {}\n".format(var1, var2, var3))

print("Wildcard values: {}".format(args["wildcard"]))