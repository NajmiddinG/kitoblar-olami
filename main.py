from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog, QLabel, QShortcut, QAction
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5 import QtWidgets
from openpyxl import Workbook
from openpyxl.styles import Font
import pandas as pd
import openpyxl
import sqlite3
import sys, create_table as db
from datetime import datetime, date
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor, QKeySequence
from PyQt5.QtCore import Qt, QDate

conn = db.conn
cur = db.cur

def tableResizeMode(table):
    header = table.horizontalHeader()
    for i in range(header.count()):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        header.setStyleSheet("color: black;")


class window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 2400, 1000)
        tableResizeMode(self.tableWidget)
        tableResizeMode(self.tableWidget_2)
        tableResizeMode(self.tableWidget_3)
        tableResizeMode(self.tableWidget_4)
        tableResizeMode(self.tableWidget_5)
        self.sotuv = {} # Dictionary tartib name: (List(book id, number))
        self.curr_sotuv = "Sotuv 1"
        self.setCentralWidget(self.tabWidget)
        self.handle_tabbar_clicked(0)
        try: self.tabWidget.tabBarClicked.disconnect(self.handle_tabbar_clicked)
        except: pass
        self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)
        self.label_change()
        qmenu = self.menuBar()
        qmenu.setStyleSheet("""
            QMenuBar::item:selected {
            background-color: blue;
            color: white;
        }
            QMenuBar::item {
            border: 1px solid blue;
            padding: 5px;
        }
        """)
        # qmenu.action


        shortcut = QKeySequence(Qt.Key_F3)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.Key_F3_function)

        shortcut = QKeySequence(Qt.Key_F4)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.accept_buy)
        self.Key_F3_function()
    
    def Key_F3_function(self):
        self.lineEdit_2.setFocus()

    
    def Key_F3_2_function(self):
        self.lineEdit_3.setFocus()
    
    def label_change(self):
        try:
            text = self.label_3.text()
            index = text.index('Kitob')
            text = text[:index]+'📒 '+text[index:]
            self.label_3.setText(text)

            text = self.label_2.text()
            index = text.index('Umumiy')
            text = text[:index]+'💰 '+text[index:]
            self.label_2.setText(text)
        except:
            pass

    def handle_tabbar_clicked(self, index):
        if index==0: self.tab1_clicked()
        elif index==1: self.tab2_clicked()
        elif index==2: self.tab3_clicked()
        style_sheet = f"QTabBar::tab:selected {{ background-color: rgb(80, 80, 80); }}"
        self.tabWidget.setStyleSheet(style_sheet)
        self.tabWidget.setCurrentIndex(index)
    

    def tab1_clicked(self):
        try: self.lineEdit_2.textChanged.disconnect(self.on_line_edit_changed)
        except: pass
        self.lineEdit_2.textChanged.connect(self.on_line_edit_changed)
        try: self.lineEdit_2.returnPressed.disconnect(self.scanner_returned)
        except: pass
        self.lineEdit_2.returnPressed.connect(self.scanner_returned)
        try: self.pushButton_5.clicked.disconnect(self.add_selected_item_to_table)
        except: pass
        self.pushButton_5.clicked.connect(self.add_selected_item_to_table)
        try: self.pushButton_10.clicked.disconnect(self.add_selected_item_to_new_table)
        except: pass
        self.pushButton_10.clicked.connect(self.add_selected_item_to_new_table)
        try: self.pushButton_2.clicked.disconnect(self.accept_buy)
        except: pass
        self.pushButton_2.clicked.connect(self.accept_buy)
        try: self.pushButton.clicked.disconnect(self.cancel_buy)
        except: pass
        self.pushButton.clicked.connect(self.cancel_buy)
        try: self.tableWidget.itemChanged.disconnect(self.handle_item_changed)
        except: pass
        self.tableWidget.itemChanged.connect(self.handle_item_changed)
        try: self.tableWidget.clicked.disconnect(self.clicked_cancel)
        except: pass
        self.tableWidget.clicked.connect(self.clicked_cancel)
        try: self.comboBox_2.currentIndexChanged.disconnect(self.sell_combo_control)
        except: pass
        self.comboBox_2.currentIndexChanged.connect(self.sell_combo_control)
        try: self.pushButton_8.clicked.disconnect(self.sotuv_table_remove)
        except: pass
        self.pushButton_8.clicked.connect(self.sotuv_table_remove)
        self.Key_F3_function()

        # Timer for the delay
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.search_database)

    def scanner_returned(self):
        scanned_text = self.lineEdit_2.text()

    def clicked_cancel(self, item):
        if item.column() == 7:
            if 0 <= item.row() < self.tableWidget.rowCount():
                self.tableWidget.removeRow(item.row())
            else:
                print(f"Invalid row index: {item.row()}")
            self.calculate()

    def handle_item_changed(self, item):
        # Check if the item is in column 2
        if item.column() == 2:
            try: self.calculate()
            except: self.cancel_buy()

    def calculate(self):
        column_index = 2
        total_amount = 0

        for row_index in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row_index, column_index)

            if item is not None:
                count = int(float(item.text()))
                id = int(float(self.tableWidget.item(row_index, 0).text()))
                cur.execute("SELECT narxi FROM Kitob WHERE id=?", (id,))
                narxi = int(float(cur.fetchone()[0]))
                cur.execute("SELECT qoldiq FROM Kitob WHERE id=?", (id,))
                qoldiq = int(float(cur.fetchone()[0]))
                if count>qoldiq:
                    self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(qoldiq)))
                    count = qoldiq
                total_amount += narxi * count
                self.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(narxi*count)))

        self.lineEdit.setText(self.spacecomma(total_amount)+" so'm")
        self.Key_F3_function()

    def cancel_buy(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit_2.clear()
        self.lineEdit.setText("0 so'm")
        self.Key_F3_function()

    def accept_buy(self):
        try:
            rows = self.tableWidget.rowCount()
            if rows:
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                tex  = self.lineEdit.text()
                umumiy_hisob = ''
                for i in tex:
                    if i.isdigit():
                        umumiy_hisob+=i
                cur.execute("INSERT INTO Tarix (sana, hisob) VALUES (?, ?)", (formatted_datetime, umumiy_hisob))
                conn.commit()
                tarix_id = cur.lastrowid
                for row_index in range(rows):
                    kitob_id = int(float(self.tableWidget.item(row_index, 0).text()))
                    soni = int(float(self.tableWidget.item(row_index, 2).text()))
                    qoldiq = int(float(self.tableWidget.item(row_index, 5).text()))
                    hisob = int(float(self.tableWidget.item(row_index, 6).text()))
                    cur.execute("UPDATE Kitob SET qoldiq = ? WHERE id = ?", (qoldiq-soni, kitob_id))
                    conn.commit()
                    cur.execute("INSERT INTO TarixItem (Tarix, Kitob, soni, hisob) VALUES (?, ?, ?, ?)", (tarix_id, kitob_id, soni, hisob))
                    conn.commit()
        except: pass
        self.cancel_buy()
        self.Key_F3_function()
    
    def on_line_edit_changed(self):
        # Start the timer when the text in the line edit changes
        self.timer.start(1000)  # 1000 milliseconds = 1 second

    def search_database(self):
        # Perform the database query based on user input
        user_input = self.lineEdit_2.text()
        # Clear the table before populating it with new data
        # self.tableWidget_2.setRowCount(0)
        if user_input:
            if len(user_input)>7 and user_input.isdigit():
                query = "SELECT id, nomi, narxi, qoldiq, barcode FROM Kitob WHERE (barcode = ?) AND qoldiq > 0"
                cur.execute(query, (user_input,))
                result = cur.fetchall()
                if len(result)==1:
                    self.display_data_in_table(result, self.tableWidget_2)
                    self.tableWidget_2.selectRow(0)
                    self.add_selected_item_to_table()
                elif len(result)>1:
                    self.tableWidget_2.selectRow(0)
                    self.display_data_in_table(result, self.tableWidget_2)
            else:
                query = "SELECT id, nomi, narxi, qoldiq, barcode FROM Kitob WHERE (nomi LIKE ? OR id LIKE ?) AND qoldiq > 0"
                cur.execute(query, (f'%{user_input}%', f'%{user_input}%'))
                result = cur.fetchall()
                if len(result):
                    self.tableWidget_2.selectRow(0)
                    self.display_data_in_table(result, self.tableWidget_2)

    def sotuv_table_remove(self):
        try: self.pushButton_8.clicked.disconnect(self.sotuv_table_remove)
        except: pass
        try:
            curr_combo = self.comboBox_2.currentIndex()
            curr_combo_text = self.comboBox_2.currentText()
            
            if self.comboBox_2.count()!=1:

                try: del self.sotuv[curr_combo_text]
                except: pass
                a = -1
                self.comboBox_2.clear()
                for key in self.sotuv.keys():
                    if self.sotuv[key]:
                        self.comboBox_2.addItem(key)
                        a+=1
                if a==-1:
                    self.comboBox_2.addItem('Sotuv 1')
                    self.curr_sotuv = 'Sotuv 1'
                else:
                    self.comboBox_2.setCurrentIndex(a)
                    self.curr_sotuv = self.comboBox_2.currentText()
        except: pass
        self.tableWidget.setRowCount(0)
        try:
            curr_sell = self.sotuv[self.comboBox_2.currentText()]
        except: return
        for id, number in curr_sell:
            check = self.check_tablewidget_add(id)
            if check==-1: 
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                if int(float(data[4])):
                    for col_num, col_data in enumerate(data):
                        item = QTableWidgetItem(str(col_data))
                        if col_num>1: col_num+=1
                        self.tableWidget.setItem(row_position, col_num, item)
                    self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(number)))
                    column_position = 7
                    item = QTableWidgetItem('Bekor qilish')
                    background_color = QColor(160, 20, 20)
                    color = QColor(255, 255, 255)
                    item.setBackground(background_color)
                    item.setForeground(color)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.tableWidget.setItem(row_position, column_position, item)
                    item = self.tableWidget.item(row_position, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
                    item = self.tableWidget.item(row_position, 3)
                    item.setBackground(QColor(60, 179, 113))
                    item.setForeground(QColor(255, 255, 255))

                else:
                    current_row_count = self.tableWidget.rowCount()
                    if current_row_count > 0:
                        self.tableWidget.removeRow(current_row_count - 1)
            else:
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                qoldiq = int(data[4])
                prev = int(self.tableWidget.item(check, 2).text())
                if prev<qoldiq:
                    self.tableWidget.setItem(check, 2, QTableWidgetItem(str(prev+1)))
                    item = self.tableWidget.item(check, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
        # self.tableWidget_2.setRowCount(0)
        self.Key_F3_function()
        self.curr_sotuv = self.comboBox_2.currentText()
        self.pushButton_8.clicked.connect(self.sotuv_table_remove)
    def sell_combo_control(self):
        self.sotuv[self.curr_sotuv] = []
        for index in range(self.tableWidget.rowCount()):
            self.sotuv[self.curr_sotuv].append([int(self.tableWidget.item(index, 0).text()), int(self.tableWidget.item(index, 2).text())])
        count = self.comboBox_2.count()
        self.tableWidget.setRowCount(0)
        try:
            curr_sell = self.sotuv[self.comboBox_2.currentText()]
        except: return
        for id, number in curr_sell:
            check = self.check_tablewidget_add(id)
            if check==-1: 
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                if int(float(data[4])):
                    for col_num, col_data in enumerate(data):
                        item = QTableWidgetItem(str(col_data))
                        if col_num>1: col_num+=1
                        self.tableWidget.setItem(row_position, col_num, item)
                    self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(number)))
                    column_position = 7
                    item = QTableWidgetItem('Bekor qilish')
                    background_color = QColor(160, 20, 20)
                    color = QColor(255, 255, 255)
                    item.setBackground(background_color)
                    item.setForeground(color)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.tableWidget.setItem(row_position, column_position, item)
                    item = self.tableWidget.item(row_position, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
                    item = self.tableWidget.item(row_position, 3)
                    item.setBackground(QColor(60, 179, 113))
                    item.setForeground(QColor(255, 255, 255))

                else:
                    current_row_count = self.tableWidget.rowCount()
                    if current_row_count > 0:
                        self.tableWidget.removeRow(current_row_count - 1)
            else:
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                qoldiq = int(data[4])
                prev = int(self.tableWidget.item(check, 2).text())
                if prev<qoldiq:
                    self.tableWidget.setItem(check, 2, QTableWidgetItem(str(prev+1)))
                    item = self.tableWidget.item(check, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
        # self.tableWidget_2.setRowCount(0)
        self.Key_F3_function()
        self.curr_sotuv = self.comboBox_2.currentText()

    def add_selected_item_to_new_table(self):
        current_tartib = self.comboBox_2.currentText()
        self.sotuv[current_tartib] = []
        for index in range(self.tableWidget.rowCount()):
            self.sotuv[current_tartib].append([int(self.tableWidget.item(index, 0).text()), int(self.tableWidget.item(index, 2).text())])
        count = self.comboBox_2.count()
        curr_combo_text = self.comboBox_2.itemText(count - 1).split()[1]
        new_item_text = f'Sotuv {int(curr_combo_text) + 1}'
        self.comboBox_2.addItem(new_item_text)

        # Find the index of the newly added item
        new_item_index = self.comboBox_2.findText(new_item_text)

        self.comboBox_2.setCurrentIndex(new_item_index)
        
        self.curr_sotuv = f'Sotuv {int(curr_combo_text)+1}'
        self.tableWidget.setRowCount(0)
        self.add_selected_item_to_table()

    def add_selected_item_to_table(self):
        selected_item = self.tableWidget_2.currentRow()
        self.lineEdit_2.clear()
        if selected_item>-1:
            id = int(float(self.tableWidget_2.item(selected_item, 0).text()))
            check = self.check_tablewidget_add(id)
            if check==-1: 
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                if int(float(data[4])):
                    for col_num, col_data in enumerate(data):
                        item = QTableWidgetItem(str(col_data))
                        if col_num>1: col_num+=1
                        self.tableWidget.setItem(row_position, col_num, item)
                    self.tableWidget.setItem(row_position, 2, QTableWidgetItem('1'))
                    column_position = 7
                    item = QTableWidgetItem('Bekor qilish')
                    background_color = QColor(160, 20, 20)
                    color = QColor(255, 255, 255)
                    item.setBackground(background_color)
                    item.setForeground(color)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.tableWidget.setItem(row_position, column_position, item)
                    item = self.tableWidget.item(row_position, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
                    item = self.tableWidget.item(row_position, 3)
                    item.setBackground(QColor(60, 179, 113))
                    item.setForeground(QColor(255, 255, 255))

                else:
                    current_row_count = self.tableWidget.rowCount()
                    if current_row_count > 0:
                        self.tableWidget.removeRow(current_row_count - 1)
            else:
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                qoldiq = int(data[4])
                prev = int(self.tableWidget.item(check, 2).text())
                if prev<qoldiq:
                    self.tableWidget.setItem(check, 2, QTableWidgetItem(str(prev+1)))
                    item = self.tableWidget.item(check, 2)
                    item.setBackground(QColor(0, 0, 255))
                    item.setForeground(QColor(255, 255, 255))
        # self.tableWidget_2.setRowCount(0)
        self.Key_F3_function()

    def check_tablewidget_add(self, id):
        is_present = -1
        for row_index in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row_index, 0).text() == str(id):
                is_present=row_index
                break
        return is_present
    
    def tab2_clicked(self):
        self.populate_tableWidget_4()
        try:
            self.pushButton_3.clicked.disconnect(self.save_tableWidget_data_to_database)
        except: pass
        self.pushButton_3.clicked.connect(self.save_tableWidget_data_to_database)
        try:
            self.pushButton_6.clicked.disconnect(self.clicked_export_book)
        except: pass
        self.pushButton_6.clicked.connect(self.clicked_export_book)
        try:
            self.pushButton_4.clicked.disconnect(self.clicked_new_book)
        except: pass
        self.pushButton_4.clicked.connect(self.clicked_new_book)
        try: self.lineEdit_3.textChanged.disconnect(self.on_line_edit_changed)
        except: pass
        self.lineEdit_3.textChanged.connect(self.on_line_edit_changed)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.search_database_2)
        self.Key_F3_2_function()
    
    def search_database_2(self):
        user_input = self.lineEdit_3.text()
        if user_input:
            self.tableWidget_4.setRowCount(0)
            self.populate_tableWidget_4(filter=user_input)
        else: self.populate_tableWidget_4()
        self.Key_F3_2_function()

    def clicked_export_book(self):
        try:
            query = "SELECT * FROM Kitob"
            df = pd.read_sql_query(query, conn)

            file_path, _ = QFileDialog.getSaveFileName(self, 'Save Excel File', '', 'Excel Files (*.xlsx)')

            if file_path:
                # Create a workbook and add a worksheet
                workbook = Workbook()
                worksheet = workbook.active

                # Customize the header row
                header_row = df.columns
                for col_num, value in enumerate(header_row, 1):
                    cell = worksheet.cell(row=1, column=col_num, value=value.title() if type(value)==str else value)
                    cell.font = Font(size=20, bold=True)

                # Add data to the worksheet
                for row_num, (_, row) in enumerate(df.iterrows(), 2):
                    for col_num, value in enumerate(row, 1):
                        worksheet.cell(row=row_num, column=col_num, value=value)

                # Save the workbook to the specified file path
                workbook.save(file_path)
        except: pass
        self.Key_F3_2_function()

    def clicked_new_book(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Excel fileni tanlang', '', 'Excel Files (*.xlsx *.xls)')

            if file_path:
                # Assuming the Excel file has a sheet named 'Sheet1'
                df = pd.read_excel(file_path, header=None, skiprows=1)

                for index, row in df.iterrows():
                    # Assuming the columns are in order: id, book name, price, barcode, qoldiq
                    book_data = (row[0], row[1], row[2], row[3], row[4], row[6], row[7], str(row[5])[:10])
                    # book_data[-1] = book_data[-1][:4]
                    # book_data[-1] = book_data[-1]
                    # Check if the record already exists based on book name
                    cur.execute("SELECT * FROM Kitob WHERE nomi=?", (book_data[1],))
                    existing_record = cur.fetchone()

                    if existing_record is None:
                        """
                        nomi
                        narxi
                        barcode
                        qoldiq
                        kelgan_sana
                        tan_narx
                        pachka_narx
                        """
                        cur.execute("INSERT INTO Kitob (nomi, narxi, barcode, qoldiq, tan_narx, pachka_narx, kelgan_sana) VALUES (?, ?, ?, ?, ?, ?, ?)", book_data[1:])
                    else:
                        existing_qoldiq = existing_record[4]
                        existing_narxi = existing_record[2]
                        new_qoldiq = int(float(existing_qoldiq)) + int(float(book_data[4]))
                        new_narxi = book_data[2]
                        cur.execute("UPDATE Kitob SET qoldiq=?, narxi=?, nomi=?, kelgan_sana=? WHERE id=?", (new_qoldiq, new_narxi, book_data[1], book_data[-1], book_data[0]))

                conn.commit()
                self.populate_tableWidget_4()
        except: pass
        self.Key_F3_2_function()

    def spacecomma(self, value):
        s_text = ''
        money = str(value)[::-1]
        for i in range(len(money)//3+1):
            s_text+=money[3*i:3*i+3]+' '
        return s_text.strip()[::-1]
    
    def populate_tableWidget_4(self, filter=''):
        self.tableWidget_4.setRowCount(0)
        if filter:
            query = "SELECT id, nomi, tan_narx, narxi, pachka_narx, barcode, qoldiq, kelgan_sana FROM Kitob WHERE nomi LIKE ? OR id LIKE ? OR barcode LIKE ? ORDER BY CAST(qoldiq AS SIGNED) DESC"
            cur.execute(query, (f'%{filter}%', f'%{filter}%', f'%{filter}%'))
        else:
            query = "SELECT id, nomi, tan_narx, narxi, pachka_narx, barcode, qoldiq, kelgan_sana FROM Kitob ORDER BY CAST(qoldiq AS SIGNED) DESC"
            cur.execute(query)

        data = cur.fetchall()
        num_rows_to_add = 10 + len(data)
        dasmoya = 0
        self.tableWidget_4.setRowCount(num_rows_to_add)
        for row_index, row_data in enumerate(data):
            dasmoya += int(row_data[2])*int(row_data[6])
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_4.setItem(row_index, col_index, item)
        
        money = self.spacecomma(dasmoya)
        self.label_7.setText("Jami dasmoya qiymati: "+money+" so'm")

        for i in range(len(data), num_rows_to_add):
            for j in range(self.tableWidget_4.columnCount()):
                item = QTableWidgetItem("")
                self.tableWidget_4.setItem(i, j, item)
        self.Key_F3_2_function()

    def save_tableWidget_data_to_database(self):
        # Iterate through rows in tableWidget_4
        for row in range(self.tableWidget_4.rowCount()):
            id = self.tableWidget_4.item(row, 0).text()
            nomi = self.tableWidget_4.item(row, 1).text()
            tan_narx = self.tableWidget_4.item(row, 2).text()
            narxi = self.tableWidget_4.item(row, 3).text()
            pachka_narx = self.tableWidget_4.item(row, 4).text()
            barcode = self.tableWidget_4.item(row, 5).text()
            qoldiq = self.tableWidget_4.item(row, 6).text()
            sana = self.tableWidget_4.item(row, 7).text()
            if nomi and narxi and barcode and qoldiq:
                cur.execute("SELECT id FROM Kitob WHERE id=?", (id,))
                existing_id = cur.fetchone()

                if existing_id:

                    if int((cur.execute("SELECT qoldiq FROM Kitob WHERE id=?", (id,))).fetchone()[0])==int(qoldiq):
                        # If the record exists, update it
                        cur.execute("""
                            UPDATE Kitob
                            SET nomi=?, narxi=?, barcode=?, qoldiq=?, kelgan_sana=?, tan_narx=?, pachka_narx=?
                            WHERE id=?
                        """, (nomi, narxi, barcode, qoldiq, sana, tan_narx, pachka_narx, existing_id[0]))
                        conn.commit()
                    else:
                        cur.execute("""
                            UPDATE Kitob
                            SET nomi=?, narxi=?, barcode=?, qoldiq=?, kelgan_sana=?, tan_narx=?, pachka_narx=?
                            WHERE id=?
                        """, (nomi, narxi, barcode, qoldiq, date.today(), tan_narx, pachka_narx, existing_id[0]))
                        conn.commit()
                else:
                    """
                    nomi
                    narxi
                    barcode
                    qoldiq
                    kelgan_sana
                    tan_narx
                    pachka_narx
                    """
                    cur.execute("""
                        INSERT INTO Kitob (nomi, tan_narx, narxi, pachka_narx, barcode, qoldiq, kelgan_sana)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (nomi, tan_narx, narxi, pachka_narx, barcode, qoldiq, date.today()))
                    conn.commit()
            elif id and not nomi and not narxi and not barcode and not qoldiq:
                cur.execute("DELETE FROM Kitob WHERE id=?", (id,))
                conn.commit()
        self.populate_tableWidget_4()
        self.Key_F3_2_function()

    def tab3_clicked(self):
        # Date
        today = QDate.currentDate()
        self.dateEdit.setDate(today)
        tomorrow = QDate.currentDate().addDays(1)
        self.dateEdit_2.setDate(tomorrow)

        self.show_tarix()
        try: self.tableWidget_5.itemSelectionChanged.disconnect(self.handle_tableWidget_5_selected)
        except: pass
        self.tableWidget_5.itemSelectionChanged.connect(self.handle_tableWidget_5_selected)
        try:
            self.pushButton_7.clicked.disconnect(self.filter_history)
        except: pass
        self.pushButton_7.clicked.connect(self.filter_history)
    
    def filter_history(self):
        self.tableWidget_3.setRowCount(0)
        start_date = self.dateEdit.date().toString("yyyy-MM-dd")
        end_date = self.dateEdit_2.date().toString("yyyy-MM-dd")

        query = "SELECT * FROM Tarix WHERE sana >= ? AND sana <= ? ORDER BY sana DESC"
        cur.execute(query, (start_date, end_date))
        
        tarix_data = cur.fetchall()
        self.display_data_in_table(tarix_data, self.tableWidget_5)
        query_sum = "SELECT SUM(hisob) AS total_hisob FROM Tarix WHERE sana >= ? AND sana <= ?"
        cur.execute(query_sum, (start_date, end_date))  # Replace start_date and end_date with your actual date values
        total_hisob = cur.fetchone()[0]
        if total_hisob is None: total_hisob=0
        self.label_8.setText(f"Jami sotilganlar qiymati filiter bo'yicha: {self.spacecomma(total_hisob)} so'm")

    def handle_tableWidget_5_selected(self):
        self.tableWidget_3.setRowCount(0)
        selected_items = self.tableWidget_5.selectedItems()
        row = 0
        for item in selected_items: row = int(float(item.row()))
        if selected_items: self.show_table_widget_3(row)
    
    def show_table_widget_3(self, row):
        try:
            tarix_id = int(float(self.tableWidget_5.item(row, 0).text()))
            cur.execute("""
                SELECT TarixItem.id, Kitob.nomi, TarixItem.soni, TarixItem.hisob
                FROM TarixItem
                JOIN Kitob ON TarixItem.Kitob = Kitob.id
                WHERE TarixItem.Tarix = ?
            """, (tarix_id,))
            data = cur.fetchall()
            self.display_data_in_table(data, self.tableWidget_3)
        except:
            pass

    def show_tarix(self):
        cur.execute("SELECT * FROM Tarix ORDER BY sana DESC")
        tarix_data = cur.fetchall()
        self.display_data_in_table(tarix_data, self.tableWidget_5)
        cur.execute("SELECT SUM(hisob) FROM Tarix ORDER BY sana DESC")
        total_hisob = cur.fetchone()[0]
        if total_hisob is None: total_hisob=0
        self.label_8.setText(f"Jami sotilganlar qiymati filiter bo'yicha: {self.spacecomma(total_hisob)} so'm")
    
    def display_data_in_table(self, data, table_widget):
        try:
            table_widget.setRowCount(len(data))
            table_widget.setColumnCount(len(data[0]))

            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    table_widget.setItem(row_index, col_index, item)
        except:
            pass

if __name__ == "__main__":
    App = QApplication(sys.argv)
    wind = window()
    wind.show()
    sys.exit(App.exec())