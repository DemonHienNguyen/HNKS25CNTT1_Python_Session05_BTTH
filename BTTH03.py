import sys 
doanh_thu_cao_nhat = -sys.maxsize 
doanh_thu_thap_nhat = sys.maxsize

while True:
    try:
        tong_so_luong_hoa_don = int(input("Nhập số lượng hóa đơn tỏng ca: "))
    except:
        print("Lỗi: Dữ liệu nhập không hợp lệ")
        continue 

    if (tong_so_luong_hoa_don < 0):
        print("Số lượng đơn hàng không được âm !")
        continue 
    break 

for i in range(tong_so_luong_hoa_don):

    while True:
        try:
            temp_gia_tri_hoa_don = int(input(f"Nhập giá trị hóa đơn thứ {i+1}: "))
        except:
            print("Lỗi Dữ liệu nhập vào không hợp lệ !")
            continue 
        
        if (temp_gia_tri_hoa_don < 0):
            print("LỖI: Giá trị hóa đơn không được âm !")
            continue 

        break

    if (temp_gia_tri_hoa_don < doanh_thu_thap_nhat):
        doanh_thu_thap_nhat = temp_gia_tri_hoa_don

    if (temp_gia_tri_hoa_don > doanh_thu_cao_nhat):
        doanh_thu_cao_nhat = temp_gia_tri_hoa_don

print("-- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(
    f"Hóa đơn có giá trị cao nhất: {f"{doanh_thu_cao_nhat:,}".replace(",", ".")}  VND \n"
    f"Hóa đơn có giá trị thấp nhất: {f"{doanh_thu_thap_nhat:,}".replace(",", ".")}  VND"
)



