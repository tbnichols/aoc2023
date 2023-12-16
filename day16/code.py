import functools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
grid = []
for i, x in enumerate(f):
	x = x.strip()
	grid.append(list(x))
lights = [['.' for y in x] for x in grid]
seen = set()
def lightup (orientation, pos):	
	if (orientation, pos) in  seen:
		return
	while True:
		if pos[1]>=0:	
			lights[pos[0]][pos[1]] = '#'
		seen.add((orientation, pos))
		pos = (pos[0]+orientation[0], pos[1]+orientation[1])
		if not (0<=pos[0]<len(grid) and 0<=pos[1]<len(grid[0])):
			return
		if grid [pos[0]][pos[1]] == '|' and (orientation  == (0,1) or orientation == (0,-1)):
			lightup((1,0), pos)
			lightup((-1,0), pos)
			return
		if grid [pos[0]][pos[1]] == '/' and (orientation  == (0,1)):
			lightup((-1,0), pos)
			return
		if grid [pos[0]][pos[1]] == '/' and (orientation  == (0,-1)):
			lightup((1,0), pos)
			return
		if grid [pos[0]][pos[1]] == '\\' and (orientation  == (0,1)):
			lightup((1,0), pos)
			return
		if grid [pos[0]][pos[1]] == '\\' and (orientation  == (0,-1)):
			lightup((-1,0), pos)
			return
		if grid [pos[0]][pos[1]] == '-' and (orientation  == (1,0) or orientation == (-1,0)):
			lightup((0,1), pos)
			lightup((0,-1), pos)
			return
		if grid [pos[0]][pos[1]] == '/' and (orientation  == (1,0)):
			lightup((0,-1), pos)
			return
		if grid [pos[0]][pos[1]] == '/' and (orientation  == (-1,0)):
			lightup((0,1), pos)
			return
		if grid [pos[0]][pos[1]] == '\\' and (orientation  == (1,0)):
			lightup((0, 1), pos)
			return
		if grid [pos[0]][pos[1]] == '\\' and (orientation  == (-1,0)):
			lightup((0, -1), pos)
			return

lightup((0,1), (0,-1))
print(functools.reduce(lambda a,b: a+b, map(lambda y: len(list(filter(lambda x: x=='#', y))), lights)))