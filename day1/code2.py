f =open('input.txt', 'r')
total = 0
for x in f:
	curword = ""
	num1 = None
	num2 = None
	for y in x:
		curword = curword + y
		if curword[-3:] in ['one', 'two', 'six']:
			if y == 'e':
				y='1'
			elif y == 'o':
				y='2'
			else: 
				y='6'
		elif curword[-4:] in ['four', 'five', 'nine']:
			if y == 'r':
				y='4'
			elif curword [-4:] == 'five':
				y='5'
			else:
				y='9'
		elif curword[-5:] in ['three', 'seven', 'eight']:
			if y == 'e':
				y='3'
			elif y == 'n':
				y='7'
			else: 
				y='8'
		if y.isdigit():
			if num1 is None:
				num1 = int(y)
			num2 = int(y)
	total += num1 *10 + num2
print(total)	
