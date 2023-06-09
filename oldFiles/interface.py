from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import Qt
from juzedit import Ui_juzEditWindow, juzNumber_dictionary

class Ui_interfaceWindow(object):
    def setupUi(self, interfaceWindow):
        interfaceWindow.setObjectName("interfaceWindow")
        interfaceWindow.resize(1122, 875)
        font = QtGui.QFont()
        font.setPointSize(1)
        interfaceWindow.setFont(font)
        interfaceWindow.setSizeGripEnabled(False)
        interfaceWindow.setModal(False)
        # adding a new button
        self.pushButton_two = QtWidgets.QPushButton(interfaceWindow)
        self.pushButton_two.clicked.connect(self.update_juz_percentages)
        self.pushButton_two.setGeometry(QtCore.QRect(800, 90, 75, 23))
        font_two = QtGui.QFont()
        font_two.setPointSize(8)
        self.pushButton_two.setFont(font_two)
        self.pushButton_two.setObjectName("pushButton_two")

        self.buttonBox = QtWidgets.QDialogButtonBox(interfaceWindow)
        self.buttonBox.setGeometry(QtCore.QRect(900, 760, 156, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(interfaceWindow)
        self.label.setGeometry(QtCore.QRect(630, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(interfaceWindow)
        self.scrollArea.setGeometry(QtCore.QRect(630, 120, 421, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setLineWidth(5)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 402, 609))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 22))
        self.progressBar.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
       # self.update_juz_percentages()
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(interfaceWindow, clicked = lambda: self.openJuzEditor())
        self.pushButton.setGeometry(QtCore.QRect(700, 90, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.actiontest = QtWidgets.QAction(interfaceWindow)
        self.actiontest.setObjectName("actiontest")

        # added the icon and top right window min, max, and close
        icon = QIcon('C:/Users/noobd/Documents/GitHub/QuranReviser/quranIcon.PNG')
        interfaceWindow.setWindowIcon(icon) # icon top left
        interfaceWindow.setWindowTitle('QuranRevisor') # name of the window
        interfaceWindow.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.retranslateUi(interfaceWindow)
        self.buttonBox.accepted.connect(interfaceWindow.accept) # type: ignore
        self.buttonBox.rejected.connect(interfaceWindow.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(interfaceWindow)

    def retranslateUi(self, interfaceWindow):
        _translate = QtCore.QCoreApplication.translate
        interfaceWindow.setWindowTitle(_translate("interfaceWindow", "QuranEditor"))
        self.label.setText(_translate("interfaceWindow", "Juz :"))
        self.label_2.setText(_translate("interfaceWindow", "Juz 1"))
        self.pushButton.setText(_translate("interfaceWindow", "Edit Juz"))
        self.pushButton_two.setText(_translate("interaceWindow", "Update"))
        self.actiontest.setText(_translate("interfaceWindow", "test"))
    
    # Function to open the window
    def openJuzEditor(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_juzEditWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    # Update the progress bar
    def update_juz_percentages(self):
        self.progressBar.setValue(juzNumber_dictionary["Juz 1"])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaceWindow = QtWidgets.QDialog()
    ui = Ui_interfaceWindow()
    ui.setupUi(interfaceWindow)
    interfaceWindow.show()
    sys.exit(app.exec_())
