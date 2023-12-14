import itertools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
grid = []

for x in f:
	x = x.strip()
	grid.append(list(x))
for x in grid:
	print(str(x))
for i in range(1, len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "O":
			cur = i-1
			while grid[cur][j] == '.':
				cur-=1
				if cur == -1:
					break
			grid[i][j] = '.'
			grid[cur+1][j] = "O"
print()
for x in grid:
	print(str(x))
for i, x in enumerate(grid):
	total+=(len(grid)-i)*len(list(filter(lambda a: a=='O', x)))
print(total)



