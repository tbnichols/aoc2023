which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
grid = []
for x in f:
	x = x.strip()
	grid.append(x)
print(grid)
for lineind, line in enumerate(grid):
	index = 0
	num = 0
	while index<len(line):
		if line[index].isdigit():
			num = num *10 +int(line[index])
		if (not (line[index].isdigit()) or index==len(line)-1) and num != 0:
			adjustment =1 
			if index == len(line)-1 and line[index].isdigit():
				adjustment = 0
			added = False
			for j in range(max(0,lineind-1), min(len(grid)-1, lineind+1)+1):
				for k in range(max(0, index-len(str(num))-adjustment), index+1):
					if not added and (not grid[j][k].isdigit()) and not (grid[j][k] == '.'):
						total += num
						added = True
			num = 0
		index +=1

print(total)	
