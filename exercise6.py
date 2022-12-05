# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

user_str = input("Введите слова в нижнем регистре через пробел: ")

def int_func (u_str):
    first_letter = u_str[:1]
    upper_id = ord(first_letter) - 32
    return f'{chr(upper_id)}{u_str[1:]}'

#print(int_func(user_str))

def all_to_upper(def_str):
    to_list = def_str.split(' ')
    result_list = []
    for item in to_list:
        new_item = int_func(item)
        result_list.append(new_item)
    return ' '.join(result_list)
print(all_to_upper(user_str))