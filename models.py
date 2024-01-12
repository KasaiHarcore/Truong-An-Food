from database import Table

class Customer():
    def __init__(self, name, phone, mail, dob):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.dob = dob
        
    def add_customer(self):
        self.name = input("Họ và tên: ")
        self.phone = input("Số điện thoại: ")
        self.mail = input("Mail: ")
        self.dob = input("Ngày tháng năm sinh: ")
        self.points = 0
        Table.insert(self.name, self.phone, self.mail, self.dob, self.points)
        print("Thêm thành công")
        
    def remove_customer(self):
        self.phone = input("Nhập số điện thoại cần xóa: ")
        if Table.cursor().execute("""SELECT * FROM event WHERE phone = ?""", (self.phone,)):
            Table.cursor().execute("""DELETE FROM event WHERE phone = ?""", (self.phone,))
            print("Xóa thành công")
        else:
            print("Không tìm thấy số điện thoại này")
            
    def update_customer(self):
        self.phone = input("Nhập số điện thoại cần sửa: ")
        if Table.cursor().execute("""SELECT * FROM event WHERE phone = ?""", (self.phone,)):
            self.name = input("Họ và tên: ")
            self.mail = input("Mail: ")
            self.dob = input("Ngày tháng năm sinh: ")
            Table.update(self.name, self.phone, self.mail, self.dob)
            print("Sửa thành công")
        else:
            print("Không tìm thấy số điện thoại này")
            
    def find_customer(self, phone):
        if Table.cursor().execute("""SELECT * FROM event WHERE phone = ?""", (phone,)):
            self.info()
            return True
        else:
            print("Không tìm thấy số điện thoại này, có muốn tạo mới không")
            if input("Y/N: ") == "Y":
                self.add_customer()
                return True
            else:
                return False
            
    def info_customer(self):
        result = Table.connection.execute("""SELECT * FROM event WHERE phone = ?""", (self.phone,))
        for row in result:
            self.name = row[1]
            self.phone = row[2]
            self.mail = row[3]
            self.dob = row[4]
            self.points = row[5]
        print(f'Họ và tên: {self.name}')
        print(f'Số điện thoại: {self.phone}')
        print(f'Mail: {self.mail}')
        print(f'Ngày tháng năm sinh: {self.dob}')
        print(f'Điểm tích lũy: {self.points}')
    
            
class Point(Customer):
    def __init__(self, money_in):
        self.money_in = money_in
        self.points = self.money // 10000
        self.money_out = self.money_in - self.point * 10000
        
    def add_point(self, point, phone):
        if self.find_customer(phone):
            self.points = point
            Table.cursor().execute("""UPDATE event SET points = ? WHERE phone = ?""", (self.points, self.phone))
            Table.connection.commit()
            print("Thêm điểm thành công")
        
    def remove_point(self, point):
        if self.points < point:
            print("Số dư điểm không đủ")
            return False
        else:
            self.points -= point
            Table.cursor().execute("""UPDATE event SET points = ? WHERE phone = ?""", (self.points, self.phone))
            Table.connection.commit()
            print("Trừ điểm thành công")