# [ IMPORTING ]
import math

# [ START TITLE ]
print(f'{"-"*14} \nВведите данные \n{"-"*14}\n')

# [ SETTINGS ]
first_num = str(input("Введите первое число: ")).strip().lower()
second_num = str(input("Введите второе число: ")).strip().lower()
action = input("Введите знак математического действия: ")

# [ PREPARATION ]
if (first_num == "pi") or (first_num == "n") or (first_num == "p") or (first_num == "number pi") or (first_num == "пи") or (first_num == "п") or (first_num == "число пи") or (first_num == "π"):
    round_up = int(input("До скольки знаков после запятой округлять ПЕРВОЕ число (макс. 15): "))
    first_num = round(math.pi, round_up)
elif (first_num == "e") or (first_num == "е") or (first_num == "и"):
    round_up = int(input("До скольки знаков после запятой округлять ПЕРВОЕ число (макс. 15): "))
    first_num = round(math.e, round_up)
elif (first_num == "tau") or (first_num == "тау"):
    round_up = int(input("До скольки знаков после запятой округлять ПЕРВОЕ число (макс. 15): "))
    first_num = round(math.tau, round_up)
elif (first_num == "True") or (first_num == "Тру") or (first_num == "Труе"):
    first_num = 1
elif (first_num == "False") or (first_num == "Фолс") or (first_num == "Фолсе") or (first_num == "Фалсе"):
    first_num = 0
else:
    first_num = int(first_num)

if (second_num == "pi") or (second_num == "n") or (second_num == "p") or (second_num == "number pi") or (second_num == "пи") or (second_num == "п") or (second_num == "число пи") or (second_num == "π"):
    round_up = int(input("До скольки знаков после запятой округлять ВТОРОЕ число (макс. 15): "))
    second_num = round(math.pi, round_up)
elif (second_num == "e") or (second_num == "е") or (second_num == "и"):
    round_up = int(input("До скольки знаков после запятой округлять ВТОРОЕ число (макс. 15): "))
    second_num = round(math.e, round_up)
elif (second_num == "tau") or (second_num == "тау"):
    round_up = int(input("До скольки знаков после запятой округлять ВТОРОЕ число (макс. 15): "))
    second_num = round(math.tau, round_up)
elif (second_num == "True") or (second_num == "Тру") or (second_num == "Труе"):
    second_num = 1
elif (second_num == "False") or (second_num == "Фолс") or (second_num == "Фолсе") or (second_num == "Фалсе"):
    second_num = 0
else:
    second_num = int(second_num)

# [ ANSWER TITLE ]
print(f'\n{"-"*6} \nОтвет: \n{"-"*6}')

# [ COUNTING ]
if action == "+":
    print(f"{first_num} + {second_num} = {first_num+second_num}")
elif action == "-":
    print(f"{first_num} - {second_num} = {first_num-second_num}")
elif ((action == "/") or (action == ":")) and (second_num != 0):
    print(f"{first_num} / {second_num} = {first_num/second_num}")
elif (action == "*") or (action == "x") or (action == "х"):
    print(f"{first_num} * {second_num} = {first_num*second_num}")
elif (action == "**") or (action == "xx") or (action == "хх"):
    print(f"{first_num} ** {second_num} = {first_num**second_num}")
elif (action == "//") and (second_num != 0):
    print(f"{first_num} // {second_num} = {first_num//second_num}")
elif (action == "%") and (second_num != 0):
    print(f"{first_num} % {second_num} = {first_num%second_num}")
elif ((action == "/") or (action == "//") or (action == "%")) and (second_num == 0):
    print("На ноль делить нельзя")