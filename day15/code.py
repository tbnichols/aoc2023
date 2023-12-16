which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
for x in f:
	x = x.strip()
	inits = x.split(',')
	for y in inits:
		sub = 0
		for cha in y:
			sub+=(ord(cha))
			sub*=17
			sub = sub %256
		total +=sub
print(total)
