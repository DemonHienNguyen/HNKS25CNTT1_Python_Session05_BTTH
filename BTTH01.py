while True:
    total_bill_input = float(input("Nhập tổng tiền hóa đơn ban đầu: "))
    if(total_bill_input < 0):
        print("Tổng hóa đơn không được âm ;-;")
        continue 
    break 

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print(
    f"Số tiền được giảm giá: {total_bill_input * 0.1 if(total_bill_input > 500000) else total_bill_input * 0} VND \n"
    f"Tổng tiền khách phải trả: {total_bill_input - (total_bill_input * 0.1) if(total_bill_input > 500000) else total_bill_input} VNĐ"
)