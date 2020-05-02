# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SJFpre.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsSimpleTextItem

import FullProject





class Ui_Form2(object):

    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(783, 535)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form2.setFont(font)
        Form2.setStyleSheet("background:url(:/img/blue_wallpaper.jpg);")
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(30, 10, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;  \n"
"")
        self.label.setObjectName("label")
        self.EnterProcessNo_btn = QtWidgets.QPushButton(Form2)
        self.EnterProcessNo_btn.clicked.connect(self.no_onclick)
        self.EnterProcessNo_btn.setGeometry(QtCore.QRect(460, 100, 91, 31))
        self.EnterProcessNo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.EnterProcessNo_btn.setObjectName("EnterProcessNo_btn")
        self.WaitingTime_display = QtWidgets.QLCDNumber(Form2)
        self.WaitingTime_display.setGeometry(QtCore.QRect(320, 340, 111, 31))

        self.WaitingTime_display.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.WaitingTime_display.setObjectName("WaitingTime_display")
        self.ProcessNoText = QtWidgets.QLineEdit(Form2)
        self.ProcessNoText.setGeometry(QtCore.QRect(230, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessNoText.setFont(font)
        self.ProcessNoText.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.ProcessNoText.setObjectName("ProcessNoText")
        self.label_2 = QtWidgets.QLabel(Form2)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.label_2.setObjectName("label_2")
        self.graphicsView_FCFS = QtWidgets.QGraphicsView(Form2)
        self.graphicsView_FCFS.setGeometry(QtCore.QRect(30, 390, 731, 111))
        self.graphicsView_FCFS.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.graphicsView_FCFS.setObjectName("graphicsView_FCFS")
        self.EnterProcessInfo_btn = QtWidgets.QPushButton(Form2)
        self.EnterProcessInfo_btn.clicked.connect(self.ProcessInfoenter)
        self.EnterProcessInfo_btn.setGeometry(QtCore.QRect(670, 190, 91, 31))
        self.EnterProcessInfo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.EnterProcessInfo_btn.setObjectName("EnterProcessInfo_btn")
        self.ProcessID_text = QtWidgets.QLineEdit(Form2)
        self.ProcessID_text.setGeometry(QtCore.QRect(20, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessID_text.setFont(font)
        self.ProcessID_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.ProcessID_text.setObjectName("ProcessID_text")
        self.ProcessBurst_text = QtWidgets.QLineEdit(Form2)
        self.ProcessBurst_text.setGeometry(QtCore.QRect(440, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessBurst_text.setFont(font)
        self.ProcessBurst_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.ProcessBurst_text.setObjectName("ProcessBurst_text")
        self.ProcessArrival_text = QtWidgets.QLineEdit(Form2)
        self.ProcessArrival_text.setGeometry(QtCore.QRect(230, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessArrival_text.setFont(font)
        self.ProcessArrival_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.ProcessArrival_text.setObjectName("ProcessArrival_text")
        self.label_3 = QtWidgets.QLabel(Form2)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#55aaff;\n"
"color: #55aaff;")
        self.label_3.setObjectName("label_3")
        self.Home_btn = QtWidgets.QPushButton(Form2)
        self.Home_btn.clicked.connect(self.simulation)
        self.Home_btn.setGeometry(QtCore.QRect(680, 90, 75, 71))
        self.Home_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_btn.setIcon(icon)
        self.Home_btn.setIconSize(QtCore.QSize(80, 80))
        self.Home_btn.setObjectName("Home_btn")
        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Form2"))
        self.label.setText(_translate("Form2", "                Shortest Jop First Premetive (SJF)"))
        self.EnterProcessNo_btn.setText(_translate("Form2", "Enter"))
        self.ProcessNoText.setPlaceholderText(_translate("Form2", "Enter Number of Process"))
        self.label_2.setText(_translate("Form2", " Average Wating Time"))
        self.EnterProcessInfo_btn.setText(_translate("Form2", "Enter"))
        self.ProcessID_text.setPlaceholderText(_translate("Form2", "Enter  Process ID"))
        self.ProcessBurst_text.setPlaceholderText(_translate("Form2", " Enter Burst Time"))
        self.ProcessArrival_text.setPlaceholderText(_translate("Form2", " Enter Arrival Time"))
        self.label_3.setText(_translate("Form2", "Gantt Chart "))

    def no_onclick(self):
        process_number = int(self.ProcessNoText.text())
        FullProject.processCreate(process_number)

    def ProcessInfoenter(self):
        ProcessID = int(self.ProcessID_text.text())
        self.ProcessID_text.setText("")
        ArrivalTime = int(self.ProcessArrival_text.text())
        self.ProcessArrival_text.setText("")
        BurstTime = int(self.ProcessBurst_text.text())
        self.ProcessBurst_text.setText("")
        FullProject.pre_sjf_input(ProcessID, ArrivalTime, BurstTime)

    def simulation(self):
        FullProject.preemptive_sjf(int(self.ProcessNoText.text()))
        averagetime = FullProject.SJaveragetime(int(self.ProcessNoText.text()))
        print(averagetime)
        self.WaitingTime_display.display(averagetime)
        print(FullProject.SJprecurrent_running)
        arr2 = []
        lastdone = FullProject.SJprecurrent_running[0]
        arr2.append(lastdone)
        for i in range(len(FullProject.SJprecurrent_running)):
            if FullProject.SJprecurrent_running[i] != lastdone:
                arr2.append(FullProject.SJprecurrent_running[i])
                lastdone = FullProject.SJprecurrent_running[i]
        print(arr2)
        burst = []
        jstart = 0
        for i in range(len(arr2)):
            searchn = arr2[i]
            burstno = 0
            index = 0
            for j in range(jstart, len(FullProject.SJprecurrent_running)):
                if FullProject.SJprecurrent_running[j] == searchn:
                    burstno += 1
                else:
                    break
            jstart = jstart + burstno
            burst.append(burstno)
        print(burst)
        SJFdep = []
        depsum = 0
        for i in range(len(arr2)):
            depsum = depsum + burst[i]
            SJFdep.append(depsum)
        arr = SJFdep
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_FCFS.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        brush = QtGui.QBrush(QtCore.Qt.lightGray)
        print(arr)
        print(arr2)
        print(burst)
        n = len(arr)
        next = 0
        for i in range(n):
            if burst[i] < 3:
                m = 20 * burst[i]
            elif burst[i] < 5:
                m = 10 * burst[i]
            else:
                m = burst[i]
            if i == 0:
                r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(m * burst[i], 80))
                scene.addRect(r, pen, brush)
                next = r.right()
                mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                scene.addItem(mytext1)
                mytext1.setPos((next - burst[i] - 18), 30)
                mytext1.setScale(1.5)
                mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                scene.addItem(mytext2)
                mytext2.setPos(m * burst[i], 85)
                mytext2.setScale(1.3)
            else:
                r = QtCore.QRectF(QtCore.QPointF(next, 0), QtCore.QSizeF(m * burst[i], 80))
                scene.addRect(r, pen, brush)
                mytext1 = QGraphicsSimpleTextItem(str(arr2[i]))
                scene.addItem(mytext1)
                mytext1.setPos(burst[i] + next, 30)
                mytext1.setScale(1.5)
                mytext2 = QGraphicsSimpleTextItem(str(arr[i]))
                scene.addItem(mytext2)
                mytext2.setPos(m * burst[i] + next, 85)
                mytext2.setScale(1.3)
                next = r.right()
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QMainWindow()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
