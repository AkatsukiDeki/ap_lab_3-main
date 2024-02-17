# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_V2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Weather")
        MainWindow.setFixedSize(461, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_file = QtWidgets.QPushButton(self.centralwidget)
        self.main_file.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.main_file.setObjectName("pushButton")
        self.main_file.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_datae = QtWidgets.QPushButton(self.centralwidget)
        self.cut_datae.setGeometry(QtCore.QRect(170, 10, 121, 51))
        self.cut_datae.setObjectName("pushButton_2")
        self.cut_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_datae = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_datae.setGeometry(QtCore.QRect(230, 71, 60, 20))
        self.folder_for_datae.setObjectName("select_pushButton_2")
        self.folder_for_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_years = QtWidgets.QPushButton(self.centralwidget)
        self.cut_years.setGeometry(QtCore.QRect(330, 10, 121, 51))
        self.cut_years.setObjectName("pushButton_3")
        self.cut_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_years = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_years.setGeometry(QtCore.QRect(390, 71, 60, 20))
        self.folder_for_years.setObjectName("select_pushButton_3")
        self.folder_for_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.cut_weaks.setGeometry(QtCore.QRect(330, 100, 121, 51))
        self.cut_weaks.setObjectName("pushButton_4")
        self.cut_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_weaks.setGeometry(QtCore.QRect(390, 160, 60, 20))
        self.folder_for_weaks.setObjectName("select_pushButton_4")
        self.folder_for_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 121, 51))
        self.textEdit.setObjectName("textEdit")

        self.find_years = QtWidgets.QPushButton(self.centralwidget)
        self.find_years.setGeometry(QtCore.QRect(50, 180, 81, 21))
        self.find_years.setObjectName("pushButton_5")
        self.find_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)
        self.find_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.find_weaks.setGeometry(QtCore.QRect(50, 205, 81, 21))
        self.find_weaks.setObjectName("pushButton_5")
        self.find_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)
        self.find_datae = QtWidgets.QPushButton(self.centralwidget)
        self.find_datae.setGeometry(QtCore.QRect(50, 155, 81, 21))
        self.find_datae.setObjectName("pushButton_5")
        self.find_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(133, 90, 190, 100))
        self.label.setObjectName("label")
        self.label.setWordWrap(True)

        self.get_next = QtWidgets.QPushButton(self.centralwidget)
        self.get_next.setGeometry(QtCore.QRect(200, 170, 71, 21))
        self.get_next.setObjectName("get_text")
        self.get_next.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_file.setText(_translate("MainWindow", "Select main file"))

        self.folder_for_datae.setText(
            _translate("MainWindow", "add folder"))
        self.cut_datae.setText(_translate("MainWindow", "Cut by data/date"))

        self.folder_for_years.setText(
            _translate("MainWindow", "add folder"))
        self.cut_years.setText(_translate("MainWindow", "Cut by years"))

        self.cut_weaks.setText(_translate("MainWindow", "cut by weaks"))
        self.folder_for_weaks.setText(
            _translate("MainWindow", "add folder"))

        self.find_years.setText(_translate("MainWindow", "find in years"))
        self.find_weaks.setText(_translate("MainWindow", "find in weeks"))
        self.find_datae.setText(_translate("MainWindow", "find in data/e"))
        self.label.setText(_translate("MainWindow", ""))

        self.get_next.setText(_translate("MainWindow", "get_next"))
