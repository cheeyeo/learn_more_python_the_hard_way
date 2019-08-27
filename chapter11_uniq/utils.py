import select

def has_input(*args):
	return select.select(args, [], [], 0.0)[0]