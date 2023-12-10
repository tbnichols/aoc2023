which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
pipes = {'|': lambda x: x,
		 '-':lambda x: x,
		 'L': lambda x: 1 if x==2 else 0,
		 'J':lambda x: 3 if x ==2 else 0,
		 '7':lambda x: 3 if x ==0 else 2,
		 'F':lambda x: 1 if x ==0 else 2}
total = 0
grid = []
Sxloc = 0
for i, x in enumerate(f):
	x = x.strip()
	if 'S' in x:
		Sxloc = i
	if len(grid) == 0:
		grid.append(['.' for y in range(len(x)+2)])
	grid.append(['.'] + list(x) + ['.'])
Sxloc+=1
Syloc = grid[Sxloc].index('S')
# print(grid)
for initdir in range(4):
	cur = [Sxloc, Syloc]
	steps = 0
	dir = initdir
	while cur != [Sxloc, Syloc] or steps ==0:
		if grid[cur[0]][cur[1]] == '.':
			break
		if dir == 0:
			cur = [cur[0]-1, cur[1]]
			if grid[cur[0]][cur[1]] not in ['|', '7', 'F']:
				break
		if dir == 1:
			cur = [cur[0], cur[1]+1]
			if grid[cur[0]][cur[1]] not in ['-', '7', 'J']:
				break
		if dir == 2:
			cur = [cur[0]+1, cur[1]]
			if grid[cur[0]][cur[1]] not in ['|', 'J', 'L']:
				break
		if dir == 3:
			cur = [cur[0], cur[1]-1]
			if grid[cur[0]][cur[1]] not in ['-', 'L', 'F']:
				break
		dir = pipes[grid[cur[0]][cur[1]]](dir)
		steps +=1
		# print(dir)
		# print(cur)
	if cur == [Sxloc, Syloc]:
		print((steps+1)//2)
		exit()

