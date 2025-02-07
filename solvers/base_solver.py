from sudoku import Sudoku


class BaseSolver:
    def __init__(self, sudoku: Sudoku):
        self._sudoku = sudoku

    def run(self):
        raise NotImplemented('run not implemented')
