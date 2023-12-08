which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
pattern = f.readline().strip()
f.readline()
next = f.readline()
nodes = {}
while next:
	nodes[next.split("=")[0].strip()] = (next.split('=')[1].split(",")[0].strip()[1:], next.split('=')[1].split(",")[1].strip()[:-1])
	next = f.readline()
curnodes = list(filter(lambda x: x[2] =='A', nodes.keys()))
curpat = 0
steps = 0
print(nodes)
while len(list(filter(lambda x: x[2]!='Z', curnodes))) != 0:
	if pattern[curpat] == "L":
		curnodes = [nodes[x][0]for x in curnodes]
	else:
		curnodes = [nodes[x][1] for x in curnodes]
	steps +=1
	curpat = (curpat+1)%len(pattern)
print(steps)
