import mysql.connector

def trinhsatthongtin():
    # Kết nối đến MySQL
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",  # Thay username bằng tên đăng nhập của bạn
        # password="password",  # Thay password bằng mật khẩu của bạn
        database="trinhsatthongtin"  # Thay databasename bằng tên cơ sở dữ liệu bạn muốn truy cập
    )

    cursor = connection.cursor()

    try:
        # Truy vấn để lấy tất cả dữ liệu từ bảng "object"
        cursor.execute("SELECT * FROM object")

        # Lấy tất cả các dòng dữ liệu từ kết quả của truy vấn
        rows = cursor.fetchall()

        # In ra thông tin của từng dòng
        for row in rows:
            print(row)

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Đóng kết nối
        if connection.is_connected():
            cursor.close()
            connection.close()


trinhsatthongtin()
