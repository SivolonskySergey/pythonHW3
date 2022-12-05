user_num1, user_num2, user_num3 = int(input("Число 1: ")),\
                                  int(input("Число 2: ")),\
                                  int(input("Число 3: "))

def summ_of_max(num1, num2, num3):
    to_list = [num1, num2, num3]
    to_list.sort()
    return f"{to_list[1]} + {to_list[2]} = {to_list[1] + to_list[2]}"

print(summ_of_max(user_num1, user_num3, user_num2))