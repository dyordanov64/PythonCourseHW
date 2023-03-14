# 7. . Високосни години са всички години кратни на 4 с изключения столетията, но
# без столетия кратни на 400, т.е. 1900 не е високосна, но 1600 и 2000 са високосни.
# Съставете програма, която по въведен ден, месец, година отпечатва следващата дата.
# Входни данни: естествени числа за ден, месец, година.
# Пример: 28, 2, 2000 Изход: 1,3,2000

try :
    Den = int(input('Въведета число от [1 .. 31] за ден от месеца ='))
    if Den < 1 or Den > 31 :
        raise()
except :
    print('Въвели сте некоректна стойност за ден')
    exit()

try :
    Mesec = int(input('Въведета число от [1 .. 12] за месеца ='))
    if Mesec < 1 or Mesec > 12 :
        raise()
except :
    print('Въвели сте некоректна стойност за месец')
    exit()

try :
    Year = int(input('Въведета число от [1 .. 2200] за година ='))
    if Year < 1 or Year > 2200 :
        raise()
except :
    print('Въвели сте некоректна стойност за година')
    exit()