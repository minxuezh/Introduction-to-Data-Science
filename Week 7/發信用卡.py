# 隨堂練習:月薪超過4萬或存款超過50萬就發信用卡
monthly_income = input('請輸入月薪:')
saving_account = input('請輸入存款:')
monthly_income = int(monthly_income)
saving_account = int(saving_account )
# 條件判斷(begin)
if monthly_income > 40000:
  ans = "發信用卡"
if saving_account > 500000:
  ans = "發信用卡"
# 條件判斷(end)
print(ans)