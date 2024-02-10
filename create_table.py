try:
    import sqlite3

    print('\033[94m' + 'Connecting baza.db database' + '\033[0m')

    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()

    print('\033[92m' + 'baza.db is ready' + '\033[0m')

    print('\033[94m' + "Checking it's tables" + '\033[0m')

    cur.execute("""CREATE TABLE IF NOT EXISTS Kitob (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomi TEXT NOT NULL,
                narxi TEXT NOT NULL,
                barcode TEXT NOT NULL,
                qoldiq TEXT NOT NULL,
                kelgan_sana DATE NOT NULL,
                tan_narx TEXT NOT NULL,
                pachka_narx TEXT NOT NULL
                )""")
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS Tarix (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sana DATETIME NOT NULL,
                hisob INTEGER NOT NULL
                )""")
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS TarixItem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Tarix INTEGER NOT NULL,
                Kitob TEXT NOT NULL,
                soni INTEGER NOT NULL,
                hisob INTEGER NOT NULL,
                FOREIGN KEY (Kitob) REFERENCES Kitob(id) ON DELETE SET NULL,
                FOREIGN KEY (Tarix) REFERENCES Tarix(id) ON DELETE SET NULL
                )""")
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS Tovar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kimdan TEXT,
                sana DATETIME NOT NULL,
                hisob INTEGER NOT NULL
                )""")
    conn.commit()

    cur.execute("PRAGMA table_info(Tovar)")
    columns = cur.fetchall()
    column_names = [col[1] for col in columns]

    if 'kimdan' not in column_names:
        cur.execute("ALTER TABLE Tovar ADD COLUMN kimdan TEXT")
        conn.commit()
        print('\033[92m' + "Added 'kimdan' column to Tovar table"+ '\033[0m')
    else:
        print('\033[92m' + "The 'kimdan' column already exists in Tovar table"+ '\033[0m')

    cur.execute("""CREATE TABLE IF NOT EXISTS TovarItem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Tovar INTEGER NOT NULL,
                Kitob TEXT NOT NULL,
                soni INTEGER NOT NULL,
                hisob INTEGER NOT NULL,
                FOREIGN KEY (Kitob) REFERENCES Kitob(id) ON DELETE SET NULL,
                FOREIGN KEY (Tovar) REFERENCES Tovar(id) ON DELETE SET NULL
                )""")
    conn.commit()
    
    print('\033[92m' + 'Database tables are ready' + '\033[0m')
except Exception as e:
    print('\033[91m' + f'Database error: {e}' + '\033[0m')