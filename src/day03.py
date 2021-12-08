from functools import reduce

def _load_file():
	# Open the file in read-only mode
	return open('data/03.txt', 'r')

def _gamma(x, y):
	return list(map(lambda i: int(x[i]) + (-1 if int(y[i]) == 0 else 1), range(len(x))))

def _toNumber(bits):
	return int(''.join(bits), 2)

def _part1():
	f = _load_file()
	data = list(map(lambda s : list(s.rstrip('\n')), f))
	gammaRaw = list(map(lambda x: '1' if x > 0 else '0', list(reduce(_gamma, data))))
	gamma = _toNumber(gammaRaw)
	epsilon = _toNumber(list(map(lambda x: '0' if x == '1' else '1', gammaRaw)))
	return gamma * epsilon


def _splitBits(bits, index):
	zeroBit = list()
	oneBit = list()

	for j in range(len(bits)):
		if bits[j][index] == '0':
			zeroBit.append(bits[j])
		else:
			oneBit.append(bits[j])

	return zeroBit, oneBit


def _part2():
	f = _load_file()

	oxygenGenerator = list(map(lambda s: list(s.rstrip('\n')), f))
	c02Scrubber = list(oxygenGenerator)

	for i in range(len(oxygenGenerator[0])):
		if len(oxygenGenerator) > 1:
			zeroBit, oneBit = _splitBits(oxygenGenerator, i)
			oxygenGenerator = oneBit if len(oneBit) >= len(zeroBit) else zeroBit
		if len(c02Scrubber) > 1:
			zeroBit, oneBit = _splitBits(c02Scrubber, i)
			c02Scrubber = zeroBit if len(zeroBit) <= len(oneBit) else oneBit

	return _toNumber(oxygenGenerator[0]) * _toNumber(c02Scrubber[0])


def main():
	return _part1(), _part2()
