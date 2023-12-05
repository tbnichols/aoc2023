which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
for x in f:
	x = x.strip()
	card = x.split(":")[1].split("|")[0]
	card = list(map(int, filter(lambda x: x!= '', card.strip().split(" "))))
	winnums = x.split("|")[1]
	winnums = list(map(int, filter(lambda x: x!= '', winnums.strip().split(" "))))
	winners = set(card).intersection(set(winnums))
	score = (2**(len(winners)))/2
	# print(score)
	# print(int(score))

	total += int(score)
			

print(total)	
