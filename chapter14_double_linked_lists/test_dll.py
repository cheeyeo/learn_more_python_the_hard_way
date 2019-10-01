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
	  dll = DoubleLinkedList()
	  self.assertIsNone(dll.pop())

	  dll.push(1)
	  self.assertEqual(dll.count(), 1)

	  self.assertEqual(dll.pop(), 1)
	  self.assertEqual(dll.count(), 0)
	  self.assertIsNone(dll.begin)
	  self.assertIsNone(dll.end)

	  # Test case for more than 1 element
	  dll.push(1)
	  dll.push(2)
	  self.assertEqual(dll.count(), 2)

	  self.assertEqual(dll.pop(), 2)
	  self.assertEqual(dll.count(), 1)
	  self.assertEqual(dll.begin, dll.end)

	  self.assertEqual(dll.pop(), 1)
	  self.assertEqual(dll.count(), 0)

	def test_shift(self):
		dll = DoubleLinkedList()
		dll.shift(1)
		self.assertEqual(dll.count(), 1)
		self.assertEqual(dll.begin, dll.end)

		dll.shift(2)
		self.assertEqual(dll.count(), 2)
		self.assertNotEqual(dll.begin, dll.end)
		self.assertEqual(dll.begin.value, 2)
		self.assertEqual(dll.end.value, 1)

	def test_unshift(self):
		dll = DoubleLinkedList()
		self.assertIsNone(dll.unshift())

		dll.push(1)
		self.assertEqual(dll.unshift(), 1)

		dll.push(1)
		dll.push(2)
		self.assertEqual(dll.unshift(), 1)
		self.assertEqual(dll.unshift(), 2)

	def test_count(self):
		dll = DoubleLinkedList()
		self.assertEqual(dll.count(), 0)

		dll.push(1)
		dll.push(2)
		self.assertEqual(dll.count(), 2)

	def test_remove(self):
		colors = DoubleLinkedList()
		colors.push("Cobalt")
		colors.push("Zinc White")
		colors.push("Nickle Yellow")
		colors.push("Perinone")

		# colors.dump("before removing cobalt")
		self.assertEqual(colors.remove("Cobalt"), 0)

		# colors.dump("before removing perinone")
		self.assertEqual(colors.remove("Perinone"), 2)

		# colors.dump("after removing perinone")

		self.assertEqual(colors.remove("Nickle Yellow"), 1)
		self.assertEqual(colors.remove("Zinc White"), 0)

	def test_first(self):
		dll = DoubleLinkedList()
		dll.push(1)
		self.assertEqual(dll.first(), 1)
		dll.push(2)
		self.assertEqual(dll.first(), 1)
		dll.shift(-100)
		self.assertEqual(dll.first(), -100)

	def test_last(self):
		dll = DoubleLinkedList()
		dll.push(1)
		self.assertEqual(dll.last(), 1)
		dll.push(2)
		self.assertEqual(dll.last(), 2)
		dll.shift(-100)
		self.assertEqual(dll.last(), 2)

	def test_get(self):
		colors = DoubleLinkedList()
		colors.push("Vermillion")
		self.assertEqual(colors.get(0), "Vermillion")

		colors.push("Sap Green")
		self.assertEqual(colors.get(0), "Vermillion")
		self.assertEqual(colors.get(1), "Sap Green")

		colors.push("Cadmium Yellow Light")
		self.assertEqual(colors.get(0), "Vermillion")
		self.assertEqual(colors.get(1), "Sap Green")
		self.assertEqual(colors.get(2), "Cadmium Yellow Light")
		self.assertEqual(colors.pop(), "Cadmium Yellow Light")

		self.assertEqual(colors.get(0), "Vermillion")
		self.assertEqual(colors.get(1), "Sap Green")
		self.assertEqual(colors.get(2), None)
		colors.pop()
		self.assertEqual(colors.get(0), "Vermillion")
		colors.pop()
		self.assertEqual(colors.get(0), None)


if __name__ == '__main__':
	unittest.main()