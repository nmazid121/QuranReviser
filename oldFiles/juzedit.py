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


    def ratingSelected(self):
        selected_item = self.listWidget.currentItem()
        if self.perfectRadio.isChecked():
            juz_num = int(selected_item.text().split()[-1])
            juzNumber_dictionary[f'Juz {juz_num}'] = 100
            print(f' The Juz {juz_num}' + f': {juzNumber_dictionary[f"Juz {juz_num}"]}')
        elif self.goodRadio.isChecked():
            juz_num = int(selected_item.text().split()[-1])
            juzNumber_dictionary[f'Juz {juz_num}'] = 75
            print(f'The Juz {juz_num}' + f': {juzNumber_dictionary[f"Juz {juz_num}"]}')
        elif self.okayRadio.isChecked():
            juz_num = int(selected_item.text().split()[-1])
            juzNumber_dictionary[f'Juz {juz_num}'] = 50
            print(f'The Juz {juz_num}' + f': {juzNumber_dictionary[f"Juz {juz_num}"]}')
        elif self.notAvailableRadio.isChecked():
            juz_num = int(selected_item.text().split()[-1])
            juzNumber_dictionary[f'Juz {juz_num}'] = 0
            print(f'The Juz {juz_num}' + f': {juzNumber_dictionary[f"Juz {juz_num}"]}')

            
# storing the data for the juz
juzNumber_dictionary = {
        'Juz 1': 10,
        'Juz 2': 0,
        'Juz 3': 0,
        'Juz 4': 0,
        'Juz 5': 0,
        'Juz 6': 0,
        'Juz 7': 0,
        'Juz 8': 0,
        'Juz 9': 0,
        'Juz 10': 0,
        'Juz 11': 0,
        'Juz 12': 0,
        'Juz 13': 0,
        'Juz 14': 0,
        'Juz 15': 0,
        'Juz 16': 0,
        'Juz 17': 0,
        'Juz 18': 0,
        'Juz 19': 0,
        'Juz 20': 0,
        'Juz 21': 0,
        'Juz 22': 0,
        'Juz 23': 0,
        'Juz 24': 0,
        'Juz 25': 0,
        'Juz 26': 0,
        'Juz 27': 0,
        'Juz 28': 0,
        'Juz 29': 0,
        'Juz 30': 0
    }
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    juzEditWindow = QtWidgets.QDialog()
    ui = Ui_juzEditWindow()
    ui.setupUi(juzEditWindow)
    juzEditWindow.show()
    sys.exit(app.exec_())
