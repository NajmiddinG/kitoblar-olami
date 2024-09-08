# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import images_rc
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/image/logo.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQidirish = QAction(MainWindow)
        self.actionQidirish.setObjectName(u"actionQidirish")
        self.actionSotish = QAction(MainWindow)
        self.actionSotish.setObjectName(u"actionSotish")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(30, 25))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.tableWidget_3 = QTableWidget(self.tab)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        font2 = QFont()
        font2.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font1)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_3.addWidget(self.tableWidget_3)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(100, 0))
        self.comboBox_3.setFont(font1)
        self.comboBox_3.setEditable(False)

        self.horizontalLayout_5.addWidget(self.comboBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(90, 0))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(110, 0))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 75))
        self.label_6.setMaximumSize(QSize(150, 100))
        self.label_6.setFont(font3)
        self.label_6.setPixmap(QPixmap(u":/image/logo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(80, 0))
        self.pushButton_6.setMaximumSize(QSize(150, 35))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.comboBox_4 = QComboBox(self.tab)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(200, 0))
        self.comboBox_4.setMaximumSize(QSize(200, 16777215))
        self.comboBox_4.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboBox_4)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(30, 16777215))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(30, 16777215))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout_8.addWidget(self.pushButton_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.tableWidget_4 = QTableWidget(self.tab)
        if (self.tableWidget_4.columnCount() < 8):
            self.tableWidget_4.setColumnCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_5.addWidget(self.tableWidget_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        icon1 = QIcon()
        icon1.addFile(u":/image/main..png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        icon2 = QIcon()
        icon2.addFile(u":/image/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        icon3 = QIcon()
        icon3.addFile(u":/image/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, icon3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        icon4 = QIcon()
        icon4.addFile(u":/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_5, icon4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFunksiyalar = QMenu(self.menubar)
        self.menuFunksiyalar.setObjectName(u"menuFunksiyalar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFunksiyalar.menuAction())
        self.menuFunksiyalar.addAction(self.actionQidirish)
        self.menuFunksiyalar.addAction(self.actionSotish)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Diamond books", None))
        self.actionQidirish.setText(QCoreApplication.translate("MainWindow", u"Qidirish            F3", None))
        self.actionSotish.setText(QCoreApplication.translate("MainWindow", u"Sotish               F4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mahsulot qidirish", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Qidirish yoki scanner ...", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Narxi", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Umumiy hisob", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"0 so'm", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Naqt", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Nasiya", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Plastik", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sotish", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Bekor qilish", None))
        self.label_6.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Qo'shish", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Sotuv 1", None))

        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        ___qtablewidgetitem5 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Narxi", None));
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        ___qtablewidgetitem10 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Qoldiq", None));
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Hisob", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"O'chirish", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Sotuv", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Ombor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Sotuv tarixi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tovar tarixi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Yangi tovar", None))
        self.menuFunksiyalar.setTitle(QCoreApplication.translate("MainWindow", u"Funksiyalar", None))
    # retranslateUi

