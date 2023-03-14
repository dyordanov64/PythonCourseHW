# 9. Да се състави програма, която да провери дали е възможно един
# правоъгълник да се вмести изцяло в друг правоъгълник.
# Входни данни: X1, Y1, X2, Y2 - страните на 2-та правоъгълника - естествени числа от
# интервала [5 ..100].

try :
    x1 = int(input('Въведете ширина на 1-вия правоъгълник цяло число ='))
    if x1 < 5 or x1 > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност за ширината на първия правоъгълник')
    exit()

try :
    y1 = int(input('Въведете височина на 1-вия правоъгълник цяло число ='))
    if y1 < 5 or y1 > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност за височината на първия правоъгълник')
    exit()

try :
    x2 = int(input('Въведете ширина на 2-рия правоъгълник цяло число ='))
    if x2 < 5 or x2 > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност за ширината на втория правоъгълник')
    exit()

try :
    y2 = int(input('Въведете височина на 2-рия правоъгълник цяло число ='))
    if y2 < 5 or y2 > 100 :
        raise()
except :
    print('Въвели сте некоректна стойност за височината на втория правоъгълник')
    exit()

if x2 < x1 and y2 < y1 :
    print('Втория правоъгълник се вмества изцяло в първия правоъгълник')
else :
    print('Втория правоъгълник не може да се вмести в първия правоъгълник')