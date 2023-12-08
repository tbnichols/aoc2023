which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
seeds = list(map(int, f.readline().split(':')[1].strip().split(" ")))
print(seeds)
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
		found = False
		for row in mappings[i]:
			if seed>= row[1] and seed < row[1] + row[2]:
				new_seeds.append(row[0]+seed-row[1])
				found = True
				break
		if not found:
			new_seeds.append(seed)
	seeds = new_seeds
	print(seeds)
print(min(seeds))
