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
	if (node[0] == len(grid)-1) and node[1] == (len(grid[node[0]])-1):
		print(dist)
		break
	if (node, path[:4]) in seen:
		continue
	restricted = len(path)>=4 and 3 in functools.reduce(lambda a,b: (a[0]+b[0], a[1]+b[1]), map(lambda x: (abs(path[x][0]-path[x-1][0]), abs(path[x-1][1]-path[x][1])), range(1,4)))
	candidates = list(map(lambda x: (node[0]+x[0], node[1]+x[1]), next))
	valid = list(filter(lambda x: x[0]>=0 and x[1]>=0 and x[0]<len(grid) and x[1]<len(grid[x[0]]) and (len(path) ==1 or x!= path[1]) and (not restricted or x!=(node[0] + (node[0]-path[1][0]), node[1]+(node[1]-path[1][1]))), candidates))
	for nextnode in valid:
		pq.put((dist+grid[nextnode[0]][nextnode[1]], tuple([nextnode]+list(path))))
	seen.add((node, path[:4]))
	