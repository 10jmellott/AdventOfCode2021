from re import L


def parse_row(line):
	return line.rstrip('\n')


def _load_navigation_subsystem():
	# Open the file in read-only mode
	f = open('data/10.txt', 'r')
	return list(map(parse_row, f))

chunkPairs = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>'
}

syntaxValues = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

incompleteValues = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

def evaluate_system(system, testIncomplete):
	chunkStack = [system[0]]
	for i in range(1, len(system)):
		newChunk = system[i]
		if newChunk in syntaxValues:
			if len(chunkStack) > 0 and chunkPairs[chunkStack[len(chunkStack) - 1]] == newChunk:
				chunkStack.pop()
			elif not testIncomplete:
				return syntaxValues[newChunk]
			else:
				return 0 # discard corrupted chunks if testing for incomplete
		else:
			chunkStack.append(newChunk)

	score = 0
	if testIncomplete:
		while len(chunkStack) > 0:
			value = chunkStack.pop()
			score *= 5
			score += incompleteValues[chunkPairs[value]]
	return score


def _part1():
	subsystem = _load_navigation_subsystem()
	score = 0
	for i in range(len(subsystem)):
		system = list(subsystem[i])
		score += evaluate_system(system, False)
	return score


def _part2():
	subsystem = _load_navigation_subsystem()
	scores = []
	for i in range(len(subsystem)):
		system = list(subsystem[i])
		score = evaluate_system(system, True)
		if score > 0:
			scores.append(score)
	scores.sort()
	return scores[int((len(scores) - 1) / 2)]


def main():
	return _part1(), _part2()
