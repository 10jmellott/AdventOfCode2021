def parse_segment(line):
	parts = line.split('|')
	inputSegments = list(map(list, parts[0].strip().split(' ')))
	outputSegments = list(map(list, parts[1].strip().split(' ')))
	return inputSegments, outputSegments

def _load_segments():
	# Open the file in read-only mode
	f = open('data/08.txt', 'r')
	return list(map(parse_segment, f))


def _part1():
	segments = _load_segments()
	uniqueOutputDigits = 0
	for segment in segments:
		for outputSegment in segment[1]:
			n = len(outputSegment)
			if n == 2 or n == 3 or n == 4 or n == 7:
				uniqueOutputDigits = uniqueOutputDigits + 1
	return uniqueOutputDigits

# _part2 was a ton of paper-work to figure out some of the
# contraint propogation rules for each digit segment
def _part2():
	segments = _load_segments()
	totalSegmentValue = 0
	for segment in segments:
		segmentMapping = {}
		for outputSegment in segment[0]:
			outputSegment.sort()
			n = len(outputSegment)
			digits = list()
			if n == 2:
				digits.append(1)
			elif n == 3:
				digits.append(7)
			elif n == 4:
				digits.append(4)
			elif n == 7:
				digits.append(8)
			elif n == 5:
				digits.append(2)
				digits.append(3)
				digits.append(5)
			elif n == 6:
				digits.append(0)
				digits.append(6)
				digits.append(9)

			for digit in digits:
				digitList = [] if not digit in segmentMapping else segmentMapping[digit]
				digitList.append(list(outputSegment))
				segmentMapping[digit] = digitList

		# Known digit lengths w/o calculation
		digitMapping = {
			1: segmentMapping[1][0],
			4: segmentMapping[4][0],
			7: segmentMapping[7][0],
			8: segmentMapping[8][0]
		}

		# Map 9
		for option in segmentMapping[9]:
			mapped = 0
			for value in option:
				if value in digitMapping[7] or value in digitMapping[4]:
					mapped += 1
			if mapped == 5:
				digitMapping[9] = option

		# Map 0
		for option in segmentMapping[0]:
			mapped = 0
			for value in option:
				if value in digitMapping[1]:
					mapped += 1
			if mapped == 2:
				mapped = 0
				for value in option:
					if value in digitMapping[9]:
						mapped += 1
				if mapped == 5:
					digitMapping[0] = option

		# Map 6
		for option in segmentMapping[6]:
			if option != digitMapping[0] and option != digitMapping[9]:
				digitMapping[6] = option

		# Map 'e' - lower left segment
		eMapping = None
		for seg in digitMapping[6]:
			if seg not in digitMapping[9]:
				eMapping = seg
		# Map 'c' - upper right segment
		cMapping = None
		for seg in digitMapping[9]:
			if seg not in digitMapping[6]:
				cMapping = seg

		# Map the remaining using the individual segment mapping
		digitMapping[2] = list(filter(lambda mapping: eMapping in mapping, segmentMapping[2]))[0]
		digitMapping[5] = list(filter(lambda mapping: cMapping not in mapping, segmentMapping[5]))[0]
		digitMapping[3] = list(filter(lambda mapping: mapping != digitMapping[2] and mapping != digitMapping[5], segmentMapping[3]))[0]

		# Simple digit concatenation
		value = 0
		for outputSegment in segment[1]:
			outputSegment.sort()
			value = value * 10
			for digit in digitMapping:
				if outputSegment == digitMapping[digit]:
					value += digit
		totalSegmentValue += value
	return totalSegmentValue


def main():
	return _part1(), _part2()
