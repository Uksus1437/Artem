'''Текстовый файл состоит из символов A, C, D, F и O.

Определите максимальное количество идущих подряд пар символов вида:

согласная + гласная.

Для выполнения этого задания следует написать программу.
c = 6
      i
CCCAAFOFCCAC

CAFO

Ответ: 95.
'''
f = open('24.txt').readline()
c = 0
c1 = []
gl = 'AO'
sog ='CDF'
i = 0
while i < (len(f)-1):
    x1 = str(f[i])
    x2 = str(f[i+1])
    if ((x1 in sog) and (x2 in gl)):
        i = i+2
        c = c + 2
        c1.append(c)
    else:
        c = 0 
        i =i+1   
otvet = int(max(c1)/2)
print(otvet)
