# -*- coding: utf-8 -*-
print("Общество в начале XXI века\n")
year=int(raw_input("Хэй, пользователь! Сколько тебе лет?\n"))
if year < 7 and 0 < year :
    print("Вам в детский сад")
if year >= 7 and 18 > year :
    print("Вам в школу")
if year >=18 and 25 > year :
    print("Вам в универ")
if year >=25 and 60 > year :
    print("Вам на работу")
if year >=60 and 120 > year :
    print("Бога нет. Ты умрешь. Рождайся заново")
else:
    print('Очень смешно\n' * 5)

