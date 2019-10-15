class DoubleLinkedListNode(object):
	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):
	def __init__(self):
		self.begin = None
		self.end = None

	def push(self, obj):
		"""
		Appends new node to end of list
		"""
		new_node = DoubleLinkedListNode(obj, None, self.end)
		if self.begin == None:
			self.begin = self.end = new_node
			self.begin.prev = None
			self.end.next = None
		else:
			self.end.next = new_node
			self.end = new_node

	def pop(self):
		"""
		Remove last node from list and return it
		"""
		if self.begin == None:
			return None

		# Handle case of 1 element in list
		if self.count() == 1:
			popped = self.end
			self.begin = self.end = None
			return popped.value
		else:
			popped = self.end
			prev_node = popped.prev
			assert self.end != prev_node
			self.end = prev_node
			prev_node.next = None
			return popped.value

	def shift(self, obj):
		"""
		Appends to front of list
		"""
		new_node = DoubleLinkedListNode(obj, None, None)

		if self.begin == None:
			self.begin = self.end = new_node
			self.begin.prev = None
			self.end.next = None
		else:
			prev_node = self.begin
			self.begin = new_node
			new_node.next = prev_node
			new_node.prev = None
			prev_node.prev = new_node

	def unshift(self):
		"""
		Removes element from front of list and return its value
		"""
		if self.begin == None:
			return None

		if self.count() == 1:
			popped = self.begin
			self.begin = self.end = None
			return popped.value
		else:
			popped = self.begin
			next_node = popped.next
			popped.next = None
			next_node.prev = None
			self.begin = next_node
			return popped.value

	def detach_node(self, node):
		"""
		Take a node and detach it from list,
		whether it's at the front, middle, or end...
		"""
		if node == self.begin == self.end:
			self.begin = None
			self.end = None
		elif node == self.begin:
			node.next.prev = None
			self.begin = node.next
		elif node == self.end:
			node.prev.next = None
			self.end = node.prev
		else:
			node.next.prev = node.prev
			node.prev.next = node.next

	def remove(self, obj):
		"""
		Find matching item and remove from the list.
		Returns index of obj
		"""

		if self.begin == None:
			return None

		node = self.begin
		index = 0
		while node.value != obj:
			if node == self.end:
				return None
			node = node.next
			index += 1
		self.detach_node(node)
		return index


	def first(self):
		"""
		Returns reference to first item, does not remove
		"""
		if self.begin == None:
			return None
		else:
			return self.begin.value

	def last(self):
		"""
		Returns reference to last item, does not remove
		"""

		if self.end == None:
			return None
		else:
			return self.end.value

	def get(self, index):
		"""
		Get the value at index
		"""
		if self.begin == None:
			return None

		if index > self.count() - 1:
			return None

		node = self.begin
		counter = 0
		while counter < index:
			node = node.next
			counter += 1
		return node.value

	def count(self):
		"""
		Returns number of elements in list
		"""
		if self.begin == None:
			return 0

		count = 0
		node = self.begin
		while node:
			count += 1
			node = node.next
		return count

	def dump(self, mark):
		if self.begin == None:
			print(mark)
			print("empty")
		else:
			print(mark)
			node = self.begin
			print(node)
			while node != self.end:
				node = node.next
				print(node)