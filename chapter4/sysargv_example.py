import sys

print(sys.argv)
print(len(sys.argv))

a = False
b = False
c = False
if '-a' in sys.argv:
	a = True
	print("A option selected")
if '-b' in sys.argv:
	b = True
	print("B option selected")
if '-c' in sys.argv:
	c = True
	print("C option selected")