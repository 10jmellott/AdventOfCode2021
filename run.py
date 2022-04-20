"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from src import day09

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
test(day09.main, "Day 9: Smoke Basin")
