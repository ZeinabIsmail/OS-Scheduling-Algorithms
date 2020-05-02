# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from FCFS import Ui_Form1
from SJFpre import Ui_Form2
from piriortyNon import Ui_Form
from piriortyPre import Ui_Form3
from RR import Ui_Form4
from SJFnon import Ui_Form6
import FullProject


class Ui_MainWindow(object):
    def FCFSwindow(self):
        self.form1 = QtWidgets.QMainWindow()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.form1)
        self.form1.show()

    def SJFprewindow(self):
        self.form2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.form2)
        self.form2.show()

    def SJFnonwindow(self):
        self.form6 = QtWidgets.QMainWindow()
        self.ui = Ui_Form6()
        self.ui.setupUi(self.form6)
        self.form6.show()

    def PriononWindow(self):
        self.form = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self.form.show()

    def Prioprewindow(self):
        self.form3 = QtWidgets.QMainWindow()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.form3)
        self.form3.show()

    def RRwindow(self):
        self.form4 = QtWidgets.QMainWindow()
        self.ui = Ui_Form4()
        self.ui.setupUi(self.form4)
        self.form4.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 557)
        font = QtGui.QFont()
        font.setPointSize(25)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet("background:url(:/img/blue_wallpaper.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fcfsMain = QtWidgets.QPushButton(self.centralwidget)
        self.fcfsMain.setEnabled(True)
        self.fcfsMain.clicked.connect(self.FCFSwindow)
        self.fcfsMain.setGeometry(QtCore.QRect(310, 70, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.fcfsMain.setFont(font)
        self.fcfsMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.fcfsMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#aa007f;\n"
" text-align: left;\n"
"color: #aa007f;  \n"
"")
        self.fcfsMain.setIconSize(QtCore.QSize(49, 117))
        self.fcfsMain.setCheckable(True)
        self.fcfsMain.setChecked(False)
        self.fcfsMain.setAutoDefault(False)
        self.fcfsMain.setDefault(False)
        self.fcfsMain.setFlat(False)
        self.fcfsMain.setObjectName("fcfsMain")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 170, 255); ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 80, 71, 41))
        self.label_2.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#aa007f;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/icon3.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_no1 = QtWidgets.QLabel(self.centralwidget)
        self.label_no1.setGeometry(QtCore.QRect(210, 70, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no1.setFont(font)
        self.label_no1.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#aa007f;\n"
"color:#aa007f;\n"
"")
        self.label_no1.setObjectName("label_no1")
        self.label_no2 = QtWidgets.QLabel(self.centralwidget)
        self.label_no2.setGeometry(QtCore.QRect(110, 140, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no2.setFont(font)
        self.label_no2.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#55aaff;\n"
"color:#55aaff;\n"
"")
        self.label_no2.setObjectName("label_no2")
        self.sjfPreMain = QtWidgets.QPushButton(self.centralwidget)
        self.sjfPreMain.setEnabled(True)
        self.sjfPreMain.clicked.connect(self.SJFprewindow)
        self.sjfPreMain.setGeometry(QtCore.QRect(210, 140, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sjfPreMain.setFont(font)
        self.sjfPreMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.sjfPreMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
" text-align: left;\n"
"color: rgb(0, 170, 255);  \n"
" \n"
"")
        self.sjfPreMain.setIconSize(QtCore.QSize(49, 117))
        self.sjfPreMain.setCheckable(True)
        self.sjfPreMain.setChecked(False)
        self.sjfPreMain.setAutoDefault(False)
        self.sjfPreMain.setDefault(False)
        self.sjfPreMain.setFlat(False)
        self.sjfPreMain.setObjectName("sjfPreMain")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 150, 71, 41))
        self.label_5.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#55aaff;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/img/icon1.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_no3 = QtWidgets.QLabel(self.centralwidget)
        self.label_no3.setGeometry(QtCore.QRect(210, 210, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no3.setFont(font)
        self.label_no3.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ff0000;\n"
"color:#ff0000;\n"
"")
        self.label_no3.setObjectName("label_no3")
        self.sjfNonMain = QtWidgets.QPushButton(self.centralwidget)
        self.sjfNonMain.setEnabled(True)
        self.sjfNonMain.clicked.connect(self.SJFnonwindow)
        self.sjfNonMain.setGeometry(QtCore.QRect(310, 210, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.sjfNonMain.setFont(font)
        self.sjfNonMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.sjfNonMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff0000;\n"
" text-align: left;\n"
"color: #ff0000;  \n"
"\n"
"")
        self.sjfNonMain.setIconSize(QtCore.QSize(49, 117))
        self.sjfNonMain.setCheckable(True)
        self.sjfNonMain.setChecked(False)
        self.sjfNonMain.setAutoDefault(False)
        self.sjfNonMain.setDefault(False)
        self.sjfNonMain.setFlat(False)
        self.sjfNonMain.setObjectName("sjfNonMain")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 220, 71, 41))
        self.label_7.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ff0000;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/img/icon2.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_no4 = QtWidgets.QLabel(self.centralwidget)
        self.label_no4.setGeometry(QtCore.QRect(110, 280, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no4.setFont(font)
        self.label_no4.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ffaa00;\n"
"color:#ffaa00;\n"
"")
        self.label_no4.setObjectName("label_no4")
        self.piriortyPreMain = QtWidgets.QPushButton(self.centralwidget)
        self.piriortyPreMain.setEnabled(True)
        self.piriortyPreMain.clicked.connect(self.Prioprewindow)
        self.piriortyPreMain.setGeometry(QtCore.QRect(210, 280, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.piriortyPreMain.setFont(font)
        self.piriortyPreMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.piriortyPreMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ffaa00;\n"
" text-align: left;\n"
"color:#ffaa00;  \n"
" \n"
"")
        self.piriortyPreMain.setIconSize(QtCore.QSize(49, 117))
        self.piriortyPreMain.setCheckable(True)
        self.piriortyPreMain.setChecked(False)
        self.piriortyPreMain.setAutoDefault(False)
        self.piriortyPreMain.setDefault(False)
        self.piriortyPreMain.setFlat(False)
        self.piriortyPreMain.setObjectName("piriortyPreMain")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 290, 71, 41))
        self.label_9.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ffaa00;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/img/icon4.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_no5 = QtWidgets.QLabel(self.centralwidget)
        self.label_no5.setGeometry(QtCore.QRect(210, 350, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no5.setFont(font)
        self.label_no5.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#00aa00;\n"
"color:#00aa00;\n"
"")
        self.label_no5.setObjectName("label_no5")
        self.piriorityNonMain = QtWidgets.QPushButton(self.centralwidget)
        self.piriorityNonMain.setEnabled(True)
        self.piriorityNonMain.clicked.connect(self.PriononWindow)
        self.piriorityNonMain.setGeometry(QtCore.QRect(310, 350, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.piriorityNonMain.setFont(font)
        self.piriorityNonMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.piriorityNonMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
" text-align: left;\n"
"color:#00aa00;  \n"
"\n"
"")
        self.piriorityNonMain.setIconSize(QtCore.QSize(49, 117))
        self.piriorityNonMain.setCheckable(True)
        self.piriorityNonMain.setChecked(False)
        self.piriorityNonMain.setAutoDefault(False)
        self.piriorityNonMain.setDefault(False)
        self.piriorityNonMain.setFlat(False)
        self.piriorityNonMain.setObjectName("piriorityNonMain")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 360, 71, 41))
        self.label_11.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#00aa00;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/img/icon6.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_no6 = QtWidgets.QLabel(self.centralwidget)
        self.label_no6.setGeometry(QtCore.QRect(110, 420, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_no6.setFont(font)
        self.label_no6.setStyleSheet("background :url(:/img/button.png);\n"
" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ff00ff;\n"
"color:#ff00ff;\n"
"")
        self.label_no6.setObjectName("label_no6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 430, 71, 41))
        self.label_13.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#55aaff;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/img/icon3.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.rrMain = QtWidgets.QPushButton(self.centralwidget)
        self.rrMain.setEnabled(True)
        self.rrMain.clicked.connect(self.RRwindow)
        self.rrMain.setGeometry(QtCore.QRect(210, 420, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rrMain.setFont(font)
        self.rrMain.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rrMain.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
" text-align: left;\n"
"color: #ff00ff;  \n"
" ")
        self.rrMain.setIconSize(QtCore.QSize(49, 117))
        self.rrMain.setCheckable(True)
        self.rrMain.setChecked(False)
        self.rrMain.setAutoDefault(False)
        self.rrMain.setDefault(False)
        self.rrMain.setFlat(False)
        self.rrMain.setObjectName("rrMain")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(460, 430, 71, 41))
        self.label_14.setStyleSheet(" border: 3px solid ;\n"
"border-radius:10px;\n"
"border-color:#ff00ff;")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/img/icon5.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
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
        self.fcfsMain.setText(_translate("MainWindow", "   First Come First Serve (FCFS)"))
        self.label.setText(_translate("MainWindow", "CPU Scheduling Types"))
        self.label_no1.setText(_translate("MainWindow", "  1"))
        self.label_no2.setText(_translate("MainWindow", "  2"))
        self.sjfPreMain.setText(_translate("MainWindow", "     SJF Preemetive (SJF)"))
        self.label_no3.setText(_translate("MainWindow", "  3"))
        self.sjfNonMain.setText(_translate("MainWindow", " ShortestJopFirst Non-Premetive (SJF)"))
        self.label_no4.setText(_translate("MainWindow", "  4"))
        self.piriortyPreMain.setText(_translate("MainWindow", "Priority Preemetive"))
        self.label_no5.setText(_translate("MainWindow", "  5"))
        self.piriorityNonMain.setText(_translate("MainWindow", "Priority Non-Preemetive"))
        self.label_no6.setText(_translate("MainWindow", "  6"))
        self.rrMain.setText(_translate("MainWindow", " Round Robin( RR )"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
