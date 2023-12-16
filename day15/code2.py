which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
boxes = [[] for i in range(256)]
for x in f:
	x = x.strip()
	inits = x.split(',')
	for y in inits:
		box = 0
		for cha in y:
			if cha  =='-' or cha=='=':
				break
			box+=(ord(cha))
			box*=17
			box = box %256
		if "=" in y:
			replaced = False
			for cur, lens in enumerate(boxes[box]):
				if lens[0] == y[:y.index('=')]:
					boxes[box][cur] = (y[:y.index('=')],y[y.index('=')+1])
					replaced = True
			if not replaced:
				boxes[box].append((y[:y.index('=')],y[y.index('=')+1]))
		else:
			for lens in boxes[box]:
				if lens[0] == y[:y.index('-')]:
					boxes[box].remove(lens)
					break

		# print(boxes)
		# input()

for i in range(256):
	for j, lens in enumerate(boxes[i]):
		total+= (i+1)*(j+1)*int(lens[1])
print(total)
