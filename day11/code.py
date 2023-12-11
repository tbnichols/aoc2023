which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
points = set()
ydim = 0
xdim = 0
for i, x in enumerate(f):
	x = x.strip()
	if ydim == 0:
		ydim = len(x)
	for j, y in enumerate(x):
		xdim = i+1
		if y == '#':
			points.add((i,j))
xgaps = []
ygaps = []
for x in range(xdim):
	if len(list(filter(lambda y: y[1]==x, points))) == 0:
		xgaps.append(x)
for y in range(ydim):
	if len(list(filter(lambda x: x[0]==y, points))) == 0:
		ygaps.append(y)
pointlist = list(points)
for i, point in enumerate(pointlist):
	for point2 in pointlist[i:]:
		xdist= abs(point[0]-point2[0]) +999999*len(list(filter(lambda x: point[0]<=x<=point2[0] or point2[0]<=x<=point[0], ygaps)))
		ydist = abs(point[1]-point2[1]) +999999*len(list(filter(lambda x: point[1]<=x<=point2[1] or point2[1]<=x<=point[1], xgaps)))
		# print(point)
		# print(point2)
		# print(xdist)
		# print(ydist)
		total += xdist+ydist
		# input()
print(xdim)
print(ydim)
print(xgaps)
print(ygaps)
print(points)
print(total)
