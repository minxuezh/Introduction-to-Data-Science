# 寫作一個函數 get_fahrenheit() 將攝氏氣溫轉換為華氏氣溫 
def get_fahrenheit(x):
    """
    Transform a Celsius degree into  Farenheit scale
    """
    fah = x * 9/5 + 32
    return fah
print(get_fahrenheit(32))