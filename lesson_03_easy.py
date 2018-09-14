# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# Version 0.1
#Бредовая версия, но оставлю для себя, как пример работы со строками

# def my_round(number, ndigits):
#
#     st_number = str(number)
#     point = st_number.find('.')
#     position = point + ndigits + 1
#     st_number_sh = st_number[:position]
#     znumber = int(st_number[position:position + 1])
#
#     number = float(st_number_sh)
#
#     if znumber > 4:
#         number = number + 10 ** (ndigits * -1)
#
#     return number
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))

# Version 0.2
def my_round(number, ndigits):

    number = number + 5 / 10 ** (ndigits + 1)
    number = number * 10 ** ndigits
    number = number // 1
    number = number * 10 ** (ndigits * -1)

    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_st = str(ticket_number)

    a = 0
    b = 0
    i = 0

    for x in ticket_number_st:

        if i < 3:
            a += int(x)
        else:
            b += int(x)

        i += 1

    return a == b


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))