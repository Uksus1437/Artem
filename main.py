'''
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, 
среди которых ровно по одному разу встречаются буквы A и B.

01234567890123456789
ACCCCBCCCCACCCCBCCCB

CCCCBCCCCACCCC

              i
[[0, 'A'], [5, 'B'], [10, 'A'], [15, 'B'], [19, 'B']]


[0, 'A']    [5, 'B']        10 - 0

[5, 'B'], [10, 'A']             [i+2] - [i-1] - 1    
'''

f = open('24.txt').readline()
ia = []
c = 1
para = 0
for i in range(len(f)):
    x = f[i]
    if x == 'A' or x =='B':
        ia.append([i,x])

p = []
for i in range(1, len(ia)-2):
    if ia[i][1] != ia[i+1][1]:
        p.append(ia[i+2][0] - ia[i-1][0]-1)
print(max(p))
        
        


