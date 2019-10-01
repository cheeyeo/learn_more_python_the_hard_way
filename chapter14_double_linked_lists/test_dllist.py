from dllist import *

def test_push():
	dll = DoubleLinkedList()
	dll.push(1)
	assert dll.begin == dll.end
	assert dll.begin.prev == None
	assert dll.end.next == None
	assert dll.count() == 1

	dll.push(2)
	assert dll.begin != dll.end
	assert dll.end.prev == dll.begin
	assert dll.begin.prev == None
	assert dll.end.next == None
	assert dll.count() == 2

def test_count():
	dll = DoubleLinkedList()
	assert dll.count() == 0

	dll.push(1)
	dll.push(2)
	assert dll.count() == 2

def test_pop():
	dll = DoubleLinkedList()
	assert dll.pop() == None
	
	dll.push(1)
	assert dll.count() == 1

	res = dll.pop()
	assert res == 1
	assert dll.count() == 0
	assert dll.begin == None
	assert dll.end == None

	# Test case for more than 1 element
	dll.push(1)
	dll.push(2)
	assert dll.count() == 2

	res = dll.pop()
	assert res == 2
	assert dll.count() == 1
	assert dll.begin == dll.end

	res = dll.pop()
	assert res == 1
	assert dll.count() == 0

def test_shift():
	dll = DoubleLinkedList()
	dll.shift(1)
	assert dll.count() == 1
	assert dll.begin == dll.end

	dll.shift(2)
	assert dll.count() == 2
	assert dll.begin != dll.end
	assert dll.begin.prev == None
	assert dll.end.next == None
	assert dll.begin.value == 2
	assert dll.end.value == 1

def test_unshift():
	dll = DoubleLinkedList()

	assert dll.unshift() == None

	# Test case for 1 element
	dll.push(1)
	assert dll.unshift() == 1
	assert dll.begin == dll.end

	# Test case for > 1 element
	dll.push(1)
	dll.push(2)
	assert dll.unshift() == 1
	assert dll.begin == dll.end
	assert dll.begin.value == dll.end.value
	assert dll.count() == 1

def test_remove():
	colors = DoubleLinkedList()
	colors.push("Cobalt")
	colors.push("Zinc White")
	colors.push("Nickle Yellow")
	colors.push("Perinone")

	# colors.dump("before removing cobalt")
	assert colors.remove("Cobalt") == 0

	# colors.dump("before removing perinone")
	assert colors.remove("Perinone") == 2

	# colors.dump("after removing perinone")

	assert colors.remove("Nickle Yellow") == 1
	assert colors.remove("Zinc White") == 0


def test_first():
	dll = DoubleLinkedList()
	dll.push(1)
	assert dll.first() == 1
	dll.push(2)
	assert dll.first() == 1
	dll.shift(-100)
	assert dll.first() == -100

def test_last():
	dll = DoubleLinkedList()
	dll.push(1)
	assert dll.last() == 1
	dll.push(2)
	assert dll.last() == 2
	dll.shift(-100)
	assert dll.last() == 2

def test_get():
	colors = DoubleLinkedList()
	colors.push("Vermillion")
	assert colors.get(0) == "Vermillion"

	colors.push("Sap Green")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"

	colors.push("Cadmium Yellow Light")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == "Cadmium Yellow Light"
	assert colors.pop() == "Cadmium Yellow Light"

	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == None
	colors.pop()
	assert colors.get(0) == "Vermillion"
	colors.pop()
	assert colors.get(0) == None

if __name__ == '__main__':
	test_push()
	test_count()
	test_pop()
	test_shift()
	test_unshift()
	test_remove()
	test_first()
	test_last()
	test_get()