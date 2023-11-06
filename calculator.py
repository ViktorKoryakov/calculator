# [ IMPORTING ]
import math

# [ FUNCTIONS ]
def count_result() -> None:
    """
    Counts and prints the result
    """

    print(f'\n{"-"*6} \nОтвет: \n{"-"*6}')   # [ Answer title ]

    # !!! If you add / delete / edit some kind of action, don't forget edit 'all_actions' list otherwise, the program will not be able to count the result !!!
    if action == '+':
        print(f'{first_num} + {second_num} = {first_num+second_num}')
    elif action == '-':
        print(f'{first_num} - {second_num} = {first_num-second_num}')
    elif (action in ['/', ':']) and (second_num != 0):
        print(f'{first_num} / {second_num} = {first_num/second_num}')
    elif action in ['*', 'x', 'х']:
        print(f'{first_num} * {second_num} = {first_num*second_num}')
    elif action in ['**', 'xx', 'хх', 'xх', 'хx']:
        print(f'{first_num} ** {second_num} = {first_num**second_num}')
    elif (action == '//') and (second_num != 0):
        print(f'{first_num} // {second_num} = {first_num//second_num}')
    elif (action == '%') and (second_num != 0):
        print(f'{first_num} % {second_num} = {first_num%second_num}')
    elif (action in ['/', '//', '%']) and (second_num == 0):
        print('На ноль делить нельзя')
    else: pass

def is_valid_number(num: str, order: int) -> str | float:
    """
    Checks the transmitted number for correctness
    and, if necessary, converts it to special numbers
    """

    while True:
        if ('0' in num) or ('1' in num) or ('2' in num) or ('3' in num) or ('4' in num) or ('5' in num) or ('6' in num) or ('7' in num) or ('8' in num) or ('9' in num):
            try:
                return float(num)
            except ValueError:
                print(f'Принимаются только целые, дробные, а также особые (пи, е и т.д.) числа. Вы ввели: {num}. Попробуйте ещё раз. \n')
                if order == 1:
                    num: str = input('Введите первое число: ').strip().lower()
                elif order == 2:
                    num: str = input('Введите второе число: ').strip().lower()
                else: pass
                continue   # start cycle again
        else:
            if num in ['pi', 'n', 'p', 'number pi', 'пи', 'п', 'число пи', 'π', 'e', 'е', 'и', 'tau', 'тау']:
                while True:
                    if order == 1:
                        round_up: int = input('До скольки цифр после запятой округлять ПЕРВОЕ число (мин. 0; макс. 15): ')
                    elif order == 2:
                        round_up: int = input('До скольки цифр после запятой округлять ВТОРОЕ число (мин. 0; макс. 15): ')
                    else: pass

                    try:
                        round_up = int(round_up)
                        if (round_up <= 15) or (round_up >= 0):
                            break
                        else:
                            print(f'Разрешено: Минимум - 0 цифр, Максимум - 15 цифр. Вы ввели: {round_up}. Попробуйте ещё раз. \n')
                            continue   # start sub-cycle again
                    except ValueError:
                            print(f'Принимаются только целые числа. Вы ввели: {round_up}. Попробуйте ещё раз. \n')
                            continue   # start sub-cycle again
                    except TypeError:
                            print(f'Принимаются только целые числа. Вы ввели: {round_up}. Попробуйте ещё раз. \n')
                            continue   # start sub-cycle again
                    
                if num in ['pi', 'n', 'p', 'number pi', 'пи', 'п', 'число пи', 'π']:
                    return round(math.pi, round_up)
                elif num in ['e', 'е', 'и']:
                    return round(math.e, round_up)
                elif num in ['tau', 'тау']:
                    return round(math.tau, round_up)
                else: pass
                    

            elif num in ['True', 'Тру', 'Труе']:
                return 1
            elif num in ['False', 'Фолс', 'Фолсе', 'Фалсе']:
                return 0
            else:
                print(f'Принимаются только целые, дробные, а также особые (пи, е и т.д.) числа. Вы ввели: {num}. Попробуйте ещё раз. Если Вы уверены, что произошла ошибка - свяжитесь с создателем проекта. \n')
                if order == 1:
                    num: str = input('Введите первое число: ').strip().lower()
                elif order == 2:
                    num: str = input('Введите второе число: ').strip().lower()
                else: pass
                continue   # start cycle again

# [ START TITLE ]
print(f'{"-"*14} \nВведите данные \n{"-"*14}\n')

# [ SETTINGS ]
first_num: str = input('Введите первое число: ').strip().lower()
first_num = is_valid_number(first_num, 1)
second_num: str = input('Введите второе число: ').strip().lower()
second_num = is_valid_number(second_num, 2)
action: str = input('Введите знак математического действия: ')

# [ COUNTING ]
all_actions = ['+', '-', '/', ':', '*', 'x', 'х', '**', 'xx', 'хх', 'xх', 'хx', '//', '%']

while True:
    if action in all_actions:
        count_result()
        break
    else:
        while True:
            print('Знак математического действия не распознан. Попробуйте, пожалуйста, ещё раз. \n')
            action: str = input('Введите знак математического действия: ')
            break
