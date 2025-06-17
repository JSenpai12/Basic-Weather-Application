# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(326, 498)
        icon = QIcon()
        icon.addFile(u"../../Downloads/weather (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(249, 249, 249);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 330, 329, 171))
        self.frame.setStyleSheet(u"background-color: rgb(105, 112, 255);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right: 0px;\n"
"border-bottom-left: 0px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 100, 301, 51))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	color: rgb(105, 112, 255);\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(155, 168, 244);\n"
"	color: white;\n"
"}")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 301, 51))
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(82, 85, 255);\n"
"	color: rgb(139, 117, 248);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	font-size: 18px;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 90, 81, 71))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setPixmap(QPixmap(u"../../Downloads/sun.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 41, 41))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setPixmap(QPixmap(u"../../Downloads/gps.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 40, 281, 41))
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"color: black")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 170, 101, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"font-size: 45px;\n"
"color: black")
        self.label_4.setTextFormat(Qt.TextFormat.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setIndent(0)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 260, 51, 41))
        self.label_6.setStyleSheet(u"background-color: transparent;")
        self.label_6.setPixmap(QPixmap(u"../../Downloads/speed.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 51, 41))
        self.label_7.setStyleSheet(u"background-color: transparent;")
        self.label_7.setPixmap(QPixmap(u"../../Downloads/humidity-sensor.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 250, 51, 71))
        font1 = QFont()
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: transparent;\n"
"color: black;")
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 250, 51, 71))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"color: black;")
        self.label_9.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather Application", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Find your city weather", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SEARCH A CITY", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0%\n"
"Humidity", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0 km/h\n"
"Per Hour", None))
    # retranslateUi

