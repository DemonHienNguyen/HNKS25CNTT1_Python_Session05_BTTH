LINE = "-" * 67
count_order = 0
revenue = 0.0
count_revenue_up_one_million = 0
while True:
    try: 
        costomer_bill = float(input(f"Khách hàng {count_order + 1} - Nhập giá trị hóa đơn: "))
    except:
        print("Dữ liệu nhập vào không phù hợp !")
        continue 

    if (costomer_bill < 0):
        print("Lỗi ! giá trị hóa đơn không được âm !")
        continue 
    
    if (costomer_bill > 1000000):
        count_revenue_up_one_million += 1


    revenue += costomer_bill
    count_order += 1

    while True:
        conti = input("Có muốn nhập tiếp không ? (C/K): ").lower()
        if(conti not in ["c", "k"]):
            print("Lỗi : Bạn chỉ được nhập C - Có hoặc K - Không !")
            continue 

        break 

    if (conti == "k"):
        break 

print(LINE)
print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print(
    f"Tổng số hóa đơn đã xử lý: {count_order} hóa đơn \n"
    f"Tổng doanh thu ngày hôm nay: {f"{revenue:,}".replace(",", ".")} VND\n"
    f"Số hóa đơn lớn (>= 1.000.000 VND): {count_revenue_up_one_million} hóa đơn\n"
    f"Tỷ lệ hóa đơn lớn đạt: {float((count_revenue_up_one_million / count_order)* 100)}% trên tổng số đơn hàng\n"
)
print(LINE)
