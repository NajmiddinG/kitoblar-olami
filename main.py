from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
import sqlite3
import sys, create_table as db

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
        self.pushButton.clicked.connect(self.cancel_buy)
        self.tableWidget.itemChanged.connect(self.handle_item_changed)

        # Timer for the delay
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.search_database)
    def scanner_returned(self):
        scanned_text = self.lineEdit_2.text()
        print(f"Barcode scanned: {scanned_text}")

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
                id = int(self.tableWidget.item(row_index, 0).text())  # Assuming the ID is in column 0
                cur.execute("SELECT narxi FROM Kitob WHERE id=?", (id,))
                narxi = cur.fetchone()[0]
                total_amount += int(narxi) * count
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

            # Populate the tableWidget_2 with the search results
            for row_num, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_2.setItem(row_num, col_num, item)

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
                # Populate the new row with the selected item data
                for col_num, col_data in enumerate(data):
                    item = QTableWidgetItem(str(col_data))
                    if col_num>1: col_num+=1
                    self.tableWidget.setItem(row_position, col_num, item)
                self.tableWidget.setItem(row_position, 2, QTableWidgetItem('1'))
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

        # Fetch data from the "Kitob" table
        cur.execute("SELECT * FROM Kitob")
        data = cur.fetchall()

        # Ensure at least 10 rows in the tableWidget_4
        num_rows_to_add = 10 + len(data)
        self.tableWidget_4.setRowCount(num_rows_to_add)

        # Populate data into tableWidget_4
        for row_number, row_data in enumerate(data):
            for column_number, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.tableWidget_4.setItem(row_number, column_number, item)

        # Add extra rows for creating new elements
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

if __name__ == "__main__":
    App = QApplication(sys.argv)
    wind = window()
    wind.show()
    sys.exit(App.exec())