# 球員 BMI 與過重判斷
# 以 input() 函數請使用者輸入球員姓名、身高與體重 
# 計算球員的 BMI 並且印出 
# 超過 30 代表過重，請印出判斷結果
# 球員姓名：俠客歐尼爾、球員身高（cm）：216、球員體重（kg）：147
player_name = input("請輸入球員姓名:")
height_cm = input("請輸入球員身高:")
weight = input("請輸入球員體重:")
height_cm = float(height_cm) 
weight = float(weight) 
player_bmi = weight/(height_cm/100)**2
print("{}的身體質量指數為：{:.2f}".format(player_name, player_bmi))
print("{}是否過重：{}".format(player_name, player_bmi > 30))