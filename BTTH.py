check_full_break = ""
hardworking_staff = 0
employees_do_little_work = 0 
working_day_chart = ""
while True:
    try:
        number_employee = int(input("Nhập số lượng nhân viên:"))
    except:
        print("Lỗi ! Dữ liệu nhập vào không phù hợp !")
        continue 
    if(number_employee <= 0):
        print("Só lượng nhân viên phải lớn hơn 0")
        continue 
    print()
    break

for i in range(number_employee):
    print(f"Nhân viên {i+1}")
    employee_name = input("Tên: ")
    while True:
        try:
            day_of_work = int(input("Số ngày làm: "))
        except:
            print("Dữ liệu nhập không phù hợp")
            continue 

        if (day_of_work < 0 or day_of_work > 22):
            print("Số ngày làm không được nhỏ hơn 0 và lớn hơn 22")
            continue 

        break
    
    if (day_of_work == 0):
        check_full_break += f"{employee_name} "

    temp = "*"*day_of_work
        
    working_day_chart += f"{employee_name} : {temp} \n"

    if(day_of_work >= 18):
        hardworking_staff += 1

    if(day_of_work < 10):
        employees_do_little_work += 1

    print()

    
print("=== KIỂM TRA NGHỈ TOÀN BỘ ===")
print(f"Nhân viên nghỉ toàn bộ: {check_full_break} \n")

print("=== BIỂU ĐÒ NGÀY LÀM ===")
print(working_day_chart)
print()

print("=== THỐNG KÊ ===")
print(
    f"Nhân viên chăm chỉ (>= 18): {hardworking_staff} \n"
    f"Nhân viên ít làm (< 10): {employees_do_little_work} \n"
    )








