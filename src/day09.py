from functools import reduce

def parse_row(line):
	return list(map(int, list(line.rstrip('\n'))))


def _load_heightmap():
	# Open the file in read-only mode
	f = open('data/09.txt', 'r')
	return list(map(parse_row, f))


def get_neighbors(x, y, maxX, maxY):
	neighbors = []
	if x > 0:
		neighbors.append((x - 1, y))
	if y > 0:
		neighbors.append((x, y - 1))
	if x < maxX - 1:
		neighbors.append((x + 1, y))
	if y < maxY - 1:
		neighbors.append((x, y + 1))
	return neighbors


def get_basin_size(heightmap, x, y, maxX, maxY):
	exploredNeighbors = []
	unexploredNeighbors = [(x, y)]
	while len(unexploredNeighbors) > 0:
		neighbor = unexploredNeighbors.pop()
		exploredNeighbors.append(neighbor)
		newNeighbors = get_neighbors(neighbor[0], neighbor[1], maxX, maxY)
		for i in range(len(newNeighbors)):
			if heightmap[newNeighbors[i][1]][newNeighbors[i][0]] != 9:
				if newNeighbors[i] not in exploredNeighbors and newNeighbors[i] not in unexploredNeighbors:
					unexploredNeighbors.append(newNeighbors[i])
	return len(exploredNeighbors)


def _part1():
	heightmap = _load_heightmap()
	maxX = len(heightmap[0])
	maxY = len(heightmap)

	risk = 0
	for x in range(maxX):
		for y in range(maxY):
			value = heightmap[y][x]
			neighbors = get_neighbors(x, y, maxX, maxY)
			if (all(map(lambda n: heightmap[n[1]][n[0]] > value, neighbors))):
				risk += 1 + value

	return risk


def _part2():
	heightmap = _load_heightmap()
	maxX = len(heightmap[0])
	maxY = len(heightmap)

	basins = []
	for x in range(maxX):
		for y in range(maxY):
			value = heightmap[y][x]
			neighbors = get_neighbors(x, y, maxX, maxY)
			if (all(map(lambda n: heightmap[n[1]][n[0]] > value, neighbors))):
				basins.append(get_basin_size(heightmap, x, y, maxX, maxY))

	maxBasins = []
	for i in range(3):
		maxBasins.append(max(basins))
		basins.remove(maxBasins[i])

	return reduce((lambda x, y: x * y), maxBasins)


def main():
	return _part1(), _part2()
