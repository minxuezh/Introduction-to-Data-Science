# 判斷bob出現的次數
test_str = 'azcbobobegghakl'
n_char = len(test_str)
n_bobs = 0
for i in range(n_char - 2):
  #print(test_str[i:i+3])
  if test_str[i:i+3] == 'bob':
    n_bobs += 1
print(n_bobs)