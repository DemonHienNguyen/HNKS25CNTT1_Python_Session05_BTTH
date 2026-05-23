import random 
lucky_number = random.randint(0, 10)
lucky_number = 79

count = 0

while count < 5 :
    try:
        lucky_guest = int(input(f"Lượt đoán thứ {count + 1} - Nhập số của bạn: "))
    except:
        print("Lỗi: Nhập sai kiểu dữ liệu !")
        continue 


    if (lucky_guest < lucky_number):
        print("Gợi ý: Số của bạn nhỏ hơn số may mắn")
        count += 1

    if(lucky_guest > lucky_number):
        print("Gợi ý: Số của bạn lớn hơn hơn số may mắn")
        count += 1

    if(lucky_guest == lucky_number):
        print("=> Chúc mừng ! Bạn đã đoán chính xác mã số may mắn")
        break 
    
    if(count == 5 and lucky_guest != lucky_number):
        print(f"Bạn vẫn chưa đoán được số may mắn của mình :D là {lucky_number}")
        break

print("--- TRÒ CHƠI KẾT THÚC ---")