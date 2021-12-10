# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CGgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QProcess

# editBegin
from draw.BresenhamLine import bresLine
from draw.BresenhamCircle import bresCir
from draw.Ellipse import midptellipse
from draw.BezierCurve import DrawBezeriCurve
from draw.BSplineCurve import DrawBSplineCurve
# editEnd

class Ui_MainWindow(object):
    # editBegin
    def drawBreLine(self, MainWindow):
        x1 = int(self.bres_x1.text())
        y1 = int(self.bres_y1.text())
        x2 = int(self.bres_x2.text())
        y2 = int(self.bres_y2.text())
        bresLine(x1, y1, x2, y2)

    def drawBreCircle(self, MainWindow):
        x = int(self.circle_x.text())
        y = int(self.circle_x.text())
        r = int(self.circle_r.text())
        bresCir(x, y, r)

    def drawEllipse(self, MainWindow):
        rx = int(self.ellipse_rx.text())
        ry = int(self.ellipse_ry.text())
        xc = int(self.ellipse_x.text())
        yc = int(self.ellipse_y.text())
        midptellipse(xc, yc, rx, ry)

    def drawBezier(self, MainWindow):
        x1 = int(self.BezierCurve_x1.text())
        x2 = int(self.BezierCurve_x2.text())
        x3 = int(self.BezierCurve_x3.text())
        y1 = int(self.BezierCurve_y1.text())
        y2 = int(self.BezierCurve_y2.text())
        y3 = int(self.BezierCurve_y3.text())
        DrawBezeriCurve(x1, y1, x2, y2, x3, y3)

    def drawBSpline(self, MainWindow):
        x1 = int(self.BSpline_x1.text())
        x2 = int(self.BSpline_x2.text())
        x3 = int(self.BSpline_x3.text())
        x4 = int(self.BSpline_x4.text())
        x5 = int(self.BSpline_x5.text())
        x6 = int(self.BSpline_x6.text())
        x7 = int(self.BSpline_x7.text())
        x8 = int(self.BSpline_x8.text())
        x9 = int(self.BSpline_x9.text())
        y1 = int(self.BSpline_y1.text())
        y2 = int(self.BSpline_y2.text())
        y3 = int(self.BSpline_y3.text())
        y4 = int(self.BSpline_y4.text())
        y5 = int(self.BSpline_y5.text())
        y6 = int(self.BSpline_y6.text())
        y7 = int(self.BSpline_y7.text())
        y8 = int(self.BSpline_y8.text())
        y9 = int(self.BSpline_y9.text())
        DrawBSplineCurve(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9)

    # editEnd

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.generate_line_btn = QtWidgets.QPushButton(self.tab_3)
        self.generate_line_btn.setGeometry(QtCore.QRect(480, 60, 75, 23))
        self.generate_line_btn.setObjectName("generate_line_btn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 421, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.circle_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.circle_x.setObjectName("circle_x")
        self.horizontalLayout_4.addWidget(self.circle_x)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.circle_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.circle_y.setObjectName("circle_y")
        self.horizontalLayout_4.addWidget(self.circle_y)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.circle_r = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.circle_r.setObjectName("circle_r")
        self.horizontalLayout_4.addWidget(self.circle_r)
        self.generate_circle_btn = QtWidgets.QPushButton(self.tab_3)
        self.generate_circle_btn.setGeometry(QtCore.QRect(480, 160, 75, 23))
        self.generate_circle_btn.setObjectName("generate_circle_btn")
        self.generate_ellipse_btn = QtWidgets.QPushButton(self.tab_3)
        self.generate_ellipse_btn.setGeometry(QtCore.QRect(480, 260, 75, 23))
        self.generate_ellipse_btn.setObjectName("generate_ellipse_btn")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 230, 421, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.ellipse_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ellipse_x.setObjectName("ellipse_x")
        self.horizontalLayout_5.addWidget(self.ellipse_x)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.ellipse_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ellipse_y.setObjectName("ellipse_y")
        self.horizontalLayout_5.addWidget(self.ellipse_y)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.ellipse_rx = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ellipse_rx.setObjectName("ellipse_rx")
        self.horizontalLayout_5.addWidget(self.ellipse_rx)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.ellipse_ry = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ellipse_ry.setObjectName("ellipse_ry")
        self.horizontalLayout_5.addWidget(self.ellipse_ry)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 421, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.bres_x1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.bres_x1.setObjectName("bres_x1")
        self.horizontalLayout_3.addWidget(self.bres_x1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.bres_y1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.bres_y1.setObjectName("bres_y1")
        self.horizontalLayout_3.addWidget(self.bres_y1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.bres_x2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.bres_x2.setObjectName("bres_x2")
        self.horizontalLayout_3.addWidget(self.bres_x2)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.bres_y2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.bres_y2.setObjectName("bres_y2")
        self.horizontalLayout_3.addWidget(self.bres_y2)
        self.area_btn = QtWidgets.QPushButton(self.tab_3)
        self.area_btn.setGeometry(QtCore.QRect(480, 360, 75, 23))
        self.area_btn.setObjectName("area_btn")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 330, 421, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout.addWidget(self.label_40)
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout.addWidget(self.label_39)
        self.label_41 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout.addWidget(self.label_41)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.generate_bezier_btn = QtWidgets.QPushButton(self.tab_4)
        self.generate_bezier_btn.setGeometry(QtCore.QRect(410, 40, 141, 51))
        self.generate_bezier_btn.setObjectName("generate_bezier_btn")
        self.generate_BSpline_btn = QtWidgets.QPushButton(self.tab_4)
        self.generate_BSpline_btn.setGeometry(QtCore.QRect(410, 370, 141, 51))
        self.generate_BSpline_btn.setObjectName("generate_BSpline_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 381, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.BezierCurve_x1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_x1.setObjectName("BezierCurve_x1")
        self.gridLayout.addWidget(self.BezierCurve_x1, 0, 1, 1, 1)
        self.BezierCurve_x2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_x2.setObjectName("BezierCurve_x2")
        self.gridLayout.addWidget(self.BezierCurve_x2, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)
        self.BezierCurve_x3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_x3.setObjectName("BezierCurve_x3")
        self.gridLayout.addWidget(self.BezierCurve_x3, 2, 1, 1, 1)
        self.BezierCurve_y1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_y1.setObjectName("BezierCurve_y1")
        self.gridLayout.addWidget(self.BezierCurve_y1, 0, 3, 1, 1)
        self.BezierCurve_y2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_y2.setObjectName("BezierCurve_y2")
        self.gridLayout.addWidget(self.BezierCurve_y2, 1, 3, 1, 1)
        self.BezierCurve_y3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BezierCurve_y3.setObjectName("BezierCurve_y3")
        self.gridLayout.addWidget(self.BezierCurve_y3, 2, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 130, 381, 311))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 8, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 3, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 2, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 2, 1, 1)
        self.BSpline_x5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x5.setObjectName("BSpline_x5")
        self.gridLayout_2.addWidget(self.BSpline_x5, 4, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 5, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 7, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 6, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 6, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 3, 2, 1, 1)
        self.BSpline_x1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x1.setObjectName("BSpline_x1")
        self.gridLayout_2.addWidget(self.BSpline_x1, 0, 1, 1, 1)
        self.BSpline_x8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x8.setObjectName("BSpline_x8")
        self.gridLayout_2.addWidget(self.BSpline_x8, 7, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 4, 2, 1, 1)
        self.BSpline_x4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x4.setObjectName("BSpline_x4")
        self.gridLayout_2.addWidget(self.BSpline_x4, 3, 1, 1, 1)
        self.BSpline_x6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x6.setObjectName("BSpline_x6")
        self.gridLayout_2.addWidget(self.BSpline_x6, 5, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 1, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 5, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 4, 0, 1, 1)
        self.BSpline_x7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x7.setObjectName("BSpline_x7")
        self.gridLayout_2.addWidget(self.BSpline_x7, 6, 1, 1, 1)
        self.BSpline_x9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x9.setObjectName("BSpline_x9")
        self.gridLayout_2.addWidget(self.BSpline_x9, 8, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 7, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 8, 2, 1, 1)
        self.BSpline_x3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x3.setObjectName("BSpline_x3")
        self.gridLayout_2.addWidget(self.BSpline_x3, 2, 1, 1, 1)
        self.BSpline_y1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y1.setObjectName("BSpline_y1")
        self.gridLayout_2.addWidget(self.BSpline_y1, 0, 3, 1, 1)
        self.BSpline_y2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y2.setObjectName("BSpline_y2")
        self.gridLayout_2.addWidget(self.BSpline_y2, 1, 3, 1, 1)
        self.BSpline_y3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y3.setObjectName("BSpline_y3")
        self.gridLayout_2.addWidget(self.BSpline_y3, 2, 3, 1, 1)
        self.BSpline_y4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y4.setObjectName("BSpline_y4")
        self.gridLayout_2.addWidget(self.BSpline_y4, 3, 3, 1, 1)
        self.BSpline_y5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y5.setObjectName("BSpline_y5")
        self.gridLayout_2.addWidget(self.BSpline_y5, 4, 3, 1, 1)
        self.BSpline_y6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y6.setObjectName("BSpline_y6")
        self.gridLayout_2.addWidget(self.BSpline_y6, 5, 3, 1, 1)
        self.BSpline_y7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y7.setObjectName("BSpline_y7")
        self.gridLayout_2.addWidget(self.BSpline_y7, 6, 3, 1, 1)
        self.BSpline_y8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y8.setObjectName("BSpline_y8")
        self.gridLayout_2.addWidget(self.BSpline_y8, 7, 3, 1, 1)
        self.BSpline_y9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_y9.setObjectName("BSpline_y9")
        self.gridLayout_2.addWidget(self.BSpline_y9, 8, 3, 1, 1)
        self.BSpline_x2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.BSpline_x2.setObjectName("BSpline_x2")
        self.gridLayout_2.addWidget(self.BSpline_x2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.generate_koch_btn = QtWidgets.QPushButton(self.tab_5)
        self.generate_koch_btn.setGeometry(QtCore.QRect(320, 70, 121, 61))
        self.generate_koch_btn.setObjectName("generate_koch_btn")
        self.generate_Mandelbrot_btn = QtWidgets.QPushButton(self.tab_5)
        self.generate_Mandelbrot_btn.setGeometry(QtCore.QRect(320, 150, 121, 61))
        self.generate_Mandelbrot_btn.setObjectName("generate_Mandelbrot_btn")
        self.generate_julia_btn = QtWidgets.QPushButton(self.tab_5)
        self.generate_julia_btn.setGeometry(QtCore.QRect(320, 230, 121, 61))
        self.generate_julia_btn.setObjectName("generate_julia_btn")
        self.generate_fern_btn = QtWidgets.QPushButton(self.tab_5)
        self.generate_fern_btn.setGeometry(QtCore.QRect(320, 310, 121, 61))
        self.generate_fern_btn.setObjectName("generate_fern_btn")
        self.label_42 = QtWidgets.QLabel(self.tab_5)
        self.label_42.setGeometry(QtCore.QRect(470, 260, 111, 16))
        self.label_42.setObjectName("label_42")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # editBegin
        self.generate_line_btn.clicked.connect(self.drawBreLine)
        self.generate_circle_btn.clicked.connect(self.drawBreCircle)
        self.generate_ellipse_btn.clicked.connect(self.drawEllipse)
        self.generate_bezier_btn.clicked.connect(self.drawBezier)
        self.generate_BSpline_btn.clicked.connect(self.drawBSpline)
        self.area_btn.clicked.connect(lambda checked, arg="python " + "draw/FieldFill.py": self.execute(arg))
        self.generate_koch_btn.clicked.connect(lambda checked, arg="python " + "draw/Koch.py": self.execute(arg))
        self.generate_Mandelbrot_btn.clicked.connect(lambda checked, arg="python " + "draw/Mandelbrot.py": self.execute(arg))
        self.generate_julia_btn.clicked.connect(lambda checked, arg="python " + "draw/Julia.py": self.execute(arg))
        self.generate_fern_btn.clicked.connect(lambda checked, arg="python " + "draw/Fern.py": self.execute(arg))
        # editEnd

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算机图形学"))
        self.generate_line_btn.setText(_translate("MainWindow", "生成直线"))
        self.label_6.setText(_translate("MainWindow", "圆 "))
        self.label_7.setText(_translate("MainWindow", "x"))
        self.circle_x.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "y"))
        self.circle_y.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "半径"))
        self.circle_r.setText(_translate("MainWindow", "10"))
        self.generate_circle_btn.setText(_translate("MainWindow", "生成圆"))
        self.generate_ellipse_btn.setText(_translate("MainWindow", "生成椭圆"))
        self.label_10.setText(_translate("MainWindow", "椭圆 "))
        self.label_11.setText(_translate("MainWindow", "x"))
        self.ellipse_x.setText(_translate("MainWindow", "50"))
        self.label_12.setText(_translate("MainWindow", "y"))
        self.ellipse_y.setText(_translate("MainWindow", "50"))
        self.label_13.setText(_translate("MainWindow", "x轴半径"))
        self.ellipse_rx.setText(_translate("MainWindow", "16"))
        self.label_14.setText(_translate("MainWindow", "y轴半径"))
        self.ellipse_ry.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "直线 "))
        self.label_2.setText(_translate("MainWindow", "x1"))
        self.bres_x1.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "y1"))
        self.bres_y1.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "x2"))
        self.bres_x2.setText(_translate("MainWindow", "57"))
        self.label_5.setText(_translate("MainWindow", "y2"))
        self.bres_y2.setText(_translate("MainWindow", "142"))
        self.area_btn.setText(_translate("MainWindow", "区域填充"))
        self.label_40.setText(_translate("MainWindow", "种子点坐标"))
        self.label_39.setText(_translate("MainWindow", "x = 61"))
        self.label_41.setText(_translate("MainWindow", "y = 25"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图元生成"))
        self.generate_bezier_btn.setText(_translate("MainWindow", "绘制Bezier曲线"))
        self.generate_BSpline_btn.setText(_translate("MainWindow", "绘制B-样条曲线"))
        self.label_19.setText(_translate("MainWindow", "y2"))
        self.label_15.setText(_translate("MainWindow", "x1"))
        self.label_18.setText(_translate("MainWindow", "y1"))
        self.label_20.setText(_translate("MainWindow", "y3"))
        self.label_16.setText(_translate("MainWindow", "x2"))
        self.BezierCurve_x1.setText(_translate("MainWindow", "1"))
        self.BezierCurve_x2.setText(_translate("MainWindow", "6"))
        self.label_17.setText(_translate("MainWindow", "x3"))
        self.BezierCurve_x3.setText(_translate("MainWindow", "15"))
        self.BezierCurve_y1.setText(_translate("MainWindow", "1"))
        self.BezierCurve_y2.setText(_translate("MainWindow", "13"))
        self.BezierCurve_y3.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "x9"))
        self.label_24.setText(_translate("MainWindow", "x4"))
        self.label_32.setText(_translate("MainWindow", "y3"))
        self.label_21.setText(_translate("MainWindow", "x1"))
        self.label_30.setText(_translate("MainWindow", "y1"))
        self.BSpline_x5.setText(_translate("MainWindow", "-3"))
        self.label_35.setText(_translate("MainWindow", "y6"))
        self.label_37.setText(_translate("MainWindow", "y8"))
        self.label_36.setText(_translate("MainWindow", "y7"))
        self.label_27.setText(_translate("MainWindow", "x7"))
        self.label_33.setText(_translate("MainWindow", "y4"))
        self.BSpline_x1.setText(_translate("MainWindow", "3"))
        self.BSpline_x8.setText(_translate("MainWindow", "3"))
        self.label_22.setText(_translate("MainWindow", "x2"))
        self.label_34.setText(_translate("MainWindow", "y5"))
        self.BSpline_x4.setText(_translate("MainWindow", "-2"))
        self.BSpline_x6.setText(_translate("MainWindow", "-7"))
        self.label_23.setText(_translate("MainWindow", "x3"))
        self.label_31.setText(_translate("MainWindow", "y2"))
        self.label_26.setText(_translate("MainWindow", "x6"))
        self.label_25.setText(_translate("MainWindow", "x5"))
        self.BSpline_x7.setText(_translate("MainWindow", "0"))
        self.BSpline_x9.setText(_translate("MainWindow", "6"))
        self.label_28.setText(_translate("MainWindow", "x8"))
        self.label_38.setText(_translate("MainWindow", "y9"))
        self.BSpline_x3.setText(_translate("MainWindow", "0"))
        self.BSpline_y1.setText(_translate("MainWindow", "1"))
        self.BSpline_y2.setText(_translate("MainWindow", "4"))
        self.BSpline_y3.setText(_translate("MainWindow", "1"))
        self.BSpline_y4.setText(_translate("MainWindow", "4"))
        self.BSpline_y5.setText(_translate("MainWindow", "0"))
        self.BSpline_y6.setText(_translate("MainWindow", "-2"))
        self.BSpline_y7.setText(_translate("MainWindow", "-4"))
        self.BSpline_y8.setText(_translate("MainWindow", "-9"))
        self.BSpline_y9.setText(_translate("MainWindow", "-5"))
        self.BSpline_x2.setText(_translate("MainWindow", "5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "样条曲线生成"))
        self.generate_koch_btn.setText(_translate("MainWindow", "Koch曲线"))
        self.generate_Mandelbrot_btn.setText(_translate("MainWindow", "Mandelbrot"))
        self.generate_julia_btn.setText(_translate("MainWindow", "Julia"))
        self.generate_fern_btn.setText(_translate("MainWindow", "蕨类植物"))
        self.label_42.setText(_translate("MainWindow", "Julia集生成可能较慢"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "分形图形生成"))

    def execute(self, filePath):
        QProcess.startDetached(filePath)
