import sqlite3
from sqlite3.dbapi2 import connect
from nhanvien import nhanvien


conn = sqlite3.connect('nhanvientable.db')

nvien1 = nhanvien(1, 'Hồ Văn Tiến Dũng', 201795925, 'hvtd2110@gmail.com', 705953265)

c = conn.cursor()

# Tạo bảng dữ liệu
sql_create_table = """
    CREATE TABLE nhanvien (
        ID_NhânViên string,
        Tên_NhânViên string,
        CCCD string,
        Email string,
        Phone string
    )
"""

# Tạo nhân viên
sql_insert = f"""
    INSERT INTO nhanvien VALUES (:ID_NhânViên, :Tên_NhânViên, :CCCD, :Email, :Phone)
"""
def insert_nhanvien(nvien):
    with conn:
        c.execute(sql_insert, {'ID_NhânViên': nvien.ID_NhânViên, 'Tên_NhânViên': nvien.Tên_NhânViên, 'CCCD': nvien.CCCD, 'Email': nvien.Email, 'Phone': nvien.Phone})
        print("INSERT SUCCESSFULLY!!!!!!!")


# Thông tin nhân viên
sql_select1 = """
    SELECT *FROM nhanvien WHERE ID_NhânViên =:ID_NhânViên
"""
def get_nhanvien_by_idNhanvien(ID_NhânViên):
    with conn:
        c.execute(sql_select1, {'ID_NhânViên': ID_NhânViên})
        # return c.fetchall()


# Thông tin tất cả nhân viên trong DS
sql_select = """
    SELECT *FROM nhanvien
"""
def get_dsnhanvien(nhanvien):
    with conn:
        c.execute(sql_select, {'nhanvien': nhanvien})


# Cập nhật nhân viên
sql_update = """
    UPDATE nhanvien set Tên_NhânViên = :Tên_NhânViên WHERE ID_NhânViên = :ID_NhânViên
"""
def update_nhanvien(ID_NhânViên, Tên_NhânViên):
    with conn:
        c.execute(sql_update, {'ID_NhânViên': ID_NhânViên, 'Tên_NhânViên': Tên_NhânViên})


# Xóa nhân viên
sql_delete = """
    DELETE from nhanvien WHERE Tên_NhânViên = :Tên_NhânViên
"""
def delete_nhanvien(Tên_NhânViên):
    with conn:
        c.execute(sql_delete, {'Tên_NhânViên': Tên_NhânViên})


nvien1 = nhanvien(5, 'Nguyễn Văn C', '12345678', 'nguyenvanc@gmail.com', '0905123456')


try:
    get_dsnhanvien(nhanvien)
    print(c.fetchall())
except:
    print("Lỗi!!!!!!!!")

conn.close()