# 計算 range(1, 101) 的樣本標準差
x = list(range(1,101))
N = len(x)
x_bar = sum(x) / N 
sse = 0
for xi in x:
  #error = xi - x_bar
  squared_error = (xi -x_bar)**2
  sse += squared_error #sse = + squared_error
sample_mse = sse / (N-1)
sample_stdev = sample_mse**(0.5)
print(sample_stdev)