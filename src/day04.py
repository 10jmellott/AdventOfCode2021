def _load_file():
	# Open the file in read-only mode
	return open('data/04.txt', 'r')


def _parseFile(f):
	bingoSubsystem = list(map(lambda l: int(l), f.readline().split(',')))
	bingoBoards = list()
	lines = f.readlines()
	for i in range(int(len(lines) / 6)):
		start = int(i * 6 + 1)
		end = start + 5
		board = list(map(lambda line: list(map(lambda j: int(line[j * 3] + line[j * 3 + 1]), range(5))), lines[start:end]))
		bingoBoards.append(board)
	return bingoSubsystem, bingoBoards

def _findWinningMove(bingoSubsystem, board):
	boardMoveMap = list(map(lambda i: list(
		map(lambda j: bingoSubsystem.index(board[i][j]), range(5))), range(5)))
	boardWinningMove = 1000
	for i in range(5):
		if all(map(lambda j: boardMoveMap[i][j] >= 0, range(5))):
			maxMove = max(boardMoveMap[i])
			if maxMove < boardWinningMove:
				boardWinningMove = maxMove
		if all(map(lambda j: boardMoveMap[j][i] >= 0, range(5))):
			maxMove = max(map(lambda j: boardMoveMap[j][i], range(5)))
			if maxMove < boardWinningMove:
				boardWinningMove = maxMove
	return boardWinningMove

def _getScore(bingoSubsystem, move, board):
	validMoves = bingoSubsystem[:move+1]
	lastMove = validMoves[len(validMoves) - 1]
	return sum(map(lambda i: sum(map(lambda j: 0 if board[i][j] in validMoves else board[i][j], range(5))), range(5))) * lastMove

def _part1():
	f = _load_file()
	bingoSubsystem, bingoBoards = _parseFile(f)
	winningBoard = None
	winningMove = 1000
	for board in bingoBoards:
		boardWinningMove = _findWinningMove(bingoSubsystem, board)
		if boardWinningMove < winningMove:
			winningBoard = board
			winningMove = boardWinningMove
	return _getScore(bingoSubsystem, winningMove, winningBoard)

def _part2():
	f = _load_file()
	bingoSubsystem, bingoBoards = _parseFile(f)
	winningBoard = None
	winningMove = -1
	for board in bingoBoards:
		boardWinningMove = _findWinningMove(bingoSubsystem, board)
		if boardWinningMove > winningMove:
			winningBoard = board
			winningMove = boardWinningMove
	return _getScore(bingoSubsystem, winningMove, winningBoard)


def main():
	return _part1(), _part2()
