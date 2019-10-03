class QueueNode(object):
	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class Queue(object):
	def __init__(self):
		self.begin = None
		self.end = None

	def shift(self, obj):
		"""
		Adds item to end of queue
		"""
		new_node = QueueNode(obj, None, None)
		if self.begin == None:
			self.begin = self.end = new_node
			self.begin.prev = None
			self.end.next = None
		else:
			prev_node = self.end
			prev_node.next = new_node
			self.end = new_node


	def unshift(self):
		"""
		Removes item from front of queue
		"""
		if self.begin == None:
			return None
		if self.count() == 1:
			node = self.begin
			self.begin = self.end = None
			return node.value
		else:
			node = self.begin
			prev_node = node.next
			prev_node.prev = None
			self.begin = prev_node
			return node.value

	def count(self):
		if self.begin == None:
			return 0

		count = 0
		node = self.begin
		while node:
			count += 1
			node = node.next
		return count

	def dump(self, mark='------'):
		print(mark)
		node = self.begin
		print(node)
		while node:
			node = node.next
			print(node)
		print(mark)