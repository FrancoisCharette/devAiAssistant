#
# this is a developement/test for developing widgets
#

from PyQt6.QtWidgets import QApplication, QWidget
from ui.main_gui_ui import Ui_widgetDemo
import sys

sys.path.append('.')

class myApp(QWidget, Ui_widgetDemo):

  def __init__(self):
    super().__init__()
    self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window')
