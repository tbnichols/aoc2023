import queue
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
	grid.append(list(map(int,x)))
print(grid)
pq = queue.PriorityQueue()
pq.put((0, tuple([(0,0)])))
found = False
seen = set()
seentwice = set()
next = [(1,0), (0,1), (-1,0), (0,-1)]
while not pq.empty():
	cur = pq.get()
	dist = cur[0]
	path = cur[1]
	node = path[0]
	dir = (1,0) if len(path)==1 or node[0]-path[1][0] !=0 else (0,1)
	if (node[0] == len(grid)-1) and node[1] == (len(grid[node[0]])-1):
		print(dist)
		break
	if (node, dir) in seen:
		continue
	valdirs = list(filter(lambda x: abs(x[0])!= abs(dir[0]) or abs(x[1])!=abs(dir[1]) , next))
	candidates = ((node[0]+x[0]*i, node[1]+x[1]*i) for x in valdirs for i in range(4,11))
	valid = list(filter(lambda x: x[0]>=0 and x[1]>=0 and x[0]<len(grid) and x[1]<len(grid[x[0]]), candidates))
	for nextnode in valid:
		subtotal = 0
		if nextnode[0]>node[0]:
			for x in range(abs(nextnode[0]-node[0])):
				subtotal+=grid[node[0]+x+1][node[1]]
		else:	
			for x in range(abs(nextnode[0]-node[0])):
				subtotal+=grid[node[0]-x-1][node[1]]
		if nextnode[1]>node[1]:
			for x in range(abs(nextnode[1]-node[1])):
				subtotal+=grid[node[0]][node[1]+x+1]
		else:	
			for x in range(abs(nextnode[1]-node[1])):
				subtotal+=grid[node[0]][node[1]-x-1]
			
		pq.put((dist + subtotal, tuple([nextnode]+list(path))))
	seen.add((node, dir))
	