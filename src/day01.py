def _load_file():
	# Open the file in read-only mode
	return open('data/01.txt', 'r')

def _part1():
	f = _load_file()
	data = list(map(lambda l: int(l), f))
	increased = 0
	previousDepth = data[0]
	for depth in data[1:]:
		if previousDepth < depth:
			increased = increased + 1
		previousDepth = depth
	return increased

def _part2():
	f = _load_file()
	data = list(map(lambda l: int(l), f))
	increased = 0
	rollingDepth = data[0] + data[1] + data[2]
	for i in range(len(data) - 3):
		newRollingDepth = data[i + 1] + data[i + 2] + data[i + 3]
		if rollingDepth < newRollingDepth:
			increased = increased + 1
		rollingDepth = newRollingDepth
	return increased

def main():
	return _part1(), _part2()
