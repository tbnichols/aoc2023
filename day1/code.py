f =open('input.txt', 'r')
total = 0
for x in f:
	num1 = None
	num2 = None
	for y in x:
		if y.isdigit():
			if num1 is None:
				num1 = int(y)
			num2 = int(y)
	total += num1 *10 + num2
print(total)	
