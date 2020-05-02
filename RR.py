# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsSimpleTextItem

import FullProject




class Ui_Form4(object):

    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.resize(783, 535)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form4.setFont(font)
        Form4.setStyleSheet("background:url(:/img/blue_wallpaper.jpg);")
        self.label = QtWidgets.QLabel(Form4)
        self.label.setGeometry(QtCore.QRect(30, 10, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;  \n"
"")
        self.label.setObjectName("label")
        self.EnterProcessNo_btn = QtWidgets.QPushButton(Form4)

        self.EnterProcessNo_btn.setGeometry(QtCore.QRect(580, 100, 91, 31))
        self.EnterProcessNo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.EnterProcessNo_btn.setObjectName("EnterProcessNo_btn")
        self.WaitingTime_display = QtWidgets.QLCDNumber(Form4)
        self.WaitingTime_display.setGeometry(QtCore.QRect(320, 340, 111, 31))
        self.WaitingTime_display.setStyleSheet("border-color:#ff00ff;\n"
"color: #ff00ff;background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.WaitingTime_display.setObjectName("WaitingTime_display")
        self.ProcessNoText = QtWidgets.QLineEdit(Form4)
        self.ProcessNoText.setGeometry(QtCore.QRect(390, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessNoText.setFont(font)
        self.ProcessNoText.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.ProcessNoText.setObjectName("ProcessNoText")
        self.label_2 = QtWidgets.QLabel(Form4)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.label_2.setObjectName("label_2")
        self.graphicsView_FCFS = QtWidgets.QGraphicsView(Form4)
        self.graphicsView_FCFS.setGeometry(QtCore.QRect(30, 390, 731, 111))
        self.graphicsView_FCFS.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.graphicsView_FCFS.setObjectName("graphicsView_FCFS")
        self.EnterProcessInfo_btn = QtWidgets.QPushButton(Form4)
        self.EnterProcessInfo_btn.clicked.connect(self.RRProcessInfoenter)
        self.EnterProcessInfo_btn.setGeometry(QtCore.QRect(670, 190, 91, 31))
        self.EnterProcessInfo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.EnterProcessInfo_btn.setObjectName("EnterProcessInfo_btn")
        self.ProcessID_text = QtWidgets.QLineEdit(Form4)
        self.ProcessID_text.setGeometry(QtCore.QRect(20, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessID_text.setFont(font)
        self.ProcessID_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.ProcessID_text.setObjectName("ProcessID_text")
        self.ProcessBurst_text = QtWidgets.QLineEdit(Form4)
        self.ProcessBurst_text.setGeometry(QtCore.QRect(440, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessBurst_text.setFont(font)
        self.ProcessBurst_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.ProcessBurst_text.setObjectName("ProcessBurst_text")
        self.ProcessArrival_text = QtWidgets.QLineEdit(Form4)
        self.ProcessArrival_text.setGeometry(QtCore.QRect(230, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessArrival_text.setFont(font)
        self.ProcessArrival_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.ProcessArrival_text.setObjectName("ProcessArrival_text")
        self.label_3 = QtWidgets.QLabel(Form4)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.label_3.setObjectName("label_3")
        self.Home_btn = QtWidgets.QPushButton(Form4)
        self.Home_btn.clicked.connect(self.RRsimulation)
        self.Home_btn.setGeometry(QtCore.QRect(680, 90, 75, 71))
        self.Home_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_btn.setIcon(icon)
        self.Home_btn.setIconSize(QtCore.QSize(80, 80))
        self.Home_btn.setObjectName("Home_btn")
        self.ProcessNoText_2 = QtWidgets.QLineEdit(Form4)
        self.ProcessNoText_2.setGeometry(QtCore.QRect(90, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessNoText_2.setFont(font)
        self.ProcessNoText_2.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.ProcessNoText_2.setObjectName("ProcessNoText_2")
        self.EnterProcessNo_btn_2 = QtWidgets.QPushButton(Form4)
        self.EnterProcessNo_btn_2.clicked.connect(self.RR_onclick)
        self.EnterProcessNo_btn_2.setGeometry(QtCore.QRect(280, 100, 91, 31))
        self.EnterProcessNo_btn_2.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#ff00ff;\n"
"color: #ff00ff;")
        self.EnterProcessNo_btn_2.setObjectName("EnterProcessNo_btn_2")

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form4", "Form4"))
        self.label.setText(_translate("Form4", "          Round Robin( RR )"))
        self.EnterProcessNo_btn.setText(_translate("Form4", "Enter"))
        self.ProcessNoText.setPlaceholderText(_translate("Form4", "     Enter Time Quantum"))
        self.label_2.setText(_translate("Form4", " Average Wating Time"))
        self.EnterProcessInfo_btn.setText(_translate("Form4", "Enter"))
        self.ProcessID_text.setPlaceholderText(_translate("Form4", "        Enter  Process ID"))
        self.ProcessBurst_text.setPlaceholderText(_translate("Form4", "        Enter Burst Time"))
        self.ProcessArrival_text.setPlaceholderText(_translate("Form4", "       Enter Arrival Time"))
        self.label_3.setText(_translate("Form4", "   Gantt Chart "))
        self.ProcessNoText_2.setPlaceholderText(_translate("Form4", "  Enter Number of Process"))
        self.EnterProcessNo_btn_2.setText(_translate("Form4", "Enter"))


    def RR_onclick(self):
        processnum = int(self.ProcessNoText_2.text())
        FullProject.RR_create(processnum)


    def RRProcessInfoenter(self):
        ProcessID = int(self.ProcessID_text.text())
        self.ProcessID_text.setText("")
        ArrivalTime = int(self.ProcessArrival_text.text())
        self.ProcessArrival_text.setText("")
        BurstTime = int(self.ProcessBurst_text.text())
        self.ProcessBurst_text.setText("")
        PList = FullProject.RR_input(ProcessID, ArrivalTime, BurstTime)
        print("OK\n")

    def RRsimulation(self):
        burst = int(self.ProcessNoText.text())
        arr2 = FullProject.GChart
        average = FullProject.RR(int(self.ProcessNoText.text()), int(self.ProcessNoText_2.text()))
        self.WaitingTime_display.display(average)
        arr = FullProject.RRdepart
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_FCFS.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        brush = QtGui.QBrush(QtCore.Qt.lightGray)

        n = len(arr)
        next = 0
        for i in range(n):
            if burst < 5:
                m = 5 * burst
            else:
                m = burst
            print(m)
            if i == 0:
                r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF( m * burst, 80))
                scene.addRect(r, pen, brush)
                next = r.right()
                mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                scene.addItem(mytext1)
                mytext1.setPos((next - burst - 18), 30)
                mytext1.setScale(1.5)

                mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                scene.addItem(mytext2)
                mytext2.setPos(m * burst , 85)
                mytext2.setScale(1.3)
            else:
                r = QtCore.QRectF(QtCore.QPointF(next, 0), QtCore.QSizeF( m * burst, 80))
                scene.addRect(r, pen, brush)
                mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                scene.addItem(mytext1)
                mytext1.setPos(burst + next, 30)
                mytext1.setScale(1.5)
                mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                scene.addItem(mytext2)
                mytext2.setPos(m * burst + next, 85)
                mytext2.setScale(1.3)
                next = r.right()


import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form4 = QtWidgets.QMainWindow()
    ui = Ui_Form4()
    ui.setupUi(Form4)
    Form4.show()
    sys.exit(app.exec_())
