# Fizz-Buzz
# 以 input() 函數請使用者輸入一個正整數
# 如果是 3 的倍數印出 "Fizz"
# 如果是 5 的倍數印出 "Buzz"
# 如果是 15 的倍數印出 "Fizz Buzz"
# 其他情況印出該正整數即可
user_int = int(input("請輸入一個正整數:"))
if user_int % 15 == 0:
    print("Fizz Buzz")
elif user_int % 5 == 0:
    print("Buzz")
elif user_int % 3 == 0:
    print("Fizz")
else:
    print(user_int)