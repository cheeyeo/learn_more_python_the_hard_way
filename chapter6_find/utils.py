def process_exec(exec_args):
	cmd, *params = exec_args.split(" ")
	cmd_args = list()
	cmd_args.append(cmd)
	invalid_params = ['{}', '\;']

	if len(params) > 0:
		cmd_args.extend([param for param in params if param not in invalid_params])

	return cmd_args