import functools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0

grid = []
def smudgeable(stack,reflect):
	return sum(map(lambda j: functools.reduce(lambda a,b: a+b, map(lambda a: 1 if a[0]!=a[1] else 0, zip(stack[j], reflect[j]))),range(len(stack))))==1
def process(grid):
	# vert check first
	stack = [grid[0]]
	for i in range(1,len(grid)):
		if smudgeable(stack[i-min(len(stack),len(grid)-i):], grid[min(i+len(stack), len(grid))-1:i-1:-1]):
			return 100*i
		stack.append(grid[i])
	stack = [[i[0] for i in grid]]
	for i in range(1, len(grid[0])):
		if smudgeable(stack[i-min(len(stack), len(grid[0])-i):], [[j[k] for j in grid] for k in range(min(len(stack)+i, len(grid[0]))-1, i-1, -1)]):
			return i
		stack.append([j[i] for j in grid])

for x in f:
	x = x.strip()
	if x =="":
		print(grid)
		total+=process(grid)
		grid = []
	else:
		grid.append(x)
total+=process(grid)
print(total)
