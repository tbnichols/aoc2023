which = input("input 1 for test or 2 for real")
if which.isdigit() and int(which) == 1:
	path = 'example.txt'
else:
	path = 'input.txt'
f =open(path, 'r')
total = 0
for x in f:
	x = x.strip()
	games = (list(x.split(':'))[1]).split(';')
	gamenum = int(x.split(':')[0].split(' ')[-1])
	rednum = 0
	bluenum = 0
	greennum=0
	for game in games:
		colors = list(map(lambda x: x.strip(), game.split(',')))
		for color in colors:
			if 'green' in color:
				greennum = max(int(color.split(' ')[0]), greennum)
			if 'red' in color:
				rednum = max(int(color.split(' ')[0]), rednum)
			if 'blue' in color:
				bluenum = max(int(color.split(' ')[0]), bluenum)
	total += greennum*bluenum*rednum
			

print(total)	
