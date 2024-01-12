import sqlite3

class Table():
    def __init__(self, db_files = 'event.db'):
        self.db_files = db_files
        self.connection = sqlite3.connect(self.db_files)
        self.create_table()
        
    def cursor(self):
        return self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.connection.execute("""CREATE TABLE IF NOT EXISTS event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, 
                phone INTEGER, 
                mail TEXT, 
                dob DATETIME, 
                points INTEGER)""")
            self.connection.commit()
            
    def insert(self, name, phone, mail, dob, points):
        with self.connection:
            self.connection.execute("""INSERT INTO event (name, phone, mail, dob, points) VALUES (?, ?, ?, ?, ?)""", (name, phone, mail, dob, points))
            self.connection.commit()
            
    def update(self, name= None, phone = None, mail = None, dob = None):
        with self.connection:
            if self.connection.execute("""SELECT * FROM event WHERE phone = ?""", (phone,)):
                if name:
                    self.connection.execute("""UPDATE event SET name = ? WHERE phone = ?""", (name, phone))
                if mail:
                    self.connection.execute("""UPDATE event SET mail = ? WHERE phone = ?""", (mail, phone))
                if dob:
                    self.connection.execute("""UPDATE event SET dob = ? WHERE phone = ?""", (dob, phone))
                if phone:
                    self.connection.execute("""UPDATE event SET phone = ? WHERE phone = ?""", (phone, phone))
                self.connection.commit()
            else:
                print("Không tìm thấy số điện thoại này, có muốn tạo mới không")
                if input("Y/N: ") == "Y":
                    self.insert(name, phone, mail, dob, 0)
                else:
                    return False
                
    def close(self):
        self.connection.close()