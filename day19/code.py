import queue
import functools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
rules = {}
total = 0
seen_empty = False
for i, line in enumerate(f):
	line = line.strip()
	if line == "":
		seen_empty = True
		continue
	elif not seen_empty:
		rulename,seq = line[:-1].split("{")
		rules[rulename] = list(map(lambda x: (x[0],x[1],int(x[2:x.index(':')]), x.split(':')[1]) if ':' in x else (None, None, None, x),seq.split(",")))
	else:
		currule = 'in'
		x, m, a, s = map(lambda x: int("".join(list(filter(lambda y: y.isdigit(), x)))), line.split(','))  
		while currule not in ['A','R']:
			rulelist = rules[currule]
			for rule in rulelist:
				if rule[0] == None:
					currule=rule[3]
				if rule[0] =='x':
					if rule [1]=='<':
						if x<rule[2]:
							currule = rule[3]
							break
					else:
						if x>rule[2]:
							currule = rule[3]
							break
				if rule[0] =='s':
					if rule [1]=='<':
						if s<rule[2]:
							currule = rule[3]
							break
					else:
						if s>rule[2]:
							currule = rule[3]
							break
				if rule[0] =='a':
					if rule [1]=='<':
						if a<rule[2]:
							currule = rule[3]
							break
					else:
						if a>rule[2]:
							currule = rule[3]
							break
				if rule[0] =='m':
					if rule [1]=='<':
						if m<rule[2]:
							currule = rule[3]
							break
					else:
						if m>rule[2]:
							currule = rule[3]
							break
		if currule == 'A':
			total += x+m+a+s
print(total)
				
