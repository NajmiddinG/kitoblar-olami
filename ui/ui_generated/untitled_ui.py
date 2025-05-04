# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 875)
        MainWindow.setMinimumSize(QSize(0, 600))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/image/logo.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #212121;\n"
"color: white;\n"
"border-color: white;")
        self.actionasdasasdasd = QAction(MainWindow)
        self.actionasdasasdasd.setObjectName(u"actionasdasasdasd")
        self.actionasdasdas = QAction(MainWindow)
        self.actionasdasdas.setObjectName(u"actionasdasdas")
        self.actiondasda = QAction(MainWindow)
        self.actiondasda.setObjectName(u"actiondasda")
        self.actionsdas = QAction(MainWindow)
        self.actionsdas.setObjectName(u"actionsdas")
        self.actionKattalashtirish = QAction(MainWindow)
        self.actionKattalashtirish.setObjectName(u"actionKattalashtirish")
        self.actionKichiklashtirish = QAction(MainWindow)
        self.actionKichiklashtirish.setObjectName(u"actionKichiklashtirish")
        self.actionKattalashtirish_2 = QAction(MainWindow)
        self.actionKattalashtirish_2.setObjectName(u"actionKattalashtirish_2")
        self.actionKichiklashtirish_2 = QAction(MainWindow)
        self.actionKichiklashtirish_2.setObjectName(u"actionKichiklashtirish_2")
        self.actionsssss = QAction(MainWindow)
        self.actionsssss.setObjectName(u"actionsssss")
        self.actionQidirish_F3 = QAction(MainWindow)
        self.actionQidirish_F3.setObjectName(u"actionQidirish_F3")
        self.actionSotish_F4 = QAction(MainWindow)
        self.actionSotish_F4.setObjectName(u"actionSotish_F4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_20 = QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_20.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setIconSize(QSize(30, 25))
        self.tab1_2 = QWidget()
        self.tab1_2.setObjectName(u"tab1_2")
        self.horizontalLayout_8 = QHBoxLayout(self.tab1_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_2 = QLabel(self.tab1_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 40))
        self.label_2.setMaximumSize(QSize(1000, 70))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font2)

        self.gridLayout_13.addWidget(self.label_2, 1, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lineEdit_2 = QLineEdit(self.tab1_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.tab1_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.label_3, 1, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab1_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.tableWidget_2.setFont(font4)
        self.tableWidget_2.setStyleSheet(u"")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_14.addWidget(self.tableWidget_2, 3, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_18, 0, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_17, 0, 4, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_19, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.tab1_2)
        self.pushButton.setObjectName(u"pushButton")
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(14)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.gridLayout_15.addWidget(self.pushButton, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.tab1_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.gridLayout_15.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_15, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.frame = QFrame(self.tab1_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 40))
        self.frame.setStyleSheet(u"border:0;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 0, 161, 35))
        font7 = QFont()
        font7.setPointSize(15)
        self.lineEdit.setFont(font7)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: 1px solid rgb(94, 111, 135);\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"border-right: 0px;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(320, 0, 71, 35))
        self.label_16.setFont(font7)
        self.label_16.setStyleSheet(u"QLabel{\n"
"color: #9CA7B7;\n"
"background-color: #080A0C;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"padding-top: 5px;\n"
"padding-right: 10px;\n"
"padding-bottom: 5px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgb(94, 111, 135);\n"
"border-left: 0px\n"
"}")
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(9, 0, 141, 35))
        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(15)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.lineEdit_7.setFont(font8)
        self.lineEdit_7.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.lineEdit_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_7.setStyleSheet(u"")
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(400, 0, 100, 35))
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.setMaximumSize(QSize(100, 16777215))
        self.comboBox.setFont(font8)
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout_13.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self.label = QLabel(self.tab1_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(150, 75))
        self.label.setMaximumSize(QSize(150, 100))
        font9 = QFont()
        font9.setFamilies([u"Times New Roman"])
        font9.setPointSize(25)
        font9.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font9)
        self.label.setTabletTracking(False)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/image/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout_9.addWidget(self.label)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.tab1_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(150, 50))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"background-color:rgb(31, 118, 28); color: white;")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_14 = QPushButton(self.tab1_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font5)
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout.addWidget(self.pushButton_14)

        self.comboBox_2 = QComboBox(self.tab1_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(200, 0))
        self.comboBox_2.setMaximumSize(QSize(200, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Times New Roman"])
        font10.setPointSize(16)
        font10.setBold(False)
        font10.setStyleStrategy(QFont.PreferDefault)
        self.comboBox_2.setFont(font10)
        self.comboBox_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_2.setAcceptDrops(False)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.pushButton_10 = QPushButton(self.tab1_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(30, 16777215))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"background-color:rgb(31, 118, 28); color: white;")

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.pushButton_8 = QPushButton(self.tab1_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 16777215))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.tab1_2)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        font11 = QFont()
        font11.setFamilies([u"Times New Roman"])
        font11.setPointSize(14)
        font11.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font11);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        font12 = QFont()
        font12.setFamilies([u"Times New Roman"])
        font12.setPointSize(16)
        font12.setStrikeOut(False)
        font12.setStyleStrategy(QFont.PreferDefault)
        self.tableWidget.setFont(font12)
        self.tableWidget.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.gridLayout_16.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_16, 0, 1, 1, 1)

        self.gridLayout_7.setColumnStretch(0, 4)
        self.gridLayout_7.setColumnStretch(1, 6)

        self.horizontalLayout_8.addLayout(self.gridLayout_7)

        icon1 = QIcon()
        icon1.addFile(u":/image/main..png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab1_2, icon1, "")
        self.tab2_2 = QWidget()
        self.tab2_2.setObjectName(u"tab2_2")
        self.gridLayout_17 = QGridLayout(self.tab2_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tableWidget_4 = QTableWidget(self.tab2_2)
        if (self.tableWidget_4.columnCount() < 10):
            self.tableWidget_4.setColumnCount(10)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font11);
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        if (self.tableWidget_4.rowCount() < 10):
            self.tableWidget_4.setRowCount(10)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setFont(font6)
        self.tableWidget_4.setAutoFillBackground(False)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setRowCount(10)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.gridLayout_18.addWidget(self.tableWidget_4, 2, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_6 = QPushButton(self.tab2_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")
        icon2 = QIcon()
        icon2.addFile(u":/image/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_6)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.pushButton_4 = QPushButton(self.tab2_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_4)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_23)

        self.pushButton_3 = QPushButton(self.tab2_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_10.addWidget(self.pushButton_3)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_24)

        self.pushButton_13 = QPushButton(self.tab2_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_13)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)

        self.lineEdit_3 = QLineEdit(self.tab2_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_3)


        self.gridLayout_18.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab2_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_17.addWidget(self.label_7, 1, 0, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/image/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab2_2, icon3, "")
        self.tab3_2 = QWidget()
        self.tab3_2.setObjectName(u"tab3_2")
        self.gridLayout_19 = QGridLayout(self.tab3_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.tab3_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.dateEdit = QDateEdit(self.tab3_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(180, 40))
        self.dateEdit.setFont(font2)

        self.horizontalLayout_12.addWidget(self.dateEdit)

        self.label_4 = QLabel(self.tab3_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.dateEdit_2 = QDateEdit(self.tab3_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(180, 40))
        self.dateEdit_2.setFont(font2)

        self.horizontalLayout_12.addWidget(self.dateEdit_2)

        self.label_5 = QLabel(self.tab3_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.pushButton_7 = QPushButton(self.tab3_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.comboBox_3 = QComboBox(self.tab3_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(200, 0))
        self.comboBox_3.setMaximumSize(QSize(200, 16777215))
        self.comboBox_3.setFont(font10)
        self.comboBox_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_3.setAcceptDrops(False)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)

        self.horizontalLayout_12.addWidget(self.comboBox_3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_26)


        self.gridLayout_19.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget_5 = QTableWidget(self.tab3_2)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font11);
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font11);
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font11);
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font11);
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font11);
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setFont(font2)
        self.tableWidget_5.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_5.verticalHeader().setVisible(False)

        self.horizontalLayout_11.addWidget(self.tableWidget_5)

        self.tableWidget_3 = QTableWidget(self.tab3_2)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem28.setFont(font11);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font11);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font11);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font11);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font11);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setFont(font2)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.horizontalLayout_11.addWidget(self.tableWidget_3)

        self.horizontalLayout_11.setStretch(0, 7)
        self.horizontalLayout_11.setStretch(1, 10)

        self.gridLayout_19.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.tab3_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.pushButton_17 = QPushButton(self.tab3_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font5)
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_17.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout_6.addWidget(self.pushButton_17)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.gridLayout_19.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/image/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab3_2, icon4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget_8 = QTableWidget(self.tab_2)
        if (self.tableWidget_8.columnCount() < 4):
            self.tableWidget_8.setColumnCount(4)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font11);
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font11);
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font11);
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font11);
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setFont(font2)
        self.tableWidget_8.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_8.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget_8.setSortingEnabled(False)
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_8.verticalHeader().setVisible(False)

        self.horizontalLayout_15.addWidget(self.tableWidget_8)

        self.tableWidget_9 = QTableWidget(self.tab_2)
        if (self.tableWidget_9.columnCount() < 6):
            self.tableWidget_9.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem37.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font11);
        self.tableWidget_9.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        sizePolicy.setHeightForWidth(self.tableWidget_9.sizePolicy().hasHeightForWidth())
        self.tableWidget_9.setSizePolicy(sizePolicy)
        self.tableWidget_9.setFont(font2)
        self.tableWidget_9.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_9.setSortingEnabled(False)
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_9.verticalHeader().setVisible(False)

        self.horizontalLayout_15.addWidget(self.tableWidget_9)

        self.horizontalLayout_15.setStretch(0, 7)
        self.horizontalLayout_15.setStretch(1, 10)

        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.dateEdit_3 = QDateEdit(self.tab_2)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(180, 40))
        self.dateEdit_3.setFont(font2)

        self.horizontalLayout_14.addWidget(self.dateEdit_3)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.dateEdit_4 = QDateEdit(self.tab_2)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setMinimumSize(QSize(180, 40))
        self.dateEdit_4.setFont(font2)

        self.horizontalLayout_14.addWidget(self.dateEdit_4)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.pushButton_15 = QPushButton(self.tab_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_14.addWidget(self.pushButton_15)

        self.comboBox_4 = QComboBox(self.tab_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(200, 0))
        self.comboBox_4.setMaximumSize(QSize(200, 16777215))
        self.comboBox_4.setFont(font10)
        self.comboBox_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_4.setAcceptDrops(False)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)

        self.horizontalLayout_14.addWidget(self.comboBox_4)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_32)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background-color: #004d40;\n"
"color: white;\n"
"border-color: white;")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 40))
        self.label_9.setMaximumSize(QSize(1000, 70))
        self.label_9.setFont(font2)

        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 40))
        self.frame_2.setStyleSheet(u"border:0;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(160, 0, 161, 35))
        self.lineEdit_5.setFont(font7)
        self.lineEdit_5.setMouseTracking(True)
        self.lineEdit_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: 1px solid rgb(94, 111, 135);\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"border-right: 0px;\n"
"}")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, 0, 71, 35))
        self.label_17.setFont(font7)
        self.label_17.setStyleSheet(u"QLabel{\n"
"color: #9CA7B7;\n"
"background-color: #080A0C;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"padding-top: 5px;\n"
"padding-right: 10px;\n"
"padding-bottom: 5px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgb(94, 111, 135);\n"
"border-left: 0px\n"
"}")
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(9, 0, 141, 35))
        self.lineEdit_6.setFont(font8)
        self.lineEdit_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.lineEdit_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_6.setStyleSheet(u"")
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.tableWidget_6 = QTableWidget(self.tab)
        if (self.tableWidget_6.columnCount() < 5):
            self.tableWidget_6.setColumnCount(5)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font3);
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font3);
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font3);
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font3);
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font3);
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        font13 = QFont()
        font13.setFamilies([u"Times New Roman"])
        font13.setPointSize(10)
        font13.setStyleStrategy(QFont.PreferDefault)
        self.tableWidget_6.setFont(font13)
        self.tableWidget_6.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_6.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_6.setSortingEnabled(False)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_5.addWidget(self.tableWidget_6, 2, 0, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_27, 0, 2, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_28, 0, 4, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_29, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font5)
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.gridLayout_23.addWidget(self.pushButton_9, 0, 3, 1, 1)

        self.pushButton_11 = QPushButton(self.tab)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font6)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.gridLayout_23.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_23, 5, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_12 = QPushButton(self.tab)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(150, 50))
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setStyleSheet(u"background-color:rgb(31, 118, 28); color: white;")

        self.horizontalLayout_3.addWidget(self.pushButton_12)

        self.pushButton_16 = QPushButton(self.tab)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_16.setStyleSheet(u"background-color: rgb(160, 20, 20); color: white;")

        self.horizontalLayout_3.addWidget(self.pushButton_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.tableWidget_7 = QTableWidget(self.tab)
        if (self.tableWidget_7.columnCount() < 10):
            self.tableWidget_7.setColumnCount(10)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font11);
        self.tableWidget_7.setHorizontalHeaderItem(9, __qtablewidgetitem57)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setFont(font4)
        self.tableWidget_7.setSortingEnabled(False)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_4.addWidget(self.tableWidget_7, 2, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_30)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(True)
        self.label_11.setMinimumSize(QSize(150, 75))
        self.label_11.setMaximumSize(QSize(150, 100))
        self.label_11.setFont(font9)
        self.label_11.setTabletTracking(False)
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setStyleSheet(u"")
        self.label_11.setPixmap(QPixmap(u":/image/logo.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(False)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_31)


        self.gridLayout_4.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 8)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        icon5 = QIcon()
        icon5.addFile(u":/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.tableWidget_21 = QTableWidget(self.tab_3)
        if (self.tableWidget_21.columnCount() < 8):
            self.tableWidget_21.setColumnCount(8)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(5, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(6, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font11);
        self.tableWidget_21.setHorizontalHeaderItem(7, __qtablewidgetitem65)
        if (self.tableWidget_21.rowCount() < 10):
            self.tableWidget_21.setRowCount(10)
        self.tableWidget_21.setObjectName(u"tableWidget_21")
        self.tableWidget_21.setFont(font6)
        self.tableWidget_21.setAutoFillBackground(False)
        self.tableWidget_21.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget_21.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget_21.setSortingEnabled(False)
        self.tableWidget_21.setRowCount(10)
        self.tableWidget_21.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_21.verticalHeader().setVisible(False)

        self.gridLayout_37.addWidget(self.tableWidget_21, 2, 1, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_18 = QPushButton(self.tab_3)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.pushButton_18)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_57)

        self.pushButton_43 = QPushButton(self.tab_3)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setFont(font6)
        self.pushButton_43.setStyleSheet(u"background-color: rgb(31, 118, 28); color: white;")

        self.horizontalLayout_33.addWidget(self.pushButton_43)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_60)

        self.lineEdit_18 = QLineEdit(self.tab_3)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_18.setFont(font2)
        self.lineEdit_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.lineEdit_18)


        self.gridLayout_37.addLayout(self.horizontalLayout_33, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_37)

        self.label_39 = QLabel(self.tab_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_39)

        icon6 = QIcon()
        icon6.addFile(u":/image/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_3, icon6, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1043, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Diamond books", None))
        self.actionasdasasdasd.setText(QCoreApplication.translate("MainWindow", u"Qidirish                  F3", None))
        self.actionasdasdas.setText(QCoreApplication.translate("MainWindow", u"Sotish                     F4", None))
        self.actiondasda.setText(QCoreApplication.translate("MainWindow", u"Kichiklashtirish", None))
        self.actionsdas.setText(QCoreApplication.translate("MainWindow", u"sdas", None))
        self.actionKattalashtirish.setText(QCoreApplication.translate("MainWindow", u"Kattalashtirish ", None))
        self.actionKichiklashtirish.setText(QCoreApplication.translate("MainWindow", u"Kichiklashtirish", None))
        self.actionKattalashtirish_2.setText(QCoreApplication.translate("MainWindow", u"Kattalashtirish            F5", None))
        self.actionKichiklashtirish_2.setText(QCoreApplication.translate("MainWindow", u"Kichiklashtirish           F6", None))
        self.actionsssss.setText(QCoreApplication.translate("MainWindow", u"sssss", None))
        self.actionQidirish_F3.setText(QCoreApplication.translate("MainWindow", u"Qidirish            F3", None))
        self.actionSotish_F4.setText(QCoreApplication.translate("MainWindow", u"Sotish               F4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Umumiy hisob</span></p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Qidirish yoki scanner ...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Mahsulot qidirish</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Narx", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Bekor qilish", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sotish", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"so'm", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">sd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kimga", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Naqd", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Plastik", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Nasiya", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Imtiyoz", None))

        self.label.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Qo'shish", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Kamaytirish", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Sotuv 1", None))

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Narxi", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Qoldiq", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Hisob", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"O'chirish", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_2), QCoreApplication.translate("MainWindow", u"Sotuv", None))
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Kelish narxi", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Narxi", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Pachka narxi", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Qoldiq", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Sana", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Buyurtma", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Kimdan", None));
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Yuklab olish", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"  Yangi qo'shish  ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Saqlash ", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u" Buyurtma", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Qidirish", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Jami dasmoya qiymati: 0 so'm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_2), QCoreApplication.translate("MainWindow", u"Ombor", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"[oy / kun / yil]", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"dan", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"gacha", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Filterlash", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Bugun", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Shu hafta", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Bir hafta", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Shu oy", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Bir oy", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Shu yil", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Bir yil", None))

        ___qtablewidgetitem23 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Vaqt", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Umumiy hisob", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"To'lov turi", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Kimga", None));
        ___qtablewidgetitem28 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Kitob nomi", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem31 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Umumiy hisob", None));
        ___qtablewidgetitem32 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"To'lov turi", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Jami sotilganlar qiymati filiter bo'yicha: 0 so'm", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Vazvrat", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3_2), QCoreApplication.translate("MainWindow", u"Sotuv tarixi", None))
        ___qtablewidgetitem33 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem34 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Vaqt", None));
        ___qtablewidgetitem35 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Umumiy hisob", None));
        ___qtablewidgetitem36 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Kimdan", None));
        ___qtablewidgetitem37 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem38 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Kitob nomi", None));
        ___qtablewidgetitem39 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem40 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Umumiy hisob", None));
        ___qtablewidgetitem41 = self.tableWidget_9.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Kelish narx", None));
        ___qtablewidgetitem42 = self.tableWidget_9.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Sotish narxi", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"[oy / kun / yil]", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"dan", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"gacha", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Filterlash", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Bugun", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Shu hafta", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Bir hafta", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Shu oy", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Bir oy", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Shu yil", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"Bir yil", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Jami sotilganlar qiymati filiter bo'yicha: 0 so'm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tovar tarixi", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Mahsulot qidirish</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Umumiy hisob</span></p></body></html>", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Qidirish yoki scanner ...", None))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"so'm", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">sd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kimdan", None))
        ___qtablewidgetitem43 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem44 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem45 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Narx", None));
        ___qtablewidgetitem46 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem47 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Bekor qilish", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Saqlash", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Qo'shish", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Kamaytirish", None))
        ___qtablewidgetitem48 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem49 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem50 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Soni", None));
        ___qtablewidgetitem51 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Kelish Narxi", None));
        ___qtablewidgetitem52 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Narxi", None));
        ___qtablewidgetitem53 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Pachka Narxi", None));
        ___qtablewidgetitem54 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Barcode", None));
        ___qtablewidgetitem55 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Qoldiq", None));
        ___qtablewidgetitem56 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Hisob", None));
        ___qtablewidgetitem57 = self.tableWidget_7.horizontalHeaderItem(9)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"O'chirish", None));
        self.label_11.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Yangi tovar", None))
        ___qtablewidgetitem58 = self.tableWidget_21.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem59 = self.tableWidget_21.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Ism", None));
        ___qtablewidgetitem60 = self.tableWidget_21.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Familiya", None));
        ___qtablewidgetitem61 = self.tableWidget_21.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Telefon raqam", None));
        ___qtablewidgetitem62 = self.tableWidget_21.horizontalHeaderItem(4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Ball", None));
        ___qtablewidgetitem63 = self.tableWidget_21.horizontalHeaderItem(5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem64 = self.tableWidget_21.horizontalHeaderItem(6)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Manzil", None));
        ___qtablewidgetitem65 = self.tableWidget_21.horizontalHeaderItem(7)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Sana", None));
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u" Yuklab olish", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u" Saqlash ", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Qidirish", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Jami ballar qiymati: 0 ball", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Mijozlar", None))
    # retranslateUi

