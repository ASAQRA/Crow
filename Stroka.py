# -*- coding: utf-8 -*-
str1=raw_input("Введите строку\n")
str2=str1.split(' ')
dlina=0
for rob in str2:
    if len(rob) > dlina:
         dlina=len(rob)
    else:
        pass
for rob in str2:
    if len(rob) == dlina:
        print rob
    else:
        pass