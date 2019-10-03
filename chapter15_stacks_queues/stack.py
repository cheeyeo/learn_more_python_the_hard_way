class StackNode(object):
	def __init__(self, value, next):
		self.value = value
		self.next = next

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"


class Stack(object):
	def __init__(self):
		self.top = None

	def push(self, obj):
		"""
		Pushes a new value to top of stack.
		"""
		new_node = StackNode(obj, None)
		if self.top == None:
			self.top = new_node
		else:
			prev_node = self.top
			new_node.next = prev_node
			self.top = new_node

	def pop(self):
		"""
		Pops value from top of stack
		"""
		if self.top == None:
			return None

		node = self.top
		next_node = node.next
		node.next = None
		self.top = next_node
		return node.value


	def first(self):
		"""
		Returns reference to first item, does not remove it
		"""
		if self.top == None:
			return None

		return self.top.value


	def count(self):
		"""
		Returns count of items in stack
		"""
		if self.top == None:
			return 0

		count = 0
		top = self.top
		while top:
			count += 1
			top = top.next
		return count

	def dump(self, mark="----"):
		"""
		Debugging function that dumps contents of stack
		"""
		print(mark)
		node = self.top
		print(node)
		while node:
			node = node.next
			print(node)
		print(mark)
		print()