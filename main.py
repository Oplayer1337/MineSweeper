from random import randint


class Board:
    def __init__(self, size: int, difficulty: float):
        self.size = size
        self.board: list[list[int]] = []
        for row in range(size):
            self.board.append([])
            for col in range(size):
                self.board[row].append(0)

        self.mines_amount: int = int(size * size * difficulty)
        self.place_mines()

    def place_mines(self):
        currently_placed: int = 0
        while currently_placed < self.mines_amount:
            row: int = randint(0, self.size - 1)
            col: int = randint(0, self.size - 1)
            if self.board[row][col] == 1:
                continue
            else:
                self.board[row][col] = 1
                currently_placed += 1

    def debug_board(self):
        print('Current Board:')
        for row in self.board:
            print(row)
        print()


class Game:

    def __init__(self, board: Board):
        self.clicks: int = 0
        self.player_board: list[list[int]] = list()
        self.board = board.board
        self.size = board.size
        for row in range(board.size):
            self.player_board.append([])
            for col in range(board.size):
                self.player_board[row].append(-1)

    def click(self, x: int, y: int):

        # Edge case when player picks mine with first click
        if self.clicks == 0:
            if self.board[x][y] == 1:
                while True:
                    row: int = randint(0, self.size - 1)
                    col: int = randint(0, self.size - 1)
                    if self.board[row][col] == 1:
                        continue
                    else:
                        self.board[row][col] = 1
                        break
                self.board[x][y] = 0
                self.clicks += 1

    def debug_board(self):
        print('Current Player view:')
        for row in self.player_board:
            print(row)
        print()


def main():
    board = Board(5, 0.2)
    game = Game(board)
    board.debug_board()
    game.click(0, 1)
    board.debug_board()
    return ()


if __name__ == '__main__':
    main()
