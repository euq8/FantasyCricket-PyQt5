# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FC_v1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget,QInputDialog,QPushButton,QApplication,QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit,QInputDialog,QFileDialog
import sqlite3
import sys

class Ui_Dialog1(object):
    def __init__(self,uiMainWindow):
        self.uiMainWindow1=uiMainWindow
        self.team_players=[]
        for i in range(self.uiMainWindow1.playersSelected.count()):
            temp = self.uiMainWindow1.playersSelected.item(i)
            self.team_players.append(temp.text())
            
        for i in self.team_players:
            print(i)

        self.pointsList=[]
    
    def setupUi(self, Dialog):
        self.Dialog1 = Dialog
        Dialog.setObjectName("Evaluate")
        Dialog.resize(458, 677)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.h1 = QtWidgets.QHBoxLayout()
        self.h1.setObjectName("h1")
        self.team = QtWidgets.QLabel(Dialog)
        self.team.setObjectName("team")
        self.h1.addWidget(self.team)
        self.lineEdit_team = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_team.setObjectName("lineEdit_team")
        self.h1.addWidget(self.lineEdit_team)
        self.verticalLayout_3.addLayout(self.h1)
        self.h2 = QtWidgets.QHBoxLayout()
        self.h2.setObjectName("h2")
        self.matchNum = QtWidgets.QLabel(Dialog)
        self.matchNum.setObjectName("matchNum")
        self.h2.addWidget(self.matchNum)
        self.lineEdit_matchNum = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_matchNum.setObjectName("lineEdit_matchNum")
        self.h2.addWidget(self.lineEdit_matchNum)
        self.verticalLayout_3.addLayout(self.h2)
        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.setObjectName("h3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.players = QtWidgets.QLabel(Dialog)
        self.players.setObjectName("players")
        self.verticalLayout.addWidget(self.players)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.p1 = QtWidgets.QLabel(Dialog)
        self.p1.setObjectName("p1")
        self.verticalLayout.addWidget(self.p1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.p2 = QtWidgets.QLabel(Dialog)
        self.p2.setObjectName("p2")
        self.verticalLayout.addWidget(self.p2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.p3 = QtWidgets.QLabel(Dialog)
        self.p3.setObjectName("p3")
        self.verticalLayout.addWidget(self.p3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.p4 = QtWidgets.QLabel(Dialog)
        self.p4.setObjectName("p4")
        self.verticalLayout.addWidget(self.p4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.p5 = QtWidgets.QLabel(Dialog)
        self.p5.setObjectName("p5")
        self.verticalLayout.addWidget(self.p5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.p6 = QtWidgets.QLabel(Dialog)
        self.p6.setObjectName("p6")
        self.verticalLayout.addWidget(self.p6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.p7 = QtWidgets.QLabel(Dialog)
        self.p7.setObjectName("p7")
        self.verticalLayout.addWidget(self.p7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.p8 = QtWidgets.QLabel(Dialog)
        self.p8.setObjectName("p8")
        self.verticalLayout.addWidget(self.p8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.p9 = QtWidgets.QLabel(Dialog)
        self.p9.setObjectName("p9")
        self.verticalLayout.addWidget(self.p9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.p10 = QtWidgets.QLabel(Dialog)
        self.p10.setObjectName("p10")
        self.verticalLayout.addWidget(self.p10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.p11 = QtWidgets.QLabel(Dialog)
        self.p11.setObjectName("p11")
        self.verticalLayout.addWidget(self.p11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.h3.addLayout(self.verticalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem13)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.points = QtWidgets.QLabel(Dialog)
        self.points.setObjectName("points")
        self.verticalLayout_2.addWidget(self.points)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)
        self.point1 = QtWidgets.QLineEdit(Dialog)
        self.point1.setObjectName("point1")
        self.verticalLayout_2.addWidget(self.point1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.point2 = QtWidgets.QLineEdit(Dialog)
        self.point2.setObjectName("point2")
        self.verticalLayout_2.addWidget(self.point2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)
        self.point3 = QtWidgets.QLineEdit(Dialog)
        self.point3.setObjectName("point3")
        self.verticalLayout_2.addWidget(self.point3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.point4 = QtWidgets.QLineEdit(Dialog)
        self.point4.setObjectName("point4")
        self.verticalLayout_2.addWidget(self.point4)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.point5 = QtWidgets.QLineEdit(Dialog)
        self.point5.setObjectName("point5")
        self.verticalLayout_2.addWidget(self.point5)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)
        self.point6 = QtWidgets.QLineEdit(Dialog)
        self.point6.setObjectName("point6")
        self.verticalLayout_2.addWidget(self.point6)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.point7 = QtWidgets.QLineEdit(Dialog)
        self.point7.setObjectName("point7")
        self.verticalLayout_2.addWidget(self.point7)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem22)
        self.point8 = QtWidgets.QLineEdit(Dialog)
        self.point8.setObjectName("point8")
        self.verticalLayout_2.addWidget(self.point8)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem23)
        self.point9 = QtWidgets.QLineEdit(Dialog)
        self.point9.setObjectName("point9")
        self.verticalLayout_2.addWidget(self.point9)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem24)
        self.point10 = QtWidgets.QLineEdit(Dialog)
        self.point10.setObjectName("point10")
        self.verticalLayout_2.addWidget(self.point10)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem25)
        self.point11 = QtWidgets.QLineEdit(Dialog)
        self.point11.setObjectName("point11")
        self.verticalLayout_2.addWidget(self.point11)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem26)
        self.h3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.h3)
        #---------------------------------------------
        self.h4 = QtWidgets.QHBoxLayout()
        self.h4.setObjectName("h4")
        self.bInsert = QtWidgets.QPushButton(Dialog)
        self.bInsert.setObjectName("bInsert")
        self.h4.addWidget(self.bInsert)
        self.bEvaluate = QtWidgets.QPushButton(Dialog)
        self.bEvaluate.setObjectName("bEvaluate")
        self.h4.addWidget(self.bEvaluate)
        self.bOK = QtWidgets.QPushButton(Dialog)
        self.bOK.setObjectName("bOK")
        self.h4.addWidget(self.bOK)
        self.bInsert.clicked.connect(self.eventHandler_insert)
        self.verticalLayout_3.addLayout(self.h4)
        self.bEvaluate.clicked.connect(self.eventHandler_evaluate)
        self.bOK.clicked.connect(self.eventHandler_OK)
        
        print("before")
        self.retranslateUi(Dialog)
        print("after")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Evaluate"))
        self.team.setText(_translate("Dialog", "TEAM"))
        self.matchNum.setText(_translate("Dialog", "MATCH NUMBER"))
        self.players.setText(_translate("Dialog", "PLAYERS"))
        self.temp = self.uiMainWindow1.playersSelected.item(0)
        self.p1.setText(_translate("Dialog", self.temp.text()))
        
        self.temp = self.uiMainWindow1.playersSelected.item(1)
        self.p2.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(2)
        self.p3.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(3)
        self.p4.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(4)
        self.p5.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(5)
        self.p6.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(6)
        self.p7.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(7)
        self.p8.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(8)
        self.p9.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(9)
        self.p10.setText(_translate("Dialog", self.temp.text()))

        self.temp = self.uiMainWindow1.playersSelected.item(10)
        self.p11.setText(_translate("Dialog", self.temp.text()))
        self.points.setText(_translate("Dialog", "POINTS"))
        self.bInsert.setText(_translate("Dialog", "INSERT"))
        self.bEvaluate.setText(_translate("Dialog", "EVALUATE"))
        self.bOK.setText(_translate("Dialog", "OK"))
        self.lineEdit_team.setText(self.uiMainWindow1.teamName)#updating team name
        self.lineEdit_matchNum.setText(str(self.uiMainWindow1.match_num))#updating match num
        print("IN RETRANSLATEUI")


    def eventHandler_insert(self):
        print("in the insert")
        self.pointsList.append(int(self.point1.text()))
        self.pointsList.append(int(self.point2.text()))
        self.pointsList.append(int(self.point3.text()))
        self.pointsList.append(int(self.point4.text()))
        self.pointsList.append(int(self.point5.text()))
        self.pointsList.append(int(self.point6.text()))
        self.pointsList.append(int(self.point7.text()))
        self.pointsList.append(int(self.point8.text()))
        self.pointsList.append(int(self.point9.text()))
        self.pointsList.append(int(self.point10.text()))
        self.pointsList.append(int(self.point11.text()))
        db = DBHelper()
        db.createMatch(self.team_players,int(self.lineEdit_matchNum.text()),self.lineEdit_team.text(),self.pointsList)
        

    def eventHandler_evaluate(self):
        db = DBHelper()
        self.temp=db.evaluateTotal(int(self.lineEdit_matchNum.text()),self.lineEdit_team.text())
        QMessageBox.information(QMessageBox(), 'Total',"Total points of given team is "+str(self.temp))

    def eventHandler_OK(self):
        self.Dialog1.close()


class Ui_Dialog(QDialog):
    def __init__(self,uiMainWindow):
        super().__init__()
        self.uiMainWindow1 = uiMainWindow
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        #----------------------------------------------------
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        #-------------------------------------------
        self.teamlabel = QtWidgets.QLabel()
        self.teamlabel.setObjectName("teamlabel")
        self.horizontalLayout1.addWidget(self.teamlabel)
        #-------------------------------------------
        self.team = QtWidgets.QLineEdit()
        self.team.setObjectName("team")
        self.horizontalLayout1.addWidget(self.team)
        #-------------------------------------------
        self.verticalLayout.addLayout(self.horizontalLayout1)
        #----------------------------------------------------
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        #-------------------------------------------
        self.matchlabel = QtWidgets.QLabel()
        self.matchlabel.setObjectName("matchlabel")
        self.horizontalLayout2.addWidget(self.matchlabel)
        #-------------------------------------------
        self.match_num = QtWidgets.QLineEdit()
        self.match_num.setObjectName("match_num")
        self.horizontalLayout2.addWidget(self.match_num)
        #-------------------------------------------
        self.verticalLayout.addLayout(self.horizontalLayout2)
        #----------------------------------------------------
        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(self.okay)
        self.buttonBox.rejected.connect(self.reject)
        self.verticalLayout.addWidget(self.buttonBox)
        #----------------------------------------------------
        self.retranslateUi()
        self.setLayout(self.verticalLayout)
        self.setWindowTitle("Save")
        self.resize(387, 212)
        self.show()
        self.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Save", "Save"))
        self.teamlabel.setText(_translate("Save", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#5555ff;\">Team</span></p></body></html>"))
        self.matchlabel.setText(_translate("Save", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#5555ff;\">Match Number</span></p></body></html>"))

    def okay(self):
        print('okay method working')
        self.uiMainWindow1.setTeamName(self.team.text())
        self.uiMainWindow1.setMatchNum(self.match_num.text())
        self.close()


        

class DBHelper:
    def __init__(self):
        self.conn=sqlite3.connect("Cricket.db")
        self.c=self.conn.cursor()
        self.temp = 1

    def giveBatsmen(self):
        self.c.execute("SELECT player FROM players WHERE cat='BAT';")
        self.batsmen = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return list(self.batsmen)

    def giveBowler(self):
        self.c.execute("SELECT player FROM players WHERE cat='BWL';")
        self.bowler = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return list(self.bowler)

    def giveWK(self):
        self.c.execute("SELECT player FROM players WHERE cat='WK';")
        self.wk = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return list(self.wk)

    def giveAR(self):
        self.c.execute("SELECT player FROM players WHERE cat='AR';")
        self.ar = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return list(self.ar)

    def checkCat(self, item):
        self.c.execute("SELECT cat FROM players WHERE player=(?)",(item,))
        self.category=list(self.c.fetchall())
        return self.category[0]

    def giveValue(self, item):
        self.c.execute("SELECT value FROM players WHERE player=(?)",(item,))
        self.val=list(self.c.fetchall())
        return self.val[0]

    def createTeam(self,teamList,team,match_num):
        for i in range(11):
            self.c.execute("INSERT INTO team (teamName,player,match_num) VALUES (?,?,?);",(team,teamList[i],match_num))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def createMatch(self,teamList,match_num,team,pointList):
        self.value = []
        for i in teamList:
            self.c.execute("SELECT value FROM players WHERE player=(?);",(i,))
            self.temp=self.c.fetchall()
            self.value.append(self.temp[0][0])
        
        self.temp=[]
        for i in range(11):
            self.temp.append(self.value[i]*pointList[i])
        
        for i in range(11):
            self.c.execute("INSERT INTO match (player,match_num,team,points_inMatch) VALUES (?,?,?,?);",(teamList[i],match_num,team,self.temp[i],))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def evaluateTotal(self,match_num,team):
        self.c.execute("SELECT SUM(points_inMatch) FROM match WHERE match_num=(?) AND team=(?);",(match_num,team,))
        self.temp=self.c.fetchall()
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return self.temp[0][0]

        
class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.playing_11 = 0
        self.available=25
        self.used=0
        self.bat=0
        self.bwl=0
        self.wk=0
        self.ar=0
        self.available=25
        self.used=0
        self.teamName='Barcelona'
        self.match_num=1

    def setTeamName(self,temp):
        self.teamName=temp

    def setMatchNum(self,temp):
        self.match_num=temp
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 825)
        self.Centralwidget = QtWidgets.QWidget(MainWindow)
        self.Centralwidget.setObjectName("Centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        #-----------------------------------------------------------------------------
        self.yourSelection_groupBox = QtWidgets.QGroupBox(self.Centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.yourSelection_groupBox.setFont(font)
        self.yourSelection_groupBox.setObjectName("yourSelection_groupBox")
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.yourSelection_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        #-------------------------------------------------------------------------
        self.horizontalLayout_batsmen = QtWidgets.QHBoxLayout()
        self.horizontalLayout_batsmen.setObjectName("horizontalLayout_batsmen")
        #----------------------------------------------------------------
        self.labelBatsmen = QtWidgets.QLabel(self.yourSelection_groupBox)
        self.labelBatsmen.setObjectName("labelBatsmen")
        self.horizontalLayout_batsmen.addWidget(self.labelBatsmen)
        self.num_batsmen = QtWidgets.QLabel(self.yourSelection_groupBox)
        #----------------------------------------------------------------
        self.num_batsmen.setObjectName("num_batsmen")
        self.horizontalLayout_batsmen.addWidget(self.num_batsmen)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_batsmen)
        #-------------------------------------------------------------------------
        self.horizontalLayout_bowler = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bowler.setObjectName("horizontalLayout_bowler")
        #----------------------------------------------------------------
        self.labelBowler = QtWidgets.QLabel(self.yourSelection_groupBox)
        self.labelBowler.setObjectName("labelBowler")
        self.horizontalLayout_bowler.addWidget(self.labelBowler)
        self.num_bowler = QtWidgets.QLabel(self.yourSelection_groupBox)
        #----------------------------------------------------------------
        self.num_bowler.setObjectName("num_bowler")
        self.horizontalLayout_bowler.addWidget(self.num_bowler)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_bowler)
        #-------------------------------------------------------------------------
        self.horizontalLayout_allRounder = QtWidgets.QHBoxLayout()
        self.horizontalLayout_allRounder.setObjectName("horizontalLayout_allRounder")
        #----------------------------------------------------------------
        self.labelAllrounder = QtWidgets.QLabel(self.yourSelection_groupBox)
        self.labelAllrounder.setObjectName("labelAllrounder")
        self.horizontalLayout_allRounder.addWidget(self.labelAllrounder)
        #----------------------------------------------------------------
        self.num_AR = QtWidgets.QLabel(self.yourSelection_groupBox)
        self.num_AR.setObjectName("num_AR")
        self.horizontalLayout_allRounder.addWidget(self.num_AR)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_allRounder)
        #-------------------------------------------------------------------------
        self.horizontalLayout_wk = QtWidgets.QHBoxLayout()
        self.horizontalLayout_wk.setObjectName("horizontalLayout_wk")
        #----------------------------------------------------------------
        self.labelWK = QtWidgets.QLabel(self.yourSelection_groupBox)
        self.labelWK.setObjectName("labelWK")
        self.horizontalLayout_wk.addWidget(self.labelWK)
        self.num_WK = QtWidgets.QLabel(self.yourSelection_groupBox)
        #----------------------------------------------------------------
        self.num_WK.setObjectName("num_WK")
        self.horizontalLayout_wk.addWidget(self.num_WK)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_wk)
        #---------------------------------------------------------------------------
        self.verticalLayout_8.addWidget(self.yourSelection_groupBox)
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.horizontalLayout_gameDesk = QtWidgets.QHBoxLayout()
        self.horizontalLayout_gameDesk.setObjectName("horizontalLayout_gameDesk")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem)
        #---------------------------------------------------------------------------
        self.playersAvailable_VL = QtWidgets.QVBoxLayout()
        self.playersAvailable_VL.setObjectName("playersAvailable_VL")
        #--------------------------------------------------------------
        self.pointsAvailableDisplay_HL = QtWidgets.QHBoxLayout()
        self.pointsAvailableDisplay_HL.setObjectName("pointsAvailableDisplay_HL")
        #------------------------------------------------------
        self.pointsAvailable = QtWidgets.QLabel(self.Centralwidget)
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.pointsAvailableDisplay_HL.addWidget(self.pointsAvailable)
        #------------------------------------------------------
        self.pointsA = QtWidgets.QLabel(self.Centralwidget)
        self.pointsA.setObjectName("pointsA")
        self.pointsAvailableDisplay_HL.addWidget(self.pointsA)
        #------------------------------------------------------
        self.playersAvailable_VL.addLayout(self.pointsAvailableDisplay_HL)
        #--------------------------------------------------------------
        self.playersAvailable = QtWidgets.QListWidget(self.Centralwidget)
        self.playersAvailable.setObjectName("playersAvailable")
        self.playersAvailable.itemDoubleClicked.connect(self.eventHandler_listWidget_playersAvailable)
        self.playersAvailable_VL.addWidget(self.playersAvailable)
        #--------------------------------------------------------------
        self.ASHFAQUE_HL1 = QtWidgets.QHBoxLayout()
        self.ASHFAQUE_HL1.setObjectName("ASHFAQUE_HL1")
        #--------------------------------------------------------------
        self.rB1 = QtWidgets.QRadioButton(self.Centralwidget)
        self.rB1.setObjectName("rB1")
        self.rB1.clicked.connect(self.eventHandler_radioButtons)
        self.ASHFAQUE_HL1.addWidget(self.rB1)
        #---------------------------------------------------------
        self.rB2 = QtWidgets.QRadioButton(self.Centralwidget)
        self.rB2.setObjectName("rB2")
        self.rB2.clicked.connect(self.eventHandler_radioButtons)
        self.ASHFAQUE_HL1.addWidget(self.rB2)
        #---------------------------------------------------------
        self.rB3 = QtWidgets.QRadioButton(self.Centralwidget)
        self.rB3.setObjectName("rB3")
        self.rB3.clicked.connect(self.eventHandler_radioButtons)
        self.ASHFAQUE_HL1.addWidget(self.rB3)
        #---------------------------------------------------------
        self.rB4 = QtWidgets.QRadioButton(self.Centralwidget)
        self.rB4.setObjectName("rB4")
        self.rB4.clicked.connect(self.eventHandler_radioButtons)
        self.ASHFAQUE_HL1.addWidget(self.rB4)
        #---------------------------------------------------------
        self.playersAvailable_VL.addLayout(self.ASHFAQUE_HL1)
        #--------------------------------------------------------------
        self.horizontalLayout_gameDesk.addLayout(self.playersAvailable_VL)
        #---------------------------------------------------------------------------
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem1)
        #---------------------------------------------------------------------------
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem2)
        #---------------------------------------------------------------------------
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem3)
        #---------------------------------------------------------------------------
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem4)
        #---------------------------------------------------------------------------
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem5)
        #---------------------------------------------------------------------------
        self.playerSelected_VL = QtWidgets.QVBoxLayout()
        self.playerSelected_VL.setObjectName("playerSelected_VL")
        #---------------------------------------------------------------------------
        self.pointsUsedDisplay_HL = QtWidgets.QHBoxLayout()
        self.pointsUsedDisplay_HL.setObjectName("pointsUsedDisplay_HL")
        #------------------------------------------------------
        self.pointsUsed = QtWidgets.QLabel(self.Centralwidget)
        self.pointsUsed.setObjectName("pointsUsed")
        self.pointsUsedDisplay_HL.addWidget(self.pointsUsed)
        #------------------------------------------------------
        self.pointsU = QtWidgets.QLabel(self.Centralwidget)
        self.pointsU.setObjectName("pointsU")
        self.pointsUsedDisplay_HL.addWidget(self.pointsU)
        #------------------------------------------------------
        self.playerSelected_VL.addLayout(self.pointsUsedDisplay_HL)
        #---------------------------------------------------------------------------
        self.playersSelected = QtWidgets.QListWidget(self.Centralwidget)
        self.playersSelected.setObjectName("playersSelected")
        self.playersSelected.itemDoubleClicked.connect(self.eventHandler_listWidget_playersSelected)
        self.playerSelected_VL.addWidget(self.playersSelected)
        #---------------------------------------------------------------------------
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.playerSelected_VL.addItem(spacerItem6)
        self.horizontalLayout_gameDesk.addLayout(self.playerSelected_VL)
        #---------------------------------------------------------------------------
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gameDesk.addItem(spacerItem7)
        #---------------------------------------------------------------------------
        self.verticalLayout_8.addLayout(self.horizontalLayout_gameDesk)
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        #CENTRAL WIDGET
        MainWindow.setCentralWidget(self.Centralwidget)
        #MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)#MENU-ManageTeam
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        #STATUS BAR
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #ACTIONS
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        
        #ADDING ACTIONS TO MENU_ManageTeam
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.actionNew_Team.triggered.connect(self.eventHandler_newTeam)
        
        self.menuManage_Team.addAction(self.actionSave_Team)
        self.actionSave_Team.triggered.connect(self.eventHandler_saveTeam)

        self.menuManage_Team.addAction(self.actionEvaluate_Team)
        self.actionEvaluate_Team.triggered.connect(self.eventHandler_evaluateTeam)

        self.menubar.addAction(self.menuManage_Team.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yourSelection_groupBox.setTitle(_translate("MainWindow", "Your Selection"))
        self.labelBatsmen.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">Batsmen</span></p></body></html>"))
        self.num_batsmen.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">0</span></p></body></html>"))
        self.labelBowler.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">Bowler</span></p></body></html>"))
        self.num_bowler.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">0</span></p></body></html>"))
        self.labelAllrounder.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">All Rounder                </span></p></body></html>"))
        self.num_AR.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">0</span></p></body></html>"))
        self.labelWK.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">Wicket Keeper</span></p></body></html>"))
        self.num_WK.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#5555ff;\">   0</span></p></body></html>"))
        self.pointsAvailable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#5f0ca3;\">Points Available</span></p></body></html>"))
        self.pointsA.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#5f0ca3;\">25</span></p></body></html>"))
        self.pointsUsed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#5f0ca3;\">Points Used</span></p></body></html>"))
        self.pointsU.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#5f0ca3;\">0</span></p></body></html>"))
        #------------------------------------------------
        self.rB1.setText(_translate("MainWindow", "BAT"))
        self.rB2.setText(_translate("MainWindow", "BWL"))
        self.rB3.setText(_translate("MainWindow", "WK"))
        self.rB4.setText(_translate("MainWindow", "AR"))
        #------------------------------------------------
        self.pointsUsed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#5f0ca3;\">Points Used</span></p></body></html>"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

    def eventHandler_radioButtons(self):
        if self.rB1.isChecked()==True:
            db = DBHelper()
            batsmen=db.giveBatsmen()#list of batsmen
            self.playersAvailable.clear()
            self.showList(batsmen)
        elif self.rB2.isChecked()==True:
            db = DBHelper()
            bowler=db.giveBowler()####list of bowler
            self.playersAvailable.clear()
            self.showList(bowler)
        elif self.rB3.isChecked()==True:
            db = DBHelper()
            wk=db.giveWK()################list of WK
            self.playersAvailable.clear()
            self.showList(wk)
        elif self.rB4.isChecked()==True:
            db = DBHelper()
            ar=db.giveAR()################list of AR
            self.playersAvailable.clear()
            self.showList(ar)

    def eventHandler_listWidget_playersAvailable(self, item):
        if self.playing_11<11:
            if self.used<25:
                self.playersAvailable.takeItem(self.playersAvailable.row(item))
                self.playersSelected.addItem(item.text())
                db = DBHelper()
                result=db.checkCat(item.text())
                val=db.giveValue(item.text())
                if result[0]=='BAT':
                    self.available-=int(val[0])
                    self.used+=int(val[0])
                    self.bat+=1
                    self.num_batsmen.setText(str(self.bat))
                    self.pointsA.setText(str(self.available))
                    self.pointsU.setText(str(self.used))
                elif result[0]=='BWL':
                    self.available-=int(val[0])
                    self.used+=int(val[0])
                    self.bwl+=1
                    self.num_bowler.setText(str(self.bwl))
                    self.pointsA.setText(str(self.available))
                    self.pointsU.setText(str(self.used))
                elif result[0]=='WK':
                    self.available-=int(val[0])
                    self.used+=int(val[0])
                    self.wk+=1
                    self.num_WK.setText(str(self.wk))
                    self.pointsA.setText(str(self.available))
                    self.pointsU.setText(str(self.used))
                elif result[0]=='AR':
                    self.available-=int(val[0])
                    self.used+=int(val[0])
                    self.ar+=1
                    self.num_AR.setText(str(self.ar))
                    self.pointsA.setText(str(self.available))
                    self.pointsU.setText(str(self.used))
                self.playing_11+=1
            else:
                QMessageBox.information(QMessageBox(), 'OverFlow','All Points Used')
        else:
            QMessageBox.information(QMessageBox(), 'Squad','Eleven players have been selected.')
        #ISSUE
        
    def eventHandler_listWidget_playersSelected(self, item):
        self.playersSelected.takeItem(self.playersSelected.row(item))
        self.playersAvailable.addItem(item.text())
        db = DBHelper()
        result=db.checkCat(item.text())
        val=db.giveValue(item.text())
        if result[0]=='BAT':
            self.available+=int(val[0])
            self.used-=int(val[0])
            self.bat-=1
            self.num_batsmen.setText(str(self.bat))
            self.pointsA.setText(str(self.available))
            self.pointsU.setText(str(self.used))
        elif result[0]=='BWL':
            self.available+=int(val[0])
            self.used-=int(val[0])
            self.bwl-=1
            self.num_bowler.setText(str(self.bwl))
            self.pointsA.setText(str(self.available))
            self.pointsU.setText(str(self.used))
        elif result[0]=='WK':
            self.available+=int(val[0])
            self.used-=int(val[0])
            self.wk-=1
            self.num_WK.setText(str(self.wk))
            self.pointsA.setText(str(self.available))
            self.pointsU.setText(str(self.used))
        elif result[0]=='AR':
            self.available+=int(val[0])
            self.used-=int(val[0])
            self.ar-=1
            self.num_AR.setText(str(self.ar))
            self.pointsA.setText(str(self.available))
            self.pointsU.setText(str(self.used))
        self.playing_11-=1
        #ISSUE

    def eventHandler_newTeam(self):
        self.newWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()

    def eventHandler_saveTeam(self):
        sav = Ui_Dialog(self)
        
        self.team_players=[]
        for i in range(self.playersSelected.count()):
            self.temp = self.playersSelected.item(i)
            self.team_players.append(self.temp.text())

        print(self.teamName)
        print(self.match_num)

        db = DBHelper()
        db.createTeam(self.team_players,self.teamName,self.match_num)

        for i in self.team_players:#error check
            print(i)

    def eventHandler_evaluateTeam(self):
        print("NOT DONE")
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog1(self)
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        print("DONE")
        

    def showList(self,listPLAYER):
        for PLAYER in listPLAYER:
            self.playersAvailable.addItem(PLAYER[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
