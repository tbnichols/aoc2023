import itertools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
grid = []
cache = {}
def memoize(grid, dir):
	if (tuple([tuple(i) for i in grid]), dir) in cache:
		return cache[(tuple([tuple(i) for i in grid]), dir)] 
	initgrid = grid
	if dir == 'N':
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
		cache[(tuple([tuple(i) for i in initgrid]), dir)] = grid
		return grid
	
	if dir == 'E':
		for i in range(len(grid)):
			for j in reversed(range(len(grid[i])-1)):
				if grid[i][j] == "O":
					cur = j+1
					while grid[i][cur] == '.':
						cur+=1
						if cur == len(grid[i]):
							break
					grid[i][j] = '.'
					grid[i][cur-1] = "O"
		cache[(tuple([tuple(i) for i in initgrid]), dir)] = grid
		return grid

	if dir == 'S':
		for i in reversed(range(len(grid)-1)):
			for j in range(len(grid[i])):
				if grid[i][j] == "O":
					cur = i+1
					while grid[cur][j] == '.':
						cur+=1
						if cur == len(grid):
							break
					grid[i][j] = '.'
					grid[cur-1][j] = "O"
		cache[(tuple([tuple(i) for i in initgrid]), dir)] = grid
		return grid

	if dir == 'W':
		for i in range(len(grid)):
			for j in range(1, len(grid[i])):
				if grid[i][j] == "O":
					cur = j-1
					while grid[i][cur] == '.':
						cur-=1
						if cur == -1:
							break
					grid[i][j] = '.'
					grid[i][cur+1] = "O"
		cache[(tuple([tuple(i) for i in initgrid]), dir)] = grid
		return grid

pattern = "NWSE"
for x in f:
	x = x.strip()
	grid.append(list(x))
seen = {}
for x in range(10**9):
	if tuple([tuple(i) for i in grid]) in seen:
		cyclelen = x-seen[tuple([tuple(i) for i in grid])]
		orphans = (10**9 -x) %cyclelen
		for i in range(orphans):
			grid = memoize(grid, 'N')
			grid = memoize(grid, 'W')
			grid = memoize(grid, 'S')
			grid = memoize(grid, 'E')
		break
	else:
		seen[tuple([tuple(i) for i in grid])] = x
	grid = memoize(grid, 'N')
	grid = memoize(grid, 'W')
	grid = memoize(grid, 'S')
	grid = memoize(grid, 'E')
for i, x in enumerate(grid):
	total+=(len(grid)-i)*len(list(filter(lambda a: a=='O', x)))
print(total)



