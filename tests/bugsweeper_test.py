from unittest import mock

import pytest
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget

from src.bugsweeper import MainWindow


@pytest.mark.parametrize("x,y, expected", [(0, 0, 4), (4, 4, 9), (15, 15, 4), (0, 4, 6)])
def test_get_surrounding(x, y, expected):
    # Rather tedious right now
    with mock.patch("src.bugsweeper.MainWindow.update_status") as mocked_update_status:
        with mock.patch("src.bugsweeper.MainWindow.reset_map") as mocked_reset_map:
            with mock.patch("src.bugsweeper.MainWindow.show") as mocked_show:
                app = QApplication([])
                with mock.patch("src.bugsweeper.MainWindow.init_map") as mocked_init_map:
                    window = MainWindow()

                hb = QHBoxLayout()
                vb = QVBoxLayout()
                vb.addLayout(hb)
                w = QWidget()
                window.create_grid(vb, w)
                window.init_map()

    assert len(window.get_surrounding(y, x)) == expected
