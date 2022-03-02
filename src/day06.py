def _load_file():
	# Open the file in read-only mode
	return open('data/06.txt', 'r')


def _part1():
	f = _load_file()
	lanternfish = list(map(lambda l: int(l), f.readline().split(',')))
	day = 0
	while day < 80:
		newFish = 0
		for i in range(len(lanternfish)):
			lanternfish[i] = lanternfish[i] - 1
			if lanternfish[i] == -1:
				lanternfish[i] = 6
				newFish = newFish + 1
		for i in range(newFish):
			lanternfish.append(8)
		day = day + 1
	return len(lanternfish)


def _part2():
	f = _load_file()
	lanternfish = list(map(lambda l: int(l), f.readline().split(',')))

	# One fish, two fish, new fish, blue fish
	# Felt like Dr Suess doing this one
	lanternfishBuckets = []
	for _ in range(9):
		lanternfishBuckets.append(0)
	for fish in lanternfish:
		lanternfishBuckets[fish] = lanternfishBuckets[fish] + 1
	day = 0
	while day < 256:
		newFish = lanternfishBuckets[0]
		for i in range(0, 8):
			lanternfishBuckets[i] = lanternfishBuckets[i + 1]
		lanternfishBuckets[6] = lanternfishBuckets[6] + newFish
		lanternfishBuckets[8] = newFish
		day = day + 1
	return sum(lanternfishBuckets)


def main():
	return _part1(), _part2()
