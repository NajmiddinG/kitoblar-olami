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
                pachka_narx TEXT NOT NULL,
                buyurtma TEXT NOT NULL,
                kimdan TEXT NOT NULL
                )""")
    conn.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS Tarix (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sana DATETIME NOT NULL,
                hisob INTEGER NOT NULL,
                tolov_turi TEXT NOT NULL DEFAULT 'Naqt'
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
                tan_narx TEXT NOT NULL,
                sotuv_narx TEXT NOT NULL,
                FOREIGN KEY (Kitob) REFERENCES Kitob(id) ON DELETE SET NULL,
                FOREIGN KEY (Tovar) REFERENCES Tovar(id) ON DELETE SET NULL
                )""")
    conn.commit()
    cur.execute("PRAGMA table_info(TovarItem)")
    columns = cur.fetchall()
    column_names = [col[1] for col in columns]

    if 'tan_narx' not in column_names:
        cur.execute("ALTER TABLE TovarItem ADD COLUMN tan_narx TEXT")
        conn.commit()
        print('\033[92m' + "Added 'tan_narx' column to TovarItem table"+ '\033[0m')
    else:
        print('\033[92m' + "The 'tan_narx' column already exists in TovarItem table"+ '\033[0m')
    
    if 'sotuv_narx' not in column_names:
        cur.execute("ALTER TABLE TovarItem ADD COLUMN sotuv_narx TEXT")
        conn.commit()
        print('\033[92m' + "Added 'sotuv_narx' column to TovarItem table"+ '\033[0m')
    else:
        print('\033[92m' + "The 'sotuv_narx' column already exists in TovarItem table"+ '\033[0m')
    
    cur.execute("PRAGMA table_info(Kitob)")
    columns = cur.fetchall()
    column_names = [col[1] for col in columns]

    if 'buyurtma' not in column_names:
        cur.execute("ALTER TABLE Kitob ADD COLUMN buyurtma TEXT DEFAULT '-1'")
        conn.commit()
        print('\033[92m' + "Added 'buyurtma' column to Kitob table"+ '\033[0m')
    else:
        cur.execute("UPDATE Kitob SET buyurtma = '-1' WHERE buyurtma IS NULL")
        conn.commit()
        print('\033[92m' + "The 'buyurtma' column already exists in Kitob table"+ '\033[0m')

    if 'kimdan' not in column_names:
        cur.execute("ALTER TABLE Kitob ADD COLUMN kimdan TEXT DEFAULT 'Nomalum'")
        conn.commit()
        print('\033[92m' + "Added 'kimdan' column to Kitob table"+ '\033[0m')
    else:
        cur.execute("UPDATE Kitob SET kimdan = 'Nomalum' WHERE kimdan IS NULL")
        conn.commit()
        print('\033[92m' + "The 'kimdan' column already exists in Kitob table"+ '\033[0m')
    
    cur.execute("PRAGMA table_info(Tarix)")
    columns = cur.fetchall()
    column_names = [col[1] for col in columns]
    if 'tolov_turi' not in column_names:
        cur.execute("ALTER TABLE Tarix ADD COLUMN tolov_turi TEXT DEFAULT 'Naqt'")
        conn.commit()
        print('\033[92m' + "Added 'tolov_turi' column to Tarix table"+ '\033[0m')
    else:
        cur.execute("UPDATE Tarix SET tolov_turi = 'Nomalum' WHERE tolov_turi IS NULL")
        conn.commit()
        print('\033[92m' + "The 'tolov_turi' column already exists in Tarix table"+ '\033[0m')
    
    print('\033[92m' + 'Database tables are ready' + '\033[0m')
except Exception as e:
    print('\033[91m' + f'Database error: {e}' + '\033[0m')