from functools import reduce

def _load_file():
	# Open the file in read-only mode
	return open('data/02.txt', 'r')

# Reads the line and transforms it into a horizontal position
# if the command is forward and depth if the command is up or down
def _transform(line):
	(command, value) = line.split()
	if command == 'up':
		return (0, int(value))
	elif command == 'down':
		return (0, -int(value))
	elif command == 'forward':
		return (int(value), 0)
	return None


def _part1():
	f = _load_file()
	data = list(map(_transform, f))
	# Sum the horizontal and vertical distance
	(a, b) = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), data)
	return abs(a * b)


def _part2():
	f = _load_file()
	data = list(map(_transform, f))
	aim = 0
	depth = 0
	horizontalPosition = 0
	for (x, y) in data:
		aim += y
		horizontalPosition += x
		depth += x * aim
	return abs(depth * horizontalPosition)


def main():
	return _part1(), _part2()
