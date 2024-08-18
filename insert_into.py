import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("baza.db")
cur = conn.cursor()

class InsertInto():
    def kitob_add(self, nomi, narxi, barcode, qoldiq):
        cur.execute("""
                        INSERT INTO Kitob (nomi, narxi, barcode, qoldiq)
                        VALUES (?, ?, ?, ?)
                    """, (nomi, narxi, barcode, qoldiq))
        conn.commit()
    def kitob_delete(self):
        cur.execute("""
                    Delete from Kitob
                    """)
        cur.fetchall()
InsertInto().kitob_delete()
# c = InsertInto().kitob_add(nomi=input('Nomi: '), narxi=int(input('Narxi: ')), barcode=input('Barcode: '), qoldiq=int(input("Qoldiq: ")))