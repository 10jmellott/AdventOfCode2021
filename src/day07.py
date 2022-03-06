def _load_crabs():
	# Open the file in read-only mode
	f = open('data/07.txt', 'r')
	return list(map(lambda l: int(l), f.readline().split(',')))

def _part1():
	crabs = _load_crabs()
	maxCrab = max(crabs)
	optimalFuel = sum(crabs)
	for i in range(1, maxCrab + 1):
		fuelCost = sum(map(lambda c: abs(i - c), crabs))
		if fuelCost < optimalFuel:
			optimalFuel = fuelCost
	return optimalFuel


def _part2():
	crabs = _load_crabs()
	maxCrab = max(crabs)

	# Simple memoization here removes the need to
	# recalculate the integer sequence
	fuelSteps = {}
	for i in range(0, maxCrab + 1):
		fuelSteps[i] = sum(range(1, i + 1))

	optimalFuel = sum(map(lambda c: fuelSteps[c], crabs))
	for i in range(1, maxCrab + 1):
		fuelCost = sum(map(lambda c: fuelSteps[abs(i - c)], crabs))
		if fuelCost < optimalFuel:
			optimalFuel = fuelCost
	return optimalFuel


def main():
	return _part1(), _part2()
