# 隨堂練習:印出介於X到Y之間的奇數，包含x和y，如果他們是奇數的話
x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數:"))
i = x
while i <= y:
  if i % 2 == 1:
   print(i)
  i += 1