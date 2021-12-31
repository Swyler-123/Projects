# coding: utf8

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

# import main

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1178, 760)
        self.actionProjekt = QAction(MainWindow)
        self.actionProjekt.setObjectName(u"actionProjekt")
        self.actionGrafik = QAction(MainWindow)
        self.actionGrafik.setObjectName(u"actionGrafik")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.List_frame = QFrame(self.centralwidget)
        self.List_frame.setObjectName(u"List_frame")
        self.List_frame.setFrameShape(QFrame.StyledPanel)
        self.List_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.List_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.List_frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(417, 0))
        self.tableWidget.setMaximumSize(QSize(16773000, 16777215))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.List_frame, 0, 0, 1, 1)

        self.Graphic_frame = QFrame(self.centralwidget)
        self.Graphic_frame.setObjectName(u"Graphic_frame")
        self.Graphic_frame.setFrameShape(QFrame.StyledPanel)
        self.Graphic_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Graphic_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.Graphic_frame)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.Graphic_frame)
        if (self.tableWidget_2.columnCount() < 20):
            self.tableWidget_2.setColumnCount(20)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setMinimumSize(QSize(0, 102))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 102))
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setColumnCount(20)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(50)

        self.gridLayout_4.addWidget(self.tableWidget_2, 3, 0, 1, 1)

        self.Input_frame = QFrame(self.Graphic_frame)
        self.Input_frame.setObjectName(u"Input_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Input_frame.sizePolicy().hasHeightForWidth())
        self.Input_frame.setSizePolicy(sizePolicy3)
        self.Input_frame.setFrameShape(QFrame.StyledPanel)
        self.Input_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.Input_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.Input_frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Plot_BP = QPushButton(self.Input_frame)
        self.Plot_BP.setObjectName(u"Plot_BP")

        self.horizontalLayout.addWidget(self.Plot_BP)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label = QLabel(self.Input_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addRow_PB = QPushButton(self.Input_frame)
        self.addRow_PB.setObjectName(u"addRow_PB")

        self.horizontalLayout_2.addWidget(self.addRow_PB)

        self.delRow_PB = QPushButton(self.Input_frame)
        self.delRow_PB.setObjectName(u"delRow_PB")

        self.horizontalLayout_2.addWidget(self.delRow_PB)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.Input_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_Eintrittssteigung = QLabel(self.Input_frame)
        self.label_Eintrittssteigung.setObjectName(u"label_Eintrittssteigung")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_Eintrittssteigung.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_Eintrittssteigung)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.Input_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_Austrittssteigung = QLabel(self.Input_frame)
        self.label_Austrittssteigung.setObjectName(u"label_Austrittssteigung")
        self.label_Austrittssteigung.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_Austrittssteigung)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)


        self.gridLayout_4.addWidget(self.Input_frame, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.Graphic_frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1178, 21))
        self.menuMenu = QMenu(self.menuBar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuSave = QMenu(self.menuMenu)
        self.menuSave.setObjectName(u"menuSave")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuSave.menuAction())
        self.menuSave.addAction(self.actionProjekt)
        self.menuSave.addAction(self.actionGrafik)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionProjekt.setText(QCoreApplication.translate("MainWindow", u"Projekt", None))
        self.actionGrafik.setText(QCoreApplication.translate("MainWindow", u"Grafik", None))
        ___qtablewidgetitem = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Steigung pro Stange", None));
        ___qtablewidgetitem1 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Abweichung zum Maximum", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Bohrplan aktualisieren:", None))
        self.Plot_BP.setText(QCoreApplication.translate("MainWindow", u"Aktualisieren", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reihe hinzuf\u00fcgen oder l\u00f6schen:", None))
        self.addRow_PB.setText(QCoreApplication.translate("MainWindow", u"Hinzuf\u00fcgen", None))
        self.delRow_PB.setText(QCoreApplication.translate("MainWindow", u"L\u00f6schen", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Eintrittssteigung:", None))
        self.label_Eintrittssteigung.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Austrittssteigung:", None))
        self.label_Austrittssteigung.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi




###############################################################################

import numpy as np

from scipy.interpolate import CubicSpline

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanva





class MyQtApp(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.showNormal()
        self.setWindowTitle("Bohrplan")
        self.tableWidget.setRowCount(9)
        self.setValues()

        self.Plot_BP.clicked.connect(self.plot)
        self.addRow_PB.clicked.connect(self.addRow)
        self.delRow_PB.clicked.connect(self.delRow)

        self.tableWidget.setHorizontalHeaderLabels(["Terrainpunkte\nTiefe", "Terrainpunkte\nLaenge", "Bohrpunkte\nTiefe", "Bohrpunkte\nLaenge"])


        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout_4.addWidget(self.canvas, 0, 0, 1, 1)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot()


    def setValues(self):
        values = [[-1.2,0,-1.2,0],
                  [0,0,-7.2,17],
                  [0,10,0,43],
                  [-4.2,17,'',''],
                  [-4.2,20,'',''],
                  [0,29,'',''],
                  [1.2,37,'',''],
                  [1.2,43,'',''],
                  [0,43,'','']]

        for k in range(9):
            for i in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(values[k][i]))
                self.tableWidget.setItem(k, i, item)


    def addRow(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)

    def delRow(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount()-1)


    def plot(self):
        print("plot")
        tp_y = []
        tp_x = []
        bp_y = []
        bp_x = []

        n_row = self.tableWidget.rowCount()
        for i in range(n_row):
            tp_item_y = self.tableWidget.item(i,0)
            tp_item_x = self.tableWidget.item(i,1)
            bp_item_y = self.tableWidget.item(i, 2)
            bp_item_x = self.tableWidget.item(i, 3)

            try:
                tp_y.append(float(tp_item_y.text()))
                tp_x.append(float(tp_item_x.text()))
                bp_y.append(float(bp_item_y.text()))
                bp_x.append(float(bp_item_x.text()))
            except:
                #QtWidgets.QMessageBox.about(self, "Eingabefehler", "Reihen dürfen in den Bohrpunkte Spalten nicht leer sein!")
                #raise ValueError
                pass


        start_grube = [[0,0,tp_y[0]],
                       [-3,-2,-2]]
        for i in range(3):
            tp_y.insert(i,start_grube[0][i])
            tp_x.insert(i,start_grube[1][i])

        end_grube = [[tp_y[len(tp_y)-1],tp_y[len(tp_y)-2],tp_y[len(tp_y)-2]],
                     [tp_x[len(tp_x)-1]+2,tp_x[len(tp_x)-1]+2, tp_x[len(tp_x)-1]+3]]
        for i in range(3):
            tp_y.append(end_grube[0][i])
            tp_x.append(end_grube[1][i])

        tp_y = np.asarray(tp_y)
        tp_x = np.asarray(tp_x)
        bp_y = np.asarray(bp_y)
        bp_x = np.asarray(bp_x)



        #################Algorithmus##################

        # reset fehler
        fehler = False

        # Stangenlänge
        l_stange = 3

        # Max Prozent pro Stange
        proz = 8

        # delta_max berechnen
        proz_calc = 8 / 100
        delta_y_max = l_stange * proz_calc
        delta_x_max = np.sqrt(delta_y_max ** 2 + l_stange ** 2)

        # Kubische Interpolation
        try:
            cs = CubicSpline(bp_x, bp_y, bc_type="natural")
        except:
            QtWidgets.QMessageBox.about(self, "Eingabefehler", "Die Bohrpunkte Laengen müssen zwingend von klein nach gross sortiert werden!")
            raise ValueError
        ###############################################################################
        # Stangen berechnen
        x_1 = bp_x[0]
        x_2 = x_1 + delta_x_max / 2
        y_1 = bp_y[0]

        x_lin = np.array([bp_x[0]])
        y_lin = np.array([bp_y[0]])

        result = 0
        position = 1

        # loop um alle stangen zu berechnen (x und y werte in liste speichern)
        while x_2 < bp_x[len(bp_x) - 1]:
            # get x_2 and y_2
            for i in range(160):
                result = np.sqrt((x_2 - x_1) ** 2 + (cs(x_2) - y_1) ** 2) - 3
                if result > 0:
                    x_2 -= 0.01

                elif result < 0:
                    x_2 += 0.01

            # x array erweitern
            x_lin = np.append(x_lin, x_2)
            x_1 = x_2

            # y array erweitern
            y_lin = np.append(y_lin, cs(x_2))


            y_1 = y_lin[position]

            # x_2 zuruecksetzen
            x_2 = x_1 + delta_x_max / 2

            # position korrigieren
            position += 1

        ###############################################################################
        # Steigung kontrollieren
        delta_y = np.linspace(0, 1, len(x_lin) - 1)
        delta_x = np.linspace(0, 1, len(x_lin) - 1)
        steigung = np.linspace(0, 1, len(x_lin) - 1)

        for i in range(len(y_lin) - 1):
            delta_y[i] = y_lin[i + 1] - y_lin[i]
            delta_x[i] = x_lin[i + 1] - x_lin[i]
            steigung[i] = delta_y[i] / delta_x[i]

        self.tableWidget_2.setColumnCount(steigung.shape[0])

        proz_steigung = np.linspace(0, 1, len(steigung)-1)

        for i in range(len(steigung) - 1):
            proz_steigung[i] = (steigung[i + 1] - steigung[i]) * 100

        delta_proz = proz_steigung - proz

        if any(delta_proz > 0):
            index = np.nonzero(delta_proz > 0)
            temp = []
            for i in range(len(index[0])):
                temp.append(index[0].item(i) + 1)

            x_out = x_lin[temp]
            y_out = y_lin[temp]
            fehler = True
            print("\nAchtung in einzelnen Punkten wird übersteuert!")
            print("Der Unterschied zur maximalen Steigung beträgt so viel Prozent:\n")
            print(np.round(delta_proz, 2))

            for i in range(delta_proz.shape[0]):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(np.round(delta_proz[i],2)))
                self.tableWidget_2.setItem(1,i, item)
        ###############################################################################
        # Ein und Austrittssteigung

        print("--------------------------------------------------------\n")
        print("Die Einstichssteigung beträgt", round(steigung[0] * 100, 2), "%\n")
        print("Die Austrittssteigung beträgt", round(steigung[(len(steigung) - 1)] * 100, 2), "%\n")
        self.label_Eintrittssteigung.setText(str(round(steigung[0] * 100, 2)))
        self.label_Austrittssteigung.setText(str(round(steigung[(len(steigung) - 1)] * 100, 2)))
        print("--------------------------------------------------------\n")
        print("Die Steigungen pro Stange sind:\n")
        print(np.round(steigung * 100, 2))

        for i in range(steigung.shape[0]):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(np.round(steigung[i]*100,2)))
            self.tableWidget_2.setItem(0,i, item)

        ###############################################################################
        # Analyse
        l_stange_real = np.linspace(0, 1, len(x_lin) - 1)
        for i in range(len(x_lin) - 1):
            l_stange_real[i] = np.sqrt((x_lin[i + 1] - x_lin[i]) ** 2 + (y_lin[i + 1] - y_lin[i]) ** 2)

        stangen_var = np.var(l_stange_real)
        stangen_mean = np.mean(l_stange_real)



        #################Ende Algorithmus##################

        figure = Figure()
        axes = figure.gca()

        if fehler == True:
            axes.plot(tp_x, tp_y,'-', bp_x, bp_y, 'o', x_lin, y_lin, 'o', x_out, y_out, 'v', x_lin, y_lin, '-')
            axes.legend(['Landschaft', 'Punkte', 'Stangen', 'Zu hohe Steigung'], loc='best')

        else:
            axes.plot(tp_x, tp_y,'-', bp_x, bp_y, 'o', x_lin, y_lin, 'o', x_lin, y_lin, '-')
            axes.legend(['Landschaft', 'Punkte', 'Stangen'], loc='best')


        #axes.figure(dpi=600)
        axes.set_title("Bohrplan")
        axes.set_xlabel("Laenge [m]")
        axes.set_ylabel("Tiefe [m]")
        axes.axis("equal")
        axes.grid(axis="both")

        #scene = QtWidgets.QGraphicsScene()
        #view = QtWidgets.QGraphicsView(scene)

        self.graphicsView = FigureCanvas(figure)
        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()