import subprocess

action = "ls -lha"
cmd, params = action.split(" ")
print(cmd)
print(params)
process = subprocess.run([cmd, params, "./"], check=True, stdout=subprocess.PIPE, universal_newlines=True)

print(process.stdout)