import itertools
which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
cache = {}
def count (numlist, remainder):
	if (numlist, remainder) in cache:
		return cache[(numlist,remainder)]
	if sum(numlist) > len(list(filter(lambda x: x!= '.', remainder))):
		cache[(numlist, remainder)] = 0
		return 0
	if len(numlist) == 0 and len(list(filter(lambda x: x=='#', remainder)))==0:
		cache[(numlist, remainder)] = 1
		return 1
	if len(numlist) ==1 and len(remainder) == numlist[0] and len(list(filter(lambda x: x!='.', remainder)))==numlist[0]:
		cache[(numlist, remainder)] = 1
		return 1
	elif len(numlist) == 0 or len(list(filter(lambda x: x!='#', remainder)))==0:
		cache[(numlist, remainder)] = 0
		return 0
	combos = 0
	for i in range(len(remainder)-numlist[0]):
		if (i!=0  and remainder[i-1]=="#"):
			break
		if len(list(filter(lambda x: x== '.', remainder[i:i+numlist[0]])))==0 and remainder[i+numlist[0]]!='#':
			combos+=count(numlist[1:], remainder[i+numlist[0]+1:])
	cache[(numlist,remainder)] =combos
	return combos

f2=open('out2.txt', 'w')
for x in f:
	# subtotal = total
	x = x.strip()
	base =0
	arrangement, numlist = x.split(" ")
	numlist = tuple(list(map(int,numlist.split(",")))*5)
	arrangement=((list(arrangement)+["?"])*5)[:-1]+['.']
	# print(numlist)
	# print(arrangement)
	subtotal=count(numlist, tuple(arrangement))
	# print(subtotal)
	f2.write(x + " "+ str(subtotal) + "\n")
	total+=subtotal
# print(cache)
print(total)
