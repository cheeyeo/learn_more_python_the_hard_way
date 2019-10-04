from dll import *

# Sort double linked list by bubble sort
def bubble_sort(numbers):
	n = numbers.count()

	while True:
		swapped = True
		index = 1
		node = numbers.begin

		while index < n:
			if node.value > node.next.value:
				node.value, node.next.value = node.next.value, node.value
				swapped = False
			index += 1
			node = node.next

		n -= 1
		if swapped:
			break

# Sorts double linked list using merge sort
def merge_sort(dll):
	if dll.count() <= 1:
		return dll

	left = DoubleLinkedList()
	right = DoubleLinkedList()
	split = dll.count() // 2
	while dll.count() > 0:
		if split > 0:
			left.push(dll.unshift())
			split -= 1
		else:
			right.push(dll.unshift())

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	result = DoubleLinkedList()

	while left.count() > 0 and right.count() > 0:
		if left.begin.value <= right.begin.value:
			result.push(left.unshift())
		else:
			result.push(right.unshift())

	while left.count() > 0:
		result.push(left.unshift())

	while right.count() > 0:
		result.push(right.unshift())

	return result


def node_at(numbers, i):
	count = 0
	node = numbers.begin
	while node and count < i:
		node = node.next
		count += 1
	return node

def quick_sort(dll, low, high):
	if low < high:
		# pi is partition index
		pi = partition(dll, low, high)
		quick_sort(dll, low, pi - 1)
		quick_sort(dll, pi + 1, high)

def partition(dll, low, high):
	pivot = node_at(dll, high)

	i = low - 1

	for j in range(low, high):
		node_j = node_at(dll, j)
		if node_j.value < pivot.value:
			i += 1
			node_i = node_at(dll, i)
			node_i.value, node_j.value = node_j.value, node_i.value

	node_hi = node_at(dll, high)
	node_iplus  = node_at(dll, i+1)
	node_iplus.value, node_hi.value = node_hi.value, node_iplus.value

	return i + 1

if __name__ == '__main__':
	dll = DoubleLinkedList()
	dll.push(3)
	dll.push(1)
	dll.push(2)
	dll.push(-1)
	dll.dump('--BEFORE SORT--')

	quick_sort(dll, 0, dll.count()-1)

	dll.dump('--AFTER SORT--')
