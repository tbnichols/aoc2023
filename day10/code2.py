which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example2.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
pipes = {'|': lambda x: (x, None, None, None),
		 '-':lambda x: (x, None, None, None),
		 'L': lambda x: (1, 'L', [(-1,1)], [(1,1), (1,0), (1,-1), (0,-1), (-1,-1)]) if x==2 else (0, 'R', [(1,1), (1,0), (1,-1), (0,-1), (-1,-1)], [(-1,1)]),
		 'J':lambda x: (3, 'R', [(-1, 1),  (0,1), (1,1), (1,0), (1,-1)], [(-1,-1)]) if x ==2 else (0, 'L', [(-1,-1)], [(1,1), (1,0), (1,-1), (0,1), (-1,1)]),
		 '7':lambda x: (3, 'L', [(1,-1)], [(-1,-1), (-1, 0), (-1, 1), (0,1), (1,1)]) if x ==0 else (2, 'R', [(-1,1), (-1,0), (-1,-1), (0,1), (1,1)], [(1,-1)]),
		 'F':lambda x: (1, 'R', [(1,-1), (0,-1), (-1,-1), (-1, 0),  (-1,1)], [(1,1)]) if x ==0 else (2, 'L', [(1,1)],[(1,-1), (-1,0), (-1,1), (0,-1), (-1,-1)]),
}
total = 0
grid = []
turncount = 0
Sxloc = 0
for i, x in enumerate(f):
	x = x.strip()
	if 'S' in x:
		Sxloc = i
	if len(grid) == 0:
		grid.append(['.' for y in range(len(x)+2)])
	grid.append(['.'] + list(x) + ['.'])
grid.append(['.' for y in range(len(x)+2)])
	
Sxloc+=1
Syloc = grid[Sxloc].index('S')
pipegrid = []
# print(grid)
for initdir in range(4):
	cur = [Sxloc, Syloc]
	pipegrid = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]
	steps = 0
	dir = initdir
	while cur != [Sxloc, Syloc] or steps ==0:
		pipegrid[cur[0]][cur[1]] = 'P'
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
		dir, turn, leftmarks, rightmarks = pipes[grid[cur[0]][cur[1]]](dir)
		if turn:
			if turn == 'L':
				turncount +=1
			else:
				turncount-=1
			for mark in leftmarks:
				if pipegrid[cur[0]+mark[0]][cur[1]+mark[1]] != 'P':
					pipegrid[cur[0]+mark[0]][cur[1]+mark[1]] = 'L'
			for mark in rightmarks:
				print(mark)
				print(cur)
				print(len(pipegrid[cur[0]+mark[0]]))
				if pipegrid[cur[0]+mark[0]][cur[1]+mark[1]] != 'P':
					pipegrid[cur[0]+mark[0]][cur[1]+mark[1]] = 'R'
		
		steps +=1
		# print(dir)
		# print(cur)
	if cur == [Sxloc, Syloc]:
		print((steps+1)//2)
		print(turncount)
		f=open('pipegrid.txt', 'w')
		for line in pipegrid:
			f.write("".join(line))
			f.write("\n")
		count = 0
		hole = False
		if turncount <0:
			key = "R"
		else:
			key = 'L'
		for x in pipegrid:
			for y in x:
				if y == key or y == '.' and hole:
					count +=1
					hole = True
				if y == "P":
					hole = False
		print(count)
		exit()

