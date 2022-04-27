"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from src import day10

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
test(day10.main, "Day 10: Syntax Scoring")
