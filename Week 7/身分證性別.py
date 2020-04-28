# 身分證字號性別判斷 
id_number = input("請輸入身分證字號：")
id_second_digit = id_number[1]
if id_second_digit == '1':
    gender = "Male"
else:
    gender = "Female"
print(gender)