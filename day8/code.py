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
curnode = "AAA"
curpat = 0
steps = 0
print(nodes)
while curnode != "ZZZ":
	if pattern[curpat] == "L":
		curnode = nodes[curnode][0]
	else:
		curnode = nodes[curnode][1]
	steps +=1
	curpat = (curpat+1)%len(pattern)
print(steps)
