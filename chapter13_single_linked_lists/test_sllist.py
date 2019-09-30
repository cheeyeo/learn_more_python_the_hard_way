from sllist import *

def test_push():
	colors = SingleLinkedList()
	colors.push("Blue")
	assert colors.count() == 1
	colors.push("Red")
	assert colors.count() == 2

def test_pop():
	colors = SingleLinkedList()
	colors.push("Red")
	colors.push("Blue")
	assert colors.pop() == "Blue"
	assert colors.pop() == "Red"
	assert colors.pop() == None

def test_shift():
	colors = SingleLinkedList()
	colors.shift("Blue")
	assert colors.count() == 1

	colors.shift("Red")
	assert colors.count() == 2

	assert colors.pop() == "Blue"
	assert colors.count() == 1

	assert colors.pop() == "Red"
	assert colors.count() == 0

def test_unshift():
	colors = SingleLinkedList()
	colors.push("Viridian")
	colors.push("Sap Green")
	colors.push("Van Dyke")

	assert colors.unshift() == "Viridian"
	assert colors.unshift() == "Sap Green"
	assert colors.unshift() == "Van Dyke"
	assert colors.unshift() == None

def test_remove():
	colors = SingleLinkedList()
	colors.push("Cobalt")
	colors.push("Zinc White")
	colors.push("Nickel Yellow")
	colors.push("Perinone")

	assert colors.remove("Cobalt") == 0
	assert colors.remove("Perinone") == 2
	assert colors.remove("Nickel Yellow") == 1
	assert colors.remove("Zinc White") == 0

def test_first():
	colors = SingleLinkedList()

	colors.push("Cadmium Red Light")
	assert colors.first() == "Cadmium Red Light"

	colors.push("Hansa Yellow")
	assert colors.first() == "Cadmium Red Light"

	colors.shift("Pthalo Green")
	assert colors.first() == "Pthalo Green"

def test_last():
	colors = SingleLinkedList()

	colors.push("Cadmium Red Light")
	assert colors.last() == "Cadmium Red Light"

	colors.push("Hansa Yellow")
	assert colors.last() == "Hansa Yellow"

	colors.shift("Pthalo Green")
	assert colors.last() == "Hansa Yellow"

def test_get():
	colors = SingleLinkedList()

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


if __name__ == "__main__":
	test_push()
	test_pop()
	test_shift()
	test_unshift()
	test_remove()
	test_first()
	test_last()
	test_get()