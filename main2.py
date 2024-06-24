from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# create app
app = QApplication(sys.argv)

# create window
window = QWidget()
# set window title
window.setWindowTitle("Hello PyQt5")
# set window size
window.resize(800, 600)

# create button
btn = QPushButton('Click me', window)
# set button position
btn.move(0, 0)
# set button size
btn.resize(150, 60)
# set button text
btn.setToolTip("This is a <b>QPushButton</b> widget")

# set button function
def button_pressed():
    print("button pressed")

# connect button to function
btn.clicked.connect(button_pressed)




window.show()


## main loop
app.exec_()