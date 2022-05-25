from unittest import mock
from unittest.mock import MagicMock

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget

from src.bugsweeper import MainWindow


def test_get_surrounding():
    with mock.patch("src.bugsweeper.MainWindow.update_status") as mocked_update_status:
        with mock.patch("src.bugsweeper.MainWindow.reset_map") as mocked_reset_map:
            with mock.patch("src.bugsweeper.MainWindow.show") as mocked_show:
                app = QApplication([])
                with mock.patch("src.bugsweeper.MainWindow.init_map") as mocked_init_map:
                    window = MainWindow()

                # Rather tedious right now
                hb = QHBoxLayout()
                vb = QVBoxLayout()
                vb.addLayout(hb)
                w = QWidget()
                window.create_grid(vb, w)
                window.init_map()

    assert len(window.get_surrounding(0, 0)) == 4  # it is a corner
    assert len(window.get_surrounding_old(0, 0)) == 4  # it is a corner
    assert len(window.get_surrounding(0, 0)) == 4  # it is a corner
    assert len(window.get_surrounding_2d(0, 0)) == 4  # it is a corner
