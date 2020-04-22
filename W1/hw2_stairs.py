import sys

num = int(sys.argv[1])

count = num
while num > 0:
	str = ""
	num -= 1
	spaces = num
	for i in range(spaces):
		str += " "
	diez = count - spaces
	for i in range(diez):
		str += "#"
	print(str)