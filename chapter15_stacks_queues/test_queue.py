import unittest
from unittest import TestCase
from queue import *


class TestQueue(TestCase):
	def test_shift(self):
		queue = Queue()
		queue.shift(1)
		self.assertEqual(queue.end.value, 1)
		self.assertIsNone(queue.end.next)
		self.assertIsNone(queue.end.prev)

		queue.shift(2)
		queue.dump()
		self.assertEqual(queue.end.value, 2)
		self.assertEqual(queue.begin.value, 1)

	def test_unshift(self):
		queue = Queue()
		self.assertIsNone(queue.unshift())

		queue.shift(1)
		self.assertEqual(queue.unshift(), 1)
		self.assertIsNone(queue.begin)
		self.assertIsNone(queue.end)

		queue.shift(1)
		queue.shift(2)
		self.assertEqual(queue.unshift(), 1)
		self.assertEqual(queue.unshift(), 2)
		self.assertIsNone(queue.unshift())

if __name__ == '__main__':
	unittest.main()