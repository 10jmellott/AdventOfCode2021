def _load_file():
	# Open the file in read-only mode
	return open('data/11.txt', 'r')

def parseOctopi():
	f = _load_file()
	octopi = []
	for line in f.readlines():
		octopi.append(list(map(lambda c: int(c), list(line.rstrip('\n')))))
	return octopi

def flashOctopus(octopi, x, y, flashpoints):
	if ((x, y) in flashpoints):
		return
	if x < 0 or y < 0:
		return
	if y >= len(octopi) or x >= len(octopi[y]):
		return
	octopi[y][x] += 1
	if (octopi[y][x] < 10):
		return
	flashpoints.add((x, y))
	octopi[y][x] = 0
	for yi in range(y - 1, y + 2):
		for xi in range(x - 1, x + 2):
			if xi == x and yi == y:
				continue
			flashOctopus(octopi, xi, yi, flashpoints)


def stepOctopi(octopi):
	flashpoints = set()
	for y in range(len(octopi)):
		for x in range(len(octopi[y])):
			flashOctopus(octopi, x, y, flashpoints)
	return octopi, len(flashpoints)

def _part1():
	octopi = parseOctopi()
	step = 0
	totalFlashes = 0
	while step < 100:
		octopi, flashes = stepOctopi(octopi)
		totalFlashes += flashes
		step += 1
	return totalFlashes


def _part2():
	octopi = parseOctopi()
	step = 0
	flashes = 0
	while flashes != 100:
		octopi, flashes = stepOctopi(octopi)
		step += 1
	return step


def main():
	return _part1(), _part2()
