# Example of testing DoubleLinkedList using built-in unittest module

import unittest
from unittest import TestCase
from dllist import *

class TestDoubleLinkedList(TestCase):
	def test_push(self):
		dll = DoubleLinkedList()
		dll.push(1)
		self.assertEqual(dll.begin, dll.end, 'Begin should equal end')
		self.assertIsNone(dll.begin.prev, "Begin's prev should be none")
		self.assertIsNone(dll.end.next)
		self.assertEqual(dll.count(), 1)

		dll.push(2)
		self.assertNotEqual(dll.begin, dll.end, 'Begin should not equal end')
		self.assertEqual(dll.end.prev, dll.begin)
		self.assertIsNone(dll.begin.prev)
		self.assertIsNone(dll.end.next)
		self.assertEqual(dll.count(), 2)

	def test_pop(self):
		pass

	def test_shift(self):
		pass

	def test_unshift(self):
		pass

	def test_count(self):
		pass

	def test_detach_node(self):
		pass

if __name__ == '__main__':
	unittest.main()