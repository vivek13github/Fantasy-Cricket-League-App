# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dream.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgb(192, 200, 104);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setEnabled(False)
        self.e1.setObjectName("e1")
        self.horizontalLayout_5.addWidget(self.e1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.e2 = QtWidgets.QLineEdit(self.centralwidget)
        self.e2.setEnabled(False)
        self.e2.setObjectName("e2")
        self.horizontalLayout_5.addWidget(self.e2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.e3 = QtWidgets.QLineEdit(self.centralwidget)
        self.e3.setEnabled(False)
        self.e3.setObjectName("e3")
        self.horizontalLayout_5.addWidget(self.e3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.e4 = QtWidgets.QLineEdit(self.centralwidget)
        self.e4.setEnabled(False)
        self.e4.setObjectName("e4")
        self.horizontalLayout_5.addWidget(self.e4)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rb1 = QtWidgets.QRadioButton(self.groupBox)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_4.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.groupBox)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_4.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.groupBox)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_4.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.groupBox)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_4.addWidget(self.rb4)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setAutoFillBackground(True)
        self.list1.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.list1.setAutoScroll(True)
        self.list1.setObjectName("list1")
        self.verticalLayout_8.addWidget(self.list1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_8.addWidget(self.btn1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("criteria.jpg"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.l1.setFont(font)
        self.l1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.verticalLayout_9.addWidget(self.l1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem4)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.list2.setObjectName("list2")
        self.verticalLayout_9.addWidget(self.list2)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_9.addWidget(self.btn2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("dream1.png"))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionRules = QtWidgets.QAction(MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Team)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionRules)
        self.menuHelp.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dream Team Selector"))
        self.label_4.setText(_translate("MainWindow", "Batsmen"))
        self.label_6.setText(_translate("MainWindow", "Bowlers"))
        self.label_7.setText(_translate("MainWindow", "All Rounders"))
        self.label_8.setText(_translate("MainWindow", "Wicketkeepers"))
        self.label.setText(_translate("MainWindow", "Player Categories"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOWL"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.btn1.setText(_translate("MainWindow", "Available Points : 1000"))
        self.label_2.setText(_translate("MainWindow", "Selected Players"))
        self.l1.setText(_translate("MainWindow", "???"))
        self.btn2.setText(_translate("MainWindow", "Points used : "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New Team"))
        self.actionOpen.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
