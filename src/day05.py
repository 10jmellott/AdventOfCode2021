def _load_file():
	# Open the file in read-only mode
	return open('data/05.txt', 'r')

class LineSegment:
	def __init__(self, segmentStr):
		segmentStr = segmentStr.strip()
		self.segmentStr = segmentStr
		p1Str, p2Str = segmentStr.split('->')

		xStr, yStr = p1Str.split(',')
		self.p1 = [int(xStr), int(yStr)]

		xStr, yStr = p2Str.split(',')
		self.p2 = [int(xStr), int(yStr)]

		self.isDiagonal = self.p1[1] != self.p2[1] and self.p1[0] != self.p2[0]

	def getAllPoints(self):
		xStep = 0 if (self.p1[0] == self.p2[0]) else (1 if (self.p1[0] < self.p2[0]) else -1)
		yStep = 0 if (self.p1[1] == self.p2[1]) else (1 if (self.p1[1] < self.p2[1]) else -1)
		points = []
		p = [self.p1[0], self.p1[1]]
		while not (p[0] == self.p2[0] and p[1] == self.p2[1]):
			points.append([p[0], p[1]])
			p[0] = p[0] + xStep
			p[1] = p[1] + yStep
		points.append(self.p2)
		return points


def _parseFile(f):
	segments = list(map(lambda l: LineSegment(l), f))
	return segments


def _countOverlappingPoints(segments):
	s = set()
	duplicates = set()
	for segment in segments:
		# Points need to be hashable; this is a quick & dirty solution
		points = map(lambda p: f'{p[0]}x{p[1]}', segment.getAllPoints())
		for point in points:
			if point in s:
				duplicates.add(point)
			s.add(point)
	return len(duplicates)


def _part1():
	f = _load_file()
	segments = _parseFile(f)
	return _countOverlappingPoints(filter(lambda s: not s.isDiagonal, segments))


def _part2():
	f = _load_file()
	segments = _parseFile(f)
	return _countOverlappingPoints(segments)


def main():
	return _part1(), _part2()
