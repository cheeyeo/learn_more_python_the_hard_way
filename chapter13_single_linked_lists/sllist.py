class SingleLinkedListNode(object):
	def __init__(self, value, nxt):
		self.value = value
		self.nxt = nxt

	# Prints debugging output when repr() called on the node object
	def __repr__(self):
		nval = self.nxt and self.nxt.value or None
		return "{}:{}".format(self.value, repr(nval))


class SingleLinkedList(object):
	def __init__(self):
		self.begin = None
		self.end = None

	def push(self, obj):
		"""Appends new value to end of list."""
		node = SingleLinkedListNode(obj, None)
		if self.begin == None:
			self.begin = node
			self.end = self.begin
		else:
			self.end.nxt = node
			self.end = node
			assert self.begin != self.end

		assert self.end.nxt == None

	def pop(self):
		"""Removes last item and returns it."""
		if self.end == None:
			return None

		# case for only 1 node
		if self.begin == self.end:
			popped = self.end
			self.begin = None
			self.end = None
			return popped.value
		else:
			popped = self.end
			node = self.begin
			# Below takes you up to second last node, before the last node to be removed
			while node.nxt != self.end:
				node = node.nxt
			# Check that the node is not the last node
			assert self.end != node
			self.end = node
			node.nxt = None
			return popped.value


	def shift(self, obj):
		"""Append to beginning of list"""
		node = SingleLinkedListNode(obj, self.begin)
		if self.count() == 0:
			self.end = node
		self.begin = node


	def unshift(self):
		"""Removes first item and returns it."""
		if self.begin == None:
			return None

		if self.begin == self.end:
			popped = self.begin
			self.begin = None
			self.end = None
			return popped.value
		else:
			popped = self.begin
			node = popped.nxt
			self.begin = node
			return popped.value


	def remove(self, obj):
		"""Finds matching item and remove from list. Returns index of item"""
		if not self.begin:
			return None

		node = self.begin
		index = 0
		while node.value != obj:
			if node == self.end:
				return None
			node = node.nxt
			index += 1

		if index == 0:
			self.unshift()
			return 0

		if index == self.count() - 1:
			self.pop()
			return index
		else:
			prevNode = self.begin
			while prevNode.nxt != node:
				prevNode = prevNode.nxt
			prevNode.nxt = node.nxt
			return index


	def first(self):
		"""Returns a reference to first item, does not remove it."""
		if not self.begin:
			return None
		else:
			return self.begin.value

	def last(self):
		"""Returns a reference to last item, does not remove it."""
		if not self.end:
			return None
		else:
			return self.end.value

	def count(self):
		"""Counts number of elements in list."""
		count = 0
		node = self.begin
		while node:
			count += 1
			node = node.nxt
		return count

	def get(self, index):
		"""Get value at index."""
		if not self.begin:
			return None

		if index > self.count() - 1:
			return None

		node = self.begin
		counter = 0
		while counter < index:
			node = node.nxt
			counter += 1
		return node.value

	def dump(self, mark):
		"""Debugging function that dumps contents of a list."""
		print(mark)

		if not self.begin:
			print("Empty")
		else:
			node = self.begin
			print(node)
			while node != self.end:
				node = node.next
				print(node)