from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

Form, Window = uic.loadUiType('interface.ui')
# one instance of QApplication is required in every PyQt app that is made
app = QApplication([]) # [] represent the command line arguments that are passed to the app

# labels are used to show text on the GUI

# .show() actually puts the information on the GUI

window = Window()
form = Form()
form.setupUi(window)


icon = QIcon('C:/Users/noobd/Documents/GitHub/QuranReviser/quranIcon.PNG')
window.setWindowIcon(icon) # icon top left
window.setWindowTitle('QuranRevisor') # name of the window
window.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint) # formatting min, max, and close window


progress_bar = form.testText
progress_bar.setStyleSheet('QProgressBar::chunk { background-color: red; }')


#
window.show()
app.exec()
 # this command takes the app and runs the method exec() which runs the app until the user presses the X
