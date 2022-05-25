from functools import wraps
from time import time
from unittest.mock import MagicMock

from src.bugsweeper import MainWindow


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")

    return _time_it


@measure
def test_get_surrounding():
    window = MainWindow.__init__ = MagicMock()
    board_mock = window()
    board_mock.board_size = 5
    board_mock.get_surrounding = MainWindow.get_surrounding

    assert len(board_mock.get_surrounding(board_mock, 0, 0)) == 4  # it is a corner
