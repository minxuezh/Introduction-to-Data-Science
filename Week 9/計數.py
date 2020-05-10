# 隨堂練習：承接上題，介於 x 到 y 之間的奇數有幾個 （包含 x 與 y 假如它們是奇數）
x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_counter = 0 # 歸零
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        #odd_counter = odd_counter + 1 # = NOT ==
        odd_counter += 1 # 計數累計
    #print(odd_counter)
    i += 1 # step
print("======")
print(odd_counter)