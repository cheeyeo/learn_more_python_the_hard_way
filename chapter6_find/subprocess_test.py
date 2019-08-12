import subprocess

file = "./find.py"

action = "ls -lt"
# action = "cat {} \;"
cmd, *params = action.split(" ")
print(cmd)
print(params)

subprocess_args = list()
subprocess_args.append(cmd)

invalid_params = ['{}', '\;']
if len(params) > 0:
	subprocess_args.extend([param for param in params if param not in invalid_params])

subprocess_args.append(file)
print(subprocess_args)

process = subprocess.run(subprocess_args, check=True, stdout=subprocess.PIPE, universal_newlines=True)

print(process.stdout)