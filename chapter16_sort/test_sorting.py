import unittest
from unittest import TestCase
from sorting import *
from dll import *
from random import randint

class TestSorting(TestCase):
	# Helper functions
	def generate_rand_nums(self, count):
		nums = list()
		for i in range(count, 0, -1):
			nums.append(randint(0, 100))
		return nums

	def is_sorted(self, nums):
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				return False
		return True

	def is_sorted_list(self, nums):
		node = nums.begin

		if node.value > node.next.value:
			return False
		else:
			node = node.next

		return True

	def test_bubble_sort(self):
		dll = DoubleLinkedList()
		dll.push(3)
		dll.push(1)
		dll.push(2)
		# dll.dump('---Before Sort----')

		bubble_sort(dll)
		# dll.dump('--After Sort----')
		self.assertTrue(self.is_sorted_list(dll))


	def test_merge_sort(self):
		dll = DoubleLinkedList()
		dll.push(3)
		dll.push(1)
		dll.push(2)
		dll.push(-1)

		# dll.dump('--Before Sort--')

		dll = merge_sort(dll)

		# dll.dump('--After Sort--')
		self.assertTrue(self.is_sorted_list(dll))

	def test_quick_sort(self):
		dll = DoubleLinkedList()
		dll.push(3)
		dll.push(1)
		dll.push(100)
		dll.push(-1)
		# dll.dump('--BEFORE SORT--')

		quick_sort(dll, 0, dll.count()-1)

		# dll.dump('--AFTER SORT--')


if __name__ == '__main__':
	unittest.main()