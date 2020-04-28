player_height = float(input("請輸入球員身高(公尺):"))
player_weight = float(input("請輸入球員體重(公斤):"))
player_bmi = player_weight / player_height**2
bmi_label = None #None 沒有值 每次從新計算不被前面輸入影響
if player_bmi > 30:
  bmi_label = 'Obese'
elif player_bmi > 25: 
  bmi_label = 'Overweight'
elif player_bmi > 18.5:
  bmi_label = 'Normal weight'
else:
  bmi_label = 'Underweight'
print(player_bmi)
print(bmi_label)