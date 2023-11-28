from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5 import QtWidgets
import sqlite3
import sys, create_table as db
from datetime import datetime

conn = db.conn
cur = db.cur

def tableResizeMode(table):
    header = table.horizontalHeader()
    for i in range(header.count()):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)


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
        self.setCentralWidget(self.tabWidget)
        self.tab1_clicked()
        self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)

    def handle_tabbar_clicked(self, index):
        if index==0: self.tab1_clicked()
        elif index==1: self.tab2_clicked()
        elif index==2: self.tab3_clicked()
    
    def tab1_clicked(self):
        # print(1)
        self.lineEdit_2.textChanged.connect(self.on_line_edit_changed)
        self.lineEdit_2.returnPressed.connect(self.scanner_returned)
        self.pushButton_5.clicked.connect(self.add_selected_item_to_table)
        self.pushButton_2.clicked.connect(self.accept_buy)
        self.pushButton.clicked.connect(self.cancel_buy)
        self.tableWidget.itemChanged.connect(self.handle_item_changed)

        # Timer for the delay
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.search_database)

    def scanner_returned(self):
        scanned_text = self.lineEdit_2.text()
        # print(f"Barcode scanned: {scanned_text}")

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
                count = int(item.text())
                id = int(self.tableWidget.item(row_index, 0).text())
                cur.execute("SELECT narxi FROM Kitob WHERE id=?", (id,))
                narxi = int(cur.fetchone()[0])
                cur.execute("SELECT qoldiq FROM Kitob WHERE id=?", (id,))
                qoldiq = int(cur.fetchone()[0])
                if count>qoldiq:
                    self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(qoldiq)))
                    count = qoldiq
                total_amount += narxi * count
                self.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(narxi*count)))

        s_text = ''
        money = str(total_amount)[::-1]
        for i in range(len(money)//3+1):
            s_text+=money[3*i:3*i+3]+' '
        self.lineEdit.setText(s_text.strip()[::-1]+" so'm")

    def cancel_buy(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit_2.clear()
        self.lineEdit.setText("0 so'm")

    def accept_buy(self):
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
                kitob_id = int(self.tableWidget.item(row_index, 0).text())
                soni = int(self.tableWidget.item(row_index, 2).text())
                qoldiq = int(self.tableWidget.item(row_index, 5).text())
                hisob = int(self.tableWidget.item(row_index, 6).text())
                cur.execute("UPDATE Kitob SET qoldiq = ? WHERE id = ?", (qoldiq-soni, kitob_id))
                conn.commit()
                cur.execute("INSERT INTO TarixItem (Tarix, Kitob, soni, hisob) VALUES (?, ?, ?, ?)", (tarix_id, kitob_id, soni, hisob))
                conn.commit()
            self.cancel_buy()
    
    def on_line_edit_changed(self):
        # Start the timer when the text in the line edit changes
        self.timer.start(1000)  # 1000 milliseconds = 1 second

    def search_database(self):
        # Perform the database query based on user input
        user_input = self.lineEdit_2.text()
        # Clear the table before populating it with new data
        self.tableWidget_2.setRowCount(0)
        if user_input:
            # Execute your query to search the 'Kitob' table
            query = "SELECT id, nomi, barcode FROM Kitob WHERE nomi LIKE ? OR id LIKE ? OR barcode LIKE ?"
            cur.execute(query, (f'%{user_input}%', f'%{user_input}%', f'%{user_input}%'))
            result = cur.fetchall()
            self.display_data_in_table(result, self.tableWidget_2)

    def add_selected_item_to_table(self):
        selected_item = self.tableWidget_2.currentRow()
        self.lineEdit_2.clear()
        if selected_item>-1:
            id = int(self.tableWidget_2.item(selected_item, 0).text())
            if not self.check_tablewidget_add(id): 
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                cur.execute("SELECT * FROM Kitob WHERE id=?", (id,))
                data = cur.fetchone()
                if int(data[4]):
                    for col_num, col_data in enumerate(data):
                        item = QTableWidgetItem(str(col_data))
                        if col_num>1: col_num+=1
                        self.tableWidget.setItem(row_position, col_num, item)
                    self.tableWidget.setItem(row_position, 2, QTableWidgetItem('1'))
                else:
                    current_row_count = self.tableWidget.rowCount()
                    if current_row_count > 0:
                        self.tableWidget.removeRow(current_row_count - 1)
        self.tableWidget_2.setRowCount(0)

    def check_tablewidget_add(self, id):
        is_present = any(self.tableWidget.item(row_index, 0).text() == str(id)
                 for row_index in range(self.tableWidget.rowCount()))
        return is_present
    
    def tab2_clicked(self):
        # print(2)
        self.populate_tableWidget_4()
        self.pushButton_3.clicked.connect(self.save_tableWidget_data_to_database)
        
    def populate_tableWidget_4(self):   
        # Clear existing data
        self.tableWidget_4.setRowCount(0)

        cur.execute("SELECT * FROM Kitob")
        data = cur.fetchall()

        # Ensure at least 10 rows in the tableWidget_4
        num_rows_to_add = 10 + len(data)
        self.tableWidget_4.setRowCount(num_rows_to_add)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_4.setItem(row_index, col_index, item)

        # self.display_data_in_table(data, self.tableWidget_4)

        for i in range(len(data), num_rows_to_add):
            for j in range(self.tableWidget_4.columnCount()):
                item = QTableWidgetItem("")
                self.tableWidget_4.setItem(i, j, item)

    def save_tableWidget_data_to_database(self):
        # Iterate through rows in tableWidget_4
        for row in range(self.tableWidget_4.rowCount()):
            id = self.tableWidget_4.item(row, 0).text()
            nomi = self.tableWidget_4.item(row, 1).text()
            narxi = self.tableWidget_4.item(row, 2).text()
            barcode = self.tableWidget_4.item(row, 3).text()
            qoldiq = self.tableWidget_4.item(row, 4).text()
            if nomi and narxi and barcode and qoldiq:
                # Check if the record with the same id already exists
                print(nomi, narxi, barcode, qoldiq)
                cur.execute("SELECT id FROM Kitob WHERE id=?", (id,))
                existing_id = cur.fetchone()

                if existing_id:
                    # If the record exists, update it
                    cur.execute("""
                        UPDATE Kitob
                        SET nomi=?, narxi=?, barcode=?, qoldiq=?
                        WHERE id=?
                    """, (nomi, narxi, barcode, qoldiq, existing_id[0]))
                    conn.commit()
                else:
                    # If the record doesn't exist, insert a new one
                    cur.execute("""
                        INSERT INTO Kitob (nomi, narxi, barcode, qoldiq)
                        VALUES (?, ?, ?, ?)
                    """, (nomi, narxi, barcode, qoldiq))
                    conn.commit()
            elif id and not nomi and not narxi and not barcode and not qoldiq:
                cur.execute("DELETE FROM Kitob WHERE id=?", (id,))
        self.populate_tableWidget_4()

    def tab3_clicked(self):
        print(3)
        self.show_tarix()
        self.tableWidget_5.itemSelectionChanged.connect(self.handle_tableWidget_5_selected)

    def handle_tableWidget_5_selected(self):
        selected_items = self.tableWidget_5.selectedItems()
        row = 0
        for item in selected_items: row = int(item.row())
        self.show_table_widget_3(row)
    
    def show_table_widget_3(self, row):
        try:
            tarix_id = int(self.tableWidget_5.item(row, 0).text())
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
    
    def display_data_in_table(self, data, table_widget):
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                table_widget.setItem(row_index, col_index, item)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    wind = window()
    wind.show()
    sys.exit(App.exec())