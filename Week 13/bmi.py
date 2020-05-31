# 寫作一個函數 get_bmi() 計算 BMI 身體質量指數 
def get_bmi(height, weight):
    """
    Calculate BMI based on height and weight
    """
    height = height / 100
    bmi = weight / height**2
    return bmi
print(get_bmi(198, 129))