# 隨堂練習：依身分證字號尾數決定星期幾可以購買口罩 
## 奇數：星期一三五日領 
## 偶數：星期二四六日領
id_last_digit = input("請輸入您身分證字號的尾數:")
id_last_digit = int(id_last_digit)
if id_last_digit % 2 == 0:
  ans = "星期二四六日領"
else:
  ans = "星期一三五日領"
print(ans)