which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
seeds = list(map(int, f.readline().split(':')[1].strip().split(" ")))
print(seeds)
new_seeds=[]
for i in range(len(seeds)//2):
	new_seeds.append((seeds[2*i], seeds[2*i+1]))
seeds = new_seeds
mappings = [[]]
f.readline()
f.readline()
index = 0
next_line = f.readline()
while next_line:
	if len(list(filter(lambda x: x.isdigit(), next_line))) ==0:
		f.readline()
		next_line = f.readline()
		index +=1
		mappings.append([])
		continue
	mappings[index].append(list(map(int, next_line.strip().split(" "))))	
	next_line = f.readline()
print(mappings)
for i in range(len(mappings)):
	new_seeds = []
	for seed in seeds:
		snips = []
		found = False
		for row in mappings[i]:
			if seed[0]>= row[1] and seed[0]+seed[1] < row[1] + row[2]:
				new_seeds.append((row[0]+seed[0]-row[1], seed[1]))
				found = True
			elif seed[0]< row[1] and (seed[0]+seed[1])>=row[1]:
				new_seeds.append((row[0], min(row[2], (seed[0]+seed[1]) - row[1])))
				snips.append((row[1], min(row[2], (seed[0]+seed[1]) - row[1])))
			elif row[1]<= seed[0] < row[1]+row[2]:
				new_seeds.append((row[0]+seed[0]-row[1], min(seed[1], row[2]+row[1]-seed[0])))
				snips.append((seed[0], min(seed[1], row[2]+row[1]-seed[0])))
		
		if not found:
			snips.sort(key=lambda x: x[0])
			base = seed[0]
			for snip in snips:
				if snip[0]-base!=0:
					new_seeds.append((base, snip[0]-base))
				base = snip[0]+snip[1]
			if seed[1]+seed[0]-base != 0:
				new_seeds.append((base, seed[1]+seed[0]-base))
	seeds = new_seeds
print(min(seeds))
