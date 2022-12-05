# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
# после этого завершить программу.
summ_state = []

def my_func(u_str):
    if len(u_str) == 0:
        return
    summ_el = 0
    for el in u_str:
        summ_el += int(el)
    print(summ_el)

while True:
    user_string = input("Введите числа через пробел: ")
    stop_symb = 'q'
    u_list = user_string.split()
    summ_state.extend(u_list)
    if stop_symb in summ_state:
        stop_i = summ_state.index(stop_symb)
        summ_state = summ_state[:stop_i]
        my_func(summ_state)
        break
    print(summ_state)

    my_func(summ_state)