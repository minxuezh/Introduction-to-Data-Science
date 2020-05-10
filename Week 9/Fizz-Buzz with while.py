# 從 1 印到 100 如果是 3 的倍數印出 "Fizz"，如果是 5 的倍數印出 "Buzz"，如果是 15 的倍數印出 "Fizz Buzz"，其他情況印出該正整數即可
i = 1 # start
while i <= 100: # stop
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1 # step