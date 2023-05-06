from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import Qt

class Ui_juzEditWindow(object):
    def setupUi(self, juzEditWindow):
        juzEditWindow.setObjectName("juzEditWindow")
        juzEditWindow.resize(598, 555)
        font = QtGui.QFont()
        font.setPointSize(8)
        juzEditWindow.setFont(font)
        juzEditWindow.setSizeGripEnabled(False)
        juzEditWindow.setModal(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(juzEditWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 271, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(juzEditWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 190, 160, 107))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.perfectRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.perfectRadio.setFont(font)
        self.perfectRadio.setObjectName("perfectRadio")
        self.verticalLayout_2.addWidget(self.perfectRadio)
        self.goodRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.goodRadio.setFont(font)
        self.goodRadio.setObjectName("goodRadio")
        self.verticalLayout_2.addWidget(self.goodRadio)
        self.okayRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okayRadio.setFont(font)
        self.okayRadio.setObjectName("okayRadio")
        self.verticalLayout_2.addWidget(self.okayRadio)
        self.notAvailableRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.notAvailableRadio.setFont(font)
        self.notAvailableRadio.setObjectName("notAvailableRadio")
        self.verticalLayout_2.addWidget(self.notAvailableRadio)
        self.actiontest = QtWidgets.QAction(juzEditWindow)
        self.actiontest.setObjectName("actiontest")

        icon = QIcon('C:/Users/noobd/Documents/GitHub/QuranReviser/quranIcon.PNG')
        juzEditWindow.setWindowIcon(icon) # icon top left
        juzEditWindow.setWindowTitle('JuzEditor') # name of the window

        # adds functionality to the buttons, when clicked the rating is set
        self.perfectRadio.toggled.connect(lambda: self.setRating("Perfect"))
        self.goodRadio.toggled.connect(lambda: self.setRating("Good"))
        self.okayRadio.toggled.connect(lambda: self.setRating("Okay"))
        self.notAvailableRadio.toggled.connect(lambda: self.setRating("N/A"))

        # in order to see in the terminal 
        self.perfectRadio.clicked.connect(self.ratingSelected)
        self.goodRadio.clicked.connect(self.ratingSelected)
        self.okayRadio.clicked.connect(self.ratingSelected)
        self.notAvailableRadio.clicked.connect(self.ratingSelected)

        self.retranslateUi(juzEditWindow)
        QtCore.QMetaObject.connectSlotsByName(juzEditWindow)

    def retranslateUi(self, juzEditWindow):
        _translate = QtCore.QCoreApplication.translate
        juzEditWindow.setWindowTitle(_translate("juzEditWindow", "JuzEditor"))
        self.label.setText(_translate("juzEditWindow", "Juz Editor"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("juzEditWindow", "Juz 1"))
        itemTwo = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(itemTwo)
        itemTwo.setText(_translate("juzEditWindow", "Juz 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("juzEditWindow", "Reviews :"))
        self.perfectRadio.setText(_translate("juzEditWindow", "Perfect"))
        self.goodRadio.setText(_translate("juzEditWindow", "Good"))
        self.okayRadio.setText(_translate("juzEditWindow", "Okay"))
        self.notAvailableRadio.setText(_translate("juzEditWindow", "N/A"))
        self.actiontest.setText(_translate("juzEditWindow", "test"))

    def setRating(self, rating):
        # get the selected item in the list
        selected = self.listWidget.currentItem()

        if selected is not None:
            # set the rating as the item data
            selected.setData(Qt.UserRole, rating)

    def ratingSelected(self):
        selected_item = self.listWidget.currentItem()
        selected_rating = None
        if self.perfectRadio.isChecked():
            selected_rating = 100
        elif self.goodRadio.isChecked():
            selected_rating = 75
        elif self.okayRadio.isChecked():
            selected_rating = 50
        elif self.notAvailableRadio.isChecked():
            selected_rating = 0
        if selected_item is not None and selected_rating is not None:
            print(f"{selected_item.text()} : {selected_rating}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    juzEditWindow = QtWidgets.QDialog()
    ui = Ui_juzEditWindow()
    ui.setupUi(juzEditWindow)
    juzEditWindow.show()
    sys.exit(app.exec_())
