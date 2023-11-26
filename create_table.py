import sqlite3

conn = sqlite3.connect("baza.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Kitob (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomi TEXT NOT NULL,
            narxi TEXT NOT NULL,
            barcode TEXT NOT NULL,
            qoldiq TEXT NOT NULL
            )""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS TarixItem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Kitob INTEGER NOT NULL,
            soni INTEGER NOT NULL,
            hisob INTEGER NOT NULL,
            FOREIGN KEY (Kitob) REFERENCES Kitob(id) ON DELETE SET NULL
            )""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Tarix (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TarixItem INTEGER NOT NULL,
            sana TEXT NOT NULL,
            hisob INTEGER NOT NULL,
            FOREIGN KEY (TarixItem) REFERENCES TarixItem(id) ON DELETE SET NULL
            )""")
conn.commit()

# cur.execute("""create table if not exists Ombor (
#             id integer primary key autoincrement,
#             Mahsulot integer not null,
#             holat text not null,
#             miqdor integer not null,
#             pul integer not null,
#             foreign key (Mahsulot) references Mahsulot(id) on delete set null
#             )""")
# conn.commit()

# cur.execute("""create table if not exists Sotish (
#             id integer primary key autoincrement,
#             Mahsulot integer not null,
#             holat text not null,
#             kimga not null,
#             sana text not null,
#             miqdor integer not null,
#             pul integer not null,
#             foyda integer not null,
#             foreign key (Mahsulot) references Mahsulot(id) on delete set null
#             )""")
# conn.commit()

# cur.execute(""" CREATE TABLE if not exists Parol (
# 	        id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             ism	TEXT NOT NULL,
#             familiya	TEXT NOT NULL,
#             login	TEXT NOT NULL,
#             parol	TEXT NOT NULL)
# """)
# conn.commit()