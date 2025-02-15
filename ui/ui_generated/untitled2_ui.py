# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 369)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(25, 25, 50); color: white;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        self.lineEdit.setFont(font2)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: white;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: white;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font2)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_6)

        self.horizontalLayout_6.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.gridLayout_23.addWidget(self.pushButton_9, 0, 3, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_29, 0, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_28, 0, 4, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_11.setFont(font4)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.gridLayout_23.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_27, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.verticalSpacer, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_23)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Yangi mahsulot", None))
        self.label.setText(QCoreApplication.translate("Form", u"Yangi mahsulot qo'shish oynasi", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nomi: ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Nomi", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Narxi: ", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Narxi", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Barcode: ", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Barcode", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Qoldiq: ", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"Qoldiq", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Bekor qilish", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Saqlash", None))
    # retranslateUi

