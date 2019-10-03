import unittest
from unittest import TestCase
from stack import *

class TestStack(TestCase):
	def test_push(self):
		stack = Stack()
		stack.push(1)
		self.assertEqual(stack.count(), 1)
		self.assertEqual(stack.top.value, 1)

		stack.push(2)
		self.assertEqual(stack.count(), 2)
		self.assertEqual(stack.top.value, 2)
		self.assertEqual(stack.top.next.value, 1)
		self.assertIsNone(stack.top.next.next)

	def test_pop(self):
		stack = Stack()
		self.assertIsNone(stack.pop())

		stack.push(1)
		self.assertEqual(stack.pop(), 1)
		self.assertIsNone(stack.top)

		stack.push(1)
		stack.push(2)
		stack.push(3)
		stack.dump(mark='---------')
		self.assertEqual(stack.pop(), 3)
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.pop(), 1)
		self.assertIsNone(stack.pop())

	def test_first(self):
		stack = Stack()
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.first(), 2)

		stack.pop()
		self.assertEqual(stack.first(), 1)

if __name__ == '__main__':
	unittest.main()