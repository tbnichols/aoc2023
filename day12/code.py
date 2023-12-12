import itertools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0

def valid(vals, nums):
	# print(vals)
	# print(nums)
	for num in nums:
		# print(num)
		# print(vals)
		if not (len(list(filter( lambda x: vals[x+1]-1!=vals[x], [i for i in range(num-1)])))==0 and (len(vals) == num or len(list(filter( lambda x: vals[x+1]-1!=vals[x], [i for i in range(num)])))==1)):
			return 0
		vals = vals[num:]
	return 1

f2=open('out1.txt', 'w')
for x in f:
	subtotal = total
	x = x.strip()
	arrangement, numlist = x.split(" ")
	numlist = list(map(int,numlist.split(",")))
	poss = []
	deffo = []
	for i, val in enumerate(arrangement):
		if val == '?':
			poss.append(i)
		elif val == "#":
			deffo.append(i)
	for val in itertools.combinations(poss, sum(numlist)-len(deffo)):
		total += valid(sorted(list(val)+deffo), numlist)
	# print(x)
	# print(total-subtotal)
	f2.write(x + " "+ str(total-subtotal) + "\n")
print(total)
