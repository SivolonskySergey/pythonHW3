user_num1, user_num2 = float(input("Введите положительное число: ")),\
                       int(input("Введите целое отрицательное число: "))

def my_func(x, y):
    result = x
    counter = 0
    while counter < (y * (-1)):
        result = result * x
        counter+=1
    return 1 / result

print(my_func(user_num1, user_num2))