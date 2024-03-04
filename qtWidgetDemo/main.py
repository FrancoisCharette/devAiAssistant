#
# this is a developement/test for developing widgets
#

from PyQt6.QtWidgets import QApplication, QWidget
from ui.main_gui_ui import Ui_widgetDemo
import sys

sys.path.append('.')

class myApp(QWidget):

  def __init__(self):
    QWidget.__init__(self)
    self.ui = Ui_widgetDemo
    self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window')
