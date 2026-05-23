doanh_thu = 0
ngay_trong_tuan = 7
doanh_thu_tren = 0
LINE = "-"*40
for i in range(ngay_trong_tuan):
    while True:
        try:
            temp_doanh_thu = int(input(f"Nhập doanh thu ngày thứ {i+1}: "))
        except:
            print("Lỗi: Dữ liệu nhập vào không hợp lệ !")
            continue 
        
        if (temp_doanh_thu < 0):
            print("Doanh thu không được âm !")
            continue 
        
        if(temp_doanh_thu > 5000000):
            doanh_thu_tren += 1

        doanh_thu += temp_doanh_thu
        break

print(LINE)
print("--- BÁO CÓA DOANH THU TUẦN RIKKEI STORE ---")
print(
    f"Tổng doanh thu cả tuần: {f"{doanh_thu:,}".replace(",", ".")} VND \n"
    f"Doanh thu trung bình mỗi ngày: {f"{round(float(doanh_thu / ngay_trong_tuan)):,.2f}".replace(",", ".")} VND \n"
    f"Số ngày đạt doanh thu mục tiêu (>= 5.000.000 VND): {doanh_thu_tren}"
)
print(LINE)
    