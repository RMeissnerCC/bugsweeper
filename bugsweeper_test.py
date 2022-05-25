from unittest.mock import MagicMock

from minesweeper import MainWindow


def test_get_surrounding():
    window = MainWindow.__init__ = MagicMock()
    board_mock = window()
    board_mock.board_size = 5
    board_mock.get_surrounding = MainWindow.get_surrounding

    assert len(board_mock.get_surrounding(board_mock, 0, 0)) == 4 # it is a corner
