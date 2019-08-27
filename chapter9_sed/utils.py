import select

def read_lines(file):
	with open(file, 'r') as f:
		return f.readlines()

def has_input(*args):
	return select.select(args, [], [], 0.0)[0]