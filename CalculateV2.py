# python CalculateV2.py

import sys
from colorama import init
from colorama import *
init()
from alignment import indem

test = 1
while test == 1:
    test2 = "yes"
    print(Style.BRIGHT)
    print(indem(" "), end="")
    i = float(input("Начальное вложение: "))# Первый бюджет
    print(indem(" "), end="")
    w = float(input("Желаемый итоговый доход(грн.): ")) # Необходимый итоговый доход
    print(indem(" "), end="")
    x = float(input("Введите стоимость вещи в закупке(грн.): ")) # Цена закупки
    print(indem(" "), end="")
    number_y = float(input("Введите коэффициент продажи: "))
    print(indem(" "), end="")
    y = float(x * number_y) # Доход с продажи одного экземпляра
    print("Цена продажи одного экземпляра: " + str(y))
    print(indem(" "), end="")
    percent = float(input("Введите процент повторного вложения в оборот из начального: ")) * float(0.01)
    print(indem(" "), end="")
    percent_profit = float(input("Введите процент вывода из оборота: ")) * float(0.01)
    profit = y - x # Чистая прибыль
     # m = (y / x) * 100  Маржа, выраженная в процентах
    a = (i / x) # Количество товара
    z = (a * y) * (percent) # Процент вложения в следующий оборот
    c = (a * y) * (percent_profit) # Процент вывода в чистую прибыль на текущий месяц
    datalist = [i,w,number_y]
    datalist2 = [percent*100,percent_profit*100]
    datalistsum = ('\033[42m'+str(datalist+datalist2)+'\033[40m')
    print("\n"+('\033[30m'+'\033[22m'+"{0:^78}").format(datalistsum)+'\033[39m'+'\033[1m'+'\n')
    while test2 == "yes":
        n = 1
        a = (i / x) # Количество товара
        c = (a * y) * (percent_profit) 
        z = (a * y) * (percent) # Процент вложения в следующий оборот
        b = (c + z) # Вся выручка
        while n <= 12:
            if (z <= w):
                print(indem(""), end="")
                print(('{0}' + str(n)).format("Месяц:"))
                print(('\033[36m' + '{0:<22}' + '\033[39m' +
                '\033[33m' + '{1:<6}' +'\033[39m'  + '{2:->60}' + str(percent * 100) + "%").format("Последующее вложение: ", str(round(z)), " по проценту: "))
            else:
                break
            print(('\033[36m' + '{0:<22}' + '\033[39m' + '\033[33m' +
            '{1:<6}' + '\033[39m' + '{2:->60}' + str(percent_profit * 100) + "%").format("Чистая прибыль: ", str(round(c)), " по проценту: "))
            print('\033[36m' + "Вся выручка: " + '\033[39m' + '\033[33m' + str(round(b)) + '\033[39m')
            print("Необходимое количество продаваемых вещей в месяц: " + '\033[33m' + str(round(a)) + '\033[39m' + "\n")
            a = (z * percent * number_y) / x # Количество товара
            c = c + (z * percent_profit * number_y) # Вывовод в прибыль с указанным процентом
            b = (z * percent_profit * number_y) + (z * percent * number_y) # Вся выручка
            z *= percent * number_y # Вывовод в оборот с указанным процентом
            n += 1
        print(Fore.CYAN)
        datalist = ["Первое вложение: " + str(i),"Желаемый доход: " + str(w),"Коэффициент продаж: " + str(number_y)]
        datalist2 = ["Процент, идущий в оборот: " + str(percent*100) + "%","Процент, идущий в прибыль: " + str(percent_profit*100) + "%"]
        print("\nЗначения, которые вы ввели: \n" + str(datalist) + "\n" + str(datalist2))
        print(Fore.RESET)
        nx = input("\nВведите одно или несколько значений, которые хотите изменить через пробел(цифры)\n(или нажмите любую другю кнопку для пропуска): ")
        nxx = nx.split()
        try: 
            for element in nxx:
                test2 = "yes"
                n1 = float(element)
                if n1 == number_y:
                    number_y = float(input("Введите коэффициент продажи: "))
                    y = float(x * number_y) # Доход с продажи одного экземпляра
                elif n1 == i:
                    i = float(input("Первостепенное вложение(грн.): "))
                elif n1 == w:
                    w = float(input("Желаемый итоговый доход(грн.): "))
                elif n1 == percent:
                    percent = float(input("Введите коэффициент повторного вложения в оборот: ")) * float(0.01)
                elif n1 == percent_profit:
                    percent_profit = float(input("Введите коэффициент вывода из оборота: ")) * float(0.01)
                else:
                    test2 = "no"
        except ValueError:
            break
    test = input("Хотите закрыть калькулятор?(введите 'y' или 'yes'): ")
    if test == "yes" or test == "y":
        print("End")
        sys.exit()
    else:
        test = 1
