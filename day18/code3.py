from collections import defaultdict
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
pipes = {'.': lambda x: (x, None, None, None),
		 '|': lambda x: (x, None, None, None),
		 '-':lambda x: (x, None, None, None),
		 'L': lambda x: (1, 'L', [(-1,1)], [(1,1), (1,0), (1,-1), (0,-1), (-1,-1)]) if x==2 else (0, 'R', [(1,1), (1,0), (1,-1), (0,-1), (-1,-1)], [(-1,1)]),
		 'J':lambda x: (3, 'R', [(-1, 1),  (0,1), (1,1), (1,0), (1,-1)], [(-1,-1)]) if x ==2 else (0, 'L', [(-1,-1)], [(1,1), (1,0), (1,-1), (0,1), (-1,1)]),
		 '7':lambda x: (3, 'L', [(1,-1)], [(-1,-1), (-1, 0), (-1, 1), (0,1), (1,1)]) if x ==0 else (2, 'R', [(-1,1), (-1,0), (-1,-1), (0,1), (1,1)], [(1,-1)]),
		 'F':lambda x: (1, 'R', [(1,-1), (0,-1), (-1,-1), (-1, 0),  (-1,1)], [(1,1)]) if x ==0 else (2, 'L', [(1,1)],[(1,-1), (-1,0), (-1,1), (0,-1), (-1,-1)]),
}
prevdict = {
	('R', 'D'): '7',
	('D', 'L'): 'J',
	('L', 'D'): 'F',
	('D', 'R'): 'L',
	('R', 'U'): 'J',
	('L', 'U'): 'L',
	('U', 'R'): 'F',
	('U', 'L'): '7'

}
total = 0
grid = defaultdict(lambda: '.')
turncount = 0
Sxloc = 0
Syloc = 0
grid[(0,0)]='S'
cur = [0,0]
minx = 0
maxx = 0
miny =0
maxy = 0
prevdir = False
next = [(1,0), (0,1), (-1,0), (0,-1)]
initdict = {
	'0':'R',
	'1':'D',
	'2':'L',
	'3':'U'
}
pointlist = [tuple(cur)]
for i, x in enumerate(f):
	x = x.strip()
	dir, mag, color = x.split(' ')
	dir = initdict[color[-2]]
	mag = int(color[2:7], 16)
	if prevdir:
		grid [tuple(cur)] = prevdict[(prevdir, dir)]
	prevdir = dir
	if dir == 'R':
		cur[1]+=int(mag)
	if dir == 'L':
		cur[1]-=int(mag)
	if dir == 'U':
		cur[0]-=int(mag)
	if dir == 'D':
		cur[0]+=int(mag)
	minx = min(minx, cur[0])
	miny = min(miny, cur[1])
	maxx = max(maxx, cur[0])
	maxy = max(maxy, cur[1])
	pointlist.append(tuple(cur))
pointlist.append((0,0))
area = 0
perim = 0
for i in range(len(pointlist)-1):
	area += .5*(pointlist[i][0]+pointlist[i+1][0])*(pointlist[i][1]-pointlist[i+1][1])
	perim += abs(pointlist[i][0]-pointlist[i+1][0])+ abs(pointlist[i][1]-pointlist[i+1][1])
# pipegrid = defaultdict(lambda: '.')
# print(grid)
cur = [Sxloc, Syloc]
# steps = 0
# dir = initdir
# while cur != [Sxloc, Syloc] or steps ==0:
# 	steps +=1
# 	pipegrid[tuple(cur)] = 'P'
# 	if dir == 0:
# 		cur = [cur[0]-1, cur[1]]
# 	if dir == 1:
# 		cur = [cur[0], cur[1]+1]
# 	if dir == 2:
# 		cur = [cur[0]+1, cur[1]]
# 	if dir == 3:
# 		cur = [cur[0], cur[1]-1]
# 	if cur == [Sxloc, Syloc]:
# 		# print(steps)
# 		break
# 	dir, turn, leftmarks, rightmarks = pipes[grid[tuple(cur)]](dir)
# 	if turn:
# 		if turn == 'L':
# 			turncount +=1
# 		else:
# 			turncount-=1
# 		for mark in leftmarks:
# 			if pipegrid[(cur[0]+mark[0],cur[1]+mark[1])] != 'P':
# 					pipegrid[(cur[0]+mark[0],cur[1]+mark[1])] = 'L'
# 		for mark in rightmarks:
# 			if pipegrid[(cur[0]+mark[0],cur[1]+mark[1])] != 'P':
# 				pipegrid[(cur[0]+mark[0],cur[1]+mark[1])] = 'R'
	
	# print(dir)
	# print(cur)
if cur == [Sxloc, Syloc]:
	# print((steps+1)//2)
	# print(turncount)
	# count = 0
	# hole = False
	# if turncount <0:
	# 	key = "R"
	# else:
	# 	key = 'L'
	# f=open('pipegrid.txt', 'w')
	# lines=[]
	# for x in range(minx-1, maxx+2):
	# 	line = []
	# 	for y in range(miny-1, maxy+2):
	# 		if pipegrid[(x,y)] == key or pipegrid[(x,y)]  == '.' and hole:
	# 			count +=1
	# 			hole = True
	# 			line.append('#')
	# 		elif pipegrid[(x,y)] == "P":
	# 			count+=1
	# 			hole = False
	# 			line.append('P')
	# 		else:
	# 			line.append('.')
	# 	lines.append(line)
	# lines[0][0] = 'O'	
	# lines[0][-1] = 'O'	
	# lines[-1][0] = 'O'	
	# lines[-1][-1] = 'O'
	# excluded = 4
	# prevexcluded = 0
	# while prevexcluded != excluded:
	# 	prevexcluded = excluded
	# 	for x in range(len(lines)):
	# 		for y in range(len(lines[x])):
	# 			if lines[x][y] in  ['O', '#', 'P']:
	# 				continue
	# 			for xmod,ymod in next:
	# 				if 0<=x+xmod<len(lines) and 0<=y+ymod<len(lines[x]):
	# 					if lines[x+xmod][y+ymod] == 'O':
	# 						lines[x][y]='O'
	# 						excluded+=1
	# 						break
	# for line in lines:
	# 	f.write("".join(line))
	# 	f.write("\n")
	# print(count)
	# print((len(lines)*len(lines[0]))-excluded)
	print(area+perim//2+1)
	exit()

