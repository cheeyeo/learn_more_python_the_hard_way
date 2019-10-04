# Sort list of numbers by bubble sort
def bubble_sort(numbers):
	n = len(numbers)-1

	while True:
		swapped = True

		for i in range(n):
			if numbers[i] > numbers[i+1]:
				temp = numbers[i]
				numbers[i] = numbers[i+1]
				numbers[i+1] = temp
				swapped = False
		if swapped:
			break

# Sorts a list of objects
def merge_sort(numbers):
	if len(numbers) <= 1:
		return numbers

	left = list()
	right = list()
	split = len(numbers) / 2

	while len(numbers) > 0:
		if split > 0:
			left.append(numbers.pop(0))
			split -= 1
		else:
			right.append(numbers.pop(0))

	left = merge_sort(left)
	right = merge_sort(right)

	return plain_merge(left, right)


def merge(left, right):
	result = list()

	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))

	while len(left) > 0:
		result.append(left.pop(0))

	while len(right) > 0:
		result.append(right.pop(0))

	return result

def quick_sort(numbers, low, high):
	if low < high:
		# pi is partition index
		pi = partition(numbers, low, high)

		quick_sort(numbers, low, pi - 1)
		quick_sort(numbers, pi + 1, high)

	return numbers

def partition(arr, low, high):
	pivot = arr[high]

	i = low - 1

	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1

if __name__ == '__main__':
	arr = [10, 80, 30,90, 40, 50, 70]
	print('BEFORE QUICK SORT: ', arr)
	n = len(arr)
	print('AFTER QUICK SORT: ', quick_sort(arr, 0, n-1))