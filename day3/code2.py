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
		if line[index]=='*':
			num1 = 0
			num1fin = False
			num2 = 0
			for j in range(max(0,lineind-1), min(len(grid)-1, lineind+1)+1):
				for k in range(max(0, index-1), min(index+2, len(grid)-1)):
					print(grid[j][k])
					if grid[j][k].isdigit():
						base = k
						while grid[j][base].isdigit():
							base = base-1
							if base == -1:
								break
						base +=1
						while grid[j][base].isdigit():
							print(grid[j][base])
							if not num1fin:
								num1 = num1*10 + int(grid[j][base])
							else:
								num2 = num2*10 + int(grid[j][base])
							base+=1
							if base == len(line):
								break
						num1fin = True
						if base>k+1:
							print("non left")
							break
			total += num1*num2
		index +=1
		

print(total)	
