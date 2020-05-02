from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import image_rc
import SJF_Algorithem1

AllProcessInfo = []
process_data_fit = []

class Ui_Form6(object):

    def setupUi(self, Form6):
        Form6.setObjectName("Form6")
        Form6.resize(783, 535)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form6.setFont(font)
        Form6.setStyleSheet("background:url(:/img/blue_wallpaper.jpg);")
        self.label = QtWidgets.QLabel(Form6)
        self.label.setGeometry(QtCore.QRect(30, 10, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00;  \n"
"")
        self.label.setObjectName("label")
        self.EnterProcessNo_btn = QtWidgets.QPushButton(Form6)
        self.EnterProcessNo_btn.clicked.connect(self.no_onclick)
        self.EnterProcessNo_btn.setGeometry(QtCore.QRect(460, 100, 91, 31))
        self.EnterProcessNo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.EnterProcessNo_btn.setObjectName("EnterProcessNo_btn")
        self.WaitingTime_display = QtWidgets.QLCDNumber(Form6)
        self.WaitingTime_display.setGeometry(QtCore.QRect(320, 340, 111, 31))
        self.WaitingTime_display.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.WaitingTime_display.setObjectName("WaitingTime_display")
        self.ProcessNoText = QtWidgets.QLineEdit(Form6)
        self.ProcessNoText.setGeometry(QtCore.QRect(230, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessNoText.setFont(font)
        self.ProcessNoText.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.ProcessNoText.setObjectName("ProcessNoText")
        self.label_2 = QtWidgets.QLabel(Form6)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.label_2.setObjectName("label_2")
        self.graphicsView_FCFS = QtWidgets.QGraphicsView(Form6)
        self.graphicsView_FCFS.setGeometry(QtCore.QRect(30, 390, 731, 111))
        self.graphicsView_FCFS.setStyleSheet("background: url(:/img/button.png);\n"
" border: 5px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.graphicsView_FCFS.setObjectName("graphicsView_FCFS")
        self.EnterProcessInfo_btn = QtWidgets.QPushButton(Form6)
        self.EnterProcessInfo_btn.clicked.connect(self.ProcessInf_onclick)
        self.EnterProcessInfo_btn.setGeometry(QtCore.QRect(670, 190, 91, 31))
        self.EnterProcessInfo_btn.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.EnterProcessInfo_btn.setObjectName("EnterProcessInfo_btn")
        self.ProcessID_text = QtWidgets.QLineEdit(Form6)
        self.ProcessID_text.setGeometry(QtCore.QRect(20, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessID_text.setFont(font)
        self.ProcessID_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.ProcessID_text.setObjectName("ProcessID_text")
        self.ProcessBurst_text = QtWidgets.QLineEdit(Form6)
        self.ProcessBurst_text.setGeometry(QtCore.QRect(440, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessBurst_text.setFont(font)
        self.ProcessBurst_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.ProcessBurst_text.setObjectName("ProcessBurst_text")
        self.ProcessArrival_text = QtWidgets.QLineEdit(Form6)
        self.ProcessArrival_text.setGeometry(QtCore.QRect(230, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProcessArrival_text.setFont(font)
        self.ProcessArrival_text.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.ProcessArrival_text.setObjectName("ProcessArrival_text")
        self.label_3 = QtWidgets.QLabel(Form6)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: url(:/img/button.png);\n"
" border: 3px solid ;\n"
" border-radius: 15px;\n"
"border-color:#00aa00;\n"
"color: #00aa00; ")
        self.label_3.setObjectName("label_3")
        self.Home_btn = QtWidgets.QPushButton(Form6)
        self.Home_btn.clicked.connect(self.simulation)
        self.Home_btn.setGeometry(QtCore.QRect(680, 90, 75, 71))
        self.Home_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_btn.setIcon(icon)
        self.Home_btn.setIconSize(QtCore.QSize(80, 80))
        self.Home_btn.setObjectName("Home_btn")
        self.retranslateUi(Form6)
        QtCore.QMetaObject.connectSlotsByName(Form6)

    def draw(self, process_id, process_time):
        print("in")
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_FCFS.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        brush = QtGui.QBrush(QtCore.Qt.darkGray)
        self.text = self.tr("Categories")

        #  arr = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]
        # arr2 = ['P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'P0']
        n = len(process_time)
        for i in range(n):
            r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(process_time[i], 80))
            scene.addRect(r, pen, brush)

            mytext1 = QGraphicsSimpleTextItem(str('P' + process_id[i]))
            scene.addItem(mytext1)
            mytext1.setPos(process_id[i] - 22, 30)
            mytext1.setScale(1.5)

            mytext2 = QGraphicsSimpleTextItem(str(process_time[i]))
            scene.addItem(mytext2)
            mytext2.setPos(process_time[i], 85)
            mytext2.setScale(1.3)

    def simulation(self):
        sjf = SJF_Algorithem1.SJF()
        AllProcessInfo = SJF_Algorithem1.process_data
        sjf.schedulingProcess(AllProcessInfo)
        w_time = SJF_Algorithem1.w_time
        self.WaitingTime_display.display(w_time)
        arr = SJF_Algorithem1.process_time
        print(arr)
        arr2 = SJF_Algorithem1.process_id
        print(arr2)
        burst = SJF_Algorithem1.process_burst
        print(burst)
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_FCFS.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        brush = QtGui.QBrush(QtCore.Qt.lightGray)

        n = len(arr)
        next = 0
        for i in range(n):
            m = 25
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






    def ProcessInf_onclick(self):
        processID = int(self.ProcessID_text.text())
        processArrival = int(self.ProcessArrival_text.text())
        processBurst = int(self.ProcessBurst_text.text())
        self.ProcessID_text.setText("")
        self.ProcessArrival_text.setText("")
        self.ProcessBurst_text.setText("")
        AllProcessInfo = SJF_Algorithem1.ProcessInfo(processID, processArrival, processBurst)
        print(AllProcessInfo)




    def no_onclick(self):
        SJFnon_noOfprocess = int(self.ProcessNoText.text())
        SJF_Algorithem1.noProcess(SJFnon_noOfprocess)
        return SJFnon_noOfprocess



    def retranslateUi(self, Form6):
        _translate = QtCore.QCoreApplication.translate
        Form6.setWindowTitle(_translate("Form6", "Form6"))
        self.label.setText(_translate("Form6", "                           Shortest Jop First Premetive (SJF)"))
        self.EnterProcessNo_btn.setText(_translate("Form6", "Enter"))
        self.ProcessNoText.setPlaceholderText(_translate("Form6", "  Enter Number of Process"))
        self.label_2.setText(_translate("Form6", " Average Wating Time"))
        self.EnterProcessInfo_btn.setText(_translate("Form6", "Enter"))
        self.ProcessID_text.setPlaceholderText(_translate("Form6", "        Enter  Process ID"))
        self.ProcessBurst_text.setPlaceholderText(_translate("Form6", "        Enter Burst Time"))
        self.ProcessArrival_text.setPlaceholderText(_translate("Form6", "       Enter Arrival Time"))
        self.label_3.setText(_translate("Form6", "   Gantt Chart "))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form6 = QtWidgets.QMainWindow()
    ui = Ui_Form6()
    ui.setupUi(Form6)
    Form6.show()
    sys.exit(app.exec_())
