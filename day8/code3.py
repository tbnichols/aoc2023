import functools
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
curnodes = [[key, key, 0] for key in filter(lambda x: x[2] =='A', nodes.keys())]
findable = set(list(map(lambda x: x[0], curnodes)))
founds = {key: [False, 0, None] for key in nodes.keys()}
numfounds = 0
numkeys = len(nodes.keys())
curpat = 0
steps = 0
print(nodes)
while len(curnodes)!=0:
	steps +=1
	newcurs = []
	if pattern[curpat] == "L":
		for node in curnodes:
			next_node = nodes[node[1]][0]
			if next_node[2]== 'Z':
				founds[node[0]] = [True, steps-node[2], next_node, steps, node[2]] 
			else:
				newcurs.append([node[0], next_node, node[2]])
			if next_node not in findable:
				newcurs.append([next_node, next_node, steps])
				findable.add(next_node)
	else:
		for node in curnodes:
			next_node = nodes[node[1]][1]
			if next_node[2]== 'Z':
				founds[node[0]] = [True, steps-node[2], next_node, steps, node[2]]
			else:
				newcurs.append([node[0], next_node, node[2]])
			if next_node not in findable:
				newcurs.append([next_node, next_node, steps])
				findable.add(next_node)
	curnodes = newcurs
	curpat = (curpat+1)%len(pattern)
cyclestarts = [founds[key] for key in filter(lambda x: x[2] == 'A', nodes.keys())]
print(cyclestarts)
print([founds[x] for x in map(lambda y: y[2], cyclestarts)])
input()
while len(list(filter(lambda a: a[1]==cyclestarts[0][1],cyclestarts)))!=len(cyclestarts):
	cyclestarts.sort(key=lambda x: x[1])
	newcyclestarts = cyclestarts[1:]
	newcyclestarts.append([True, cyclestarts[0][1] + founds[cyclestarts[0][2]][1], founds[cyclestarts[0][2]][2]])
	cyclestarts = newcyclestarts

print(cyclestarts)

