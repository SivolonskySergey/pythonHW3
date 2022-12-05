user_num1, user_num2 = int(input('Делимое: ')), int(input('Делитель: '))
def divider (num1, num2):
    error_f = 'Делить на ноль нельзя!'
    return round(num1 / num2) if num2 != 0 else error_f
print(divider(user_num1, user_num2))