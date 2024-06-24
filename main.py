from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# create app
app = QApplication(sys.argv)

# create window
window = QWidget()
# set window title
window.setWindowTitle("PyQt5")
# set window size
window.resize(800, 600)
# set window geometry
window.move(800, 600)
# show window


window.show()


## main loop
app.exec_()