# Да се състави програма, която да изчислява периметър и площ на
# правоъгълник по въведени дължини на прилежащи страни - естествени числа от
# интервала [5 ..100]. Изведете съобщение, ако страните формират квадрат.
# Използвайте проверка на логическо условие - оператор if.
# Пример: 4,4 Изход: квадрат лице 16, периметър 16

# Проверка за коректност на страна b
try :
    Strana_a = int(input('Въведете дължината на страна а на правоъгълник в интервала [5 ..100] ='))
    if Strana_a < 5 or Strana_a > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност за страна a или число извън интервала [5 ..100]')
    exit()

# Проверка за коректност на страна b
try :
    Strana_b = int(input('Въведете дължината на страна b на правоъгълник в интервала [5 ..100] ='))
    if Strana_b < 5 or Strana_b > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност или число извън интервала [5 ..100]')
    exit()

# изчисляване на периметъра и лицето на правоъгълника
P = (Strana_a+Strana_b)*2
S = Strana_a*Strana_b

# проверка дали е квадрат и извеждане съответните съобщения за това както и лицето и периметъра
if Strana_a == Strana_b :
    print(f'квадрат с лице {S} и периметър {P}')
else :
   print(f'правоъгълник с лице {S} и периметър {P}') 