I. NHIỆM VỤ:

Tìm hiểu và chạy thử dự án nhỏ có kết hợp giữ Flask và SQLite
Tạo 1 bảng dữ liệu bao gồm:
NHANVIEN
idNhanVien (string) suggest sử dụng uuidv4
tenNhanVien (string) 
CCCD (string) <- unique (duy nhất)
email (string) <- unique (duy nhất)
phone (string) <- unique (duy nhất)
Đầu ra: 5 APIs, sử dụng Postman để kiểm tra API nha
1. API danh sách nhân viên Method: GET
2. API tạo nhân viên: POST -> tạo thành công thì gửi email thông báo đến nhân viên đó
3. API cập nhật nhân viên Method: POST / PUT
4. API thông tin nhân viên Method: GET
5. API xóa nhân viên Method: DELETE

II. THỰC HÀNH:
1. Thư viện được sử dụng: SQLite3
2. Tạo class nhanvien
![image](https://user-images.githubusercontent.com/107546980/179411486-5df286d9-f6c8-4545-a9a4-78bc5462a3db.png)

3. Tạo bảng dữ liệu với tên là nhanvientable.db gồm có:
        ID_NhânViên string,
        Tên_NhânViên string,
        CCCD string,
        Email string,
        Phone string
![image](https://user-images.githubusercontent.com/107546980/179411244-cc2f71c8-be2a-4f49-ac5b-701b846a842c.png)
Sử dụng DB Browser for SQLite để kiểm tra và được kết quả như hình

4. Tạo thông tin nhân viên:

![image](https://user-images.githubusercontent.com/107546980/179411542-e8213683-dc62-414c-8913-d87ee4df0212.png)

5. Viết API tạo nhân viên, thông tin nhân viên, tất cả nhân viên có trong ds, cập nhật nhân viên, xóa nhân viên
