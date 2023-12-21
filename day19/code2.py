import queue
import functools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
rules = {}
seen_empty = False
for i, line in enumerate(f):
	line = line.strip()
	if line == "":
		seen_empty = True
		break
	elif not seen_empty:
		rulename,seq = line[:-1].split("{")
		rules[rulename] = list(map(lambda x: (x[0],x[1],int(x[2:x.index(':')]), x.split(':')[1]) if ':' in x else (None, None, None, x),seq.split(",")))

def valid (xslice, mslice, aslice, sslice, currule):
	if len(xslice) ==0 or len(mslice) ==0 or len(aslice) ==0 or len(sslice) == 0:
		return 0
	if currule == "A":
		return len(xslice)*len(mslice)*len(aslice)*len(sslice)
	elif currule == "R":
		return 0
	total =0
	rulelist = rules[currule]
	for rule in rulelist:
		if rule[0] == None:
			total+=valid(xslice,mslice,aslice,sslice, rule[3])
		if rule[0] =='x':
			if rule [1]=='<':
				total += valid(list(filter(lambda x: x<rule[2], xslice)), mslice, aslice, sslice, rule[3])
				xslice = list(filter(lambda x: x>=rule[2], xslice))
			else:
				total += valid(list(filter(lambda x: x>rule[2], xslice)), mslice, aslice, sslice, rule[3])
				xslice = list(filter(lambda x: x<=rule[2], xslice))
		if rule[0] =='s':
			if rule [1]=='<':
				total += valid(xslice, mslice, aslice, list(filter(lambda x: x<rule[2], sslice)), rule[3])
				sslice = list(filter(lambda x: x>=rule[2], sslice))
			else:
				total += valid(xslice, mslice, aslice, list(filter(lambda x: x>rule[2], sslice)), rule[3])
				sslice = list(filter(lambda x: x<=rule[2], sslice))
		if rule[0] =='a':
			if rule [1]=='<':
				total += valid(xslice, mslice, list(filter(lambda x: x<rule[2],aslice)), sslice, rule[3])
				aslice = list(filter(lambda x: x>=rule[2], aslice))
			else:
				total += valid(xslice, mslice, list(filter(lambda x: x>rule[2],aslice)), sslice, rule[3])
				aslice = list(filter(lambda x: x<=rule[2], aslice))
		if rule[0] =='m':
			if rule [1]=='<':
				total += valid(xslice, list(filter(lambda x: x<rule[2], mslice)), aslice, sslice, rule[3])
				mslice = list(filter(lambda x: x>=rule[2], mslice))
			else:
				total += valid(xslice, list(filter(lambda x: x>rule[2], mslice)), aslice, sslice, rule[3])
				mslice = list(filter(lambda x: x<=rule[2], mslice))
	return total


print(valid(list(range(1,4001)), list(range(1,4001)), list(range(1,4001)), list(range(1,4001)), "in"))
				
