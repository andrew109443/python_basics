# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def fun_1(a=int(input('Введите первое число: ')),b=int(input('Введите второе число: '))):
    try:
        return ( a / b )
    except ZeroDivisionError:
        return ('Zero division, try another number')
print(fun_1())

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def fun_2_1(first_name, last_name, year, city, email, phone):
    return first_name + ' ' + last_name + ' ' + year + ' ' + city + ' ' + email + ' ' + phone

def fun_2_2(**kwargs):
    return kwargs

print(fun_2_1(first_name = 'Ivan', last_name = 'Ivanov', year = '1917', city = 'Moscow', email = 'bender@ilovebender.com', phone = '55500555'))
print(fun_2_2(first_name = 'Ivan', last_name = 'Ivanov', year = '1917', city = 'Moscow', email = 'bender@ilovebender.com', phone = '55500555'))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def fun_3(arg_1, arg_2, arg_3):
    l = [arg_1, arg_2, arg_3]
    a = l.pop(l.index(min(l)))
    return sum(l)

print(fun_3(1,2,3))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа
# x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def fun_4_1(x, y):
    return x ** y

print(fun_4_1(2, -1))

# # 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# # # Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# # к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# # Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

def fun_5():
    list = input('Введите строку чисел, разделённых пробелом: ').split(' ')
    a = []
    for num in list:
        if num.upper() != 'Q':
            a.append(int(num))
        else:
            return sum(a)
            break
    return sum(a)
print(fun_5())

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def fun_6_1(a):
    return(str(a).capitalize())

def fun_6_2(b):
    a = ''
    list = str(b).split(' ')
    for l in list:
        a += ' ' + (fun_6_1(l))
    return a

print(fun_6_2('dsasdad dsadasd dasdasd'))