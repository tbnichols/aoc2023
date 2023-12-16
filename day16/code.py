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
contdict = {
	('|', (0,1)): [(1,0), (-1,0)],
	('|', (0,-1)): [(1,0), (-1,0)],
	('-', (1,0)): [(0,-1), (0,1)],
	('-', (-1,0)): [(0,-1), (0,1)],
	('\\', (0,1)): [(1,0)],
	('\\', (1,0)): [(0,1)],
	('\\', (0,-1)): [(-1,0)],
	('\\', (-1,0)): [(0,-1)],
	('/', (-1,0)): [(0,1)],
	('/', (1,0)): [(0,-1)],
	('/', (0,-1)): [(1,0)],
	('/', (0,1)): [(-1, 0)]
}
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
		if (grid[pos[0]][pos[1]], orientation) not in contdict:
			continue
		for nextdir in contdict[(grid[pos[0]][pos[1]], orientation)]:
			lightup(nextdir, pos)
		return

lightup((0,1), (0,-1))
print(functools.reduce(lambda a,b: a+b, map(lambda y: len(list(filter(lambda x: x=='#', y))), lights)))