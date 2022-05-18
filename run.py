"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from src import day11

def test(f, message):
	timer = stopwatch.Timer()
	timer.start()
	ret = f()
	timer.stop()
	print(message)
	if ret:
		print(f'  Solution: {ret}')
	print(f'  Elapsed: {timer.elapsed()}')
	print()

print('Advent of Code 2021 - https://adventofcode.com/2021')
print('----------------------------------------------')
print()
test(day11.main, "Day 11: Dumbo Octopus")
