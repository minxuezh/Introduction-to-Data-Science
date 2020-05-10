# 隨堂練習：印出介於 x 到 y 之間的奇數（包含 x 與 y 假如它們是奇數)
x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        print(i)
    i += 1 # step