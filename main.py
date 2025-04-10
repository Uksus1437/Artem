'''На числовой прямой задан отрезок A. Известно, что формула

((x ∈ A) → (x**2 ≤ 100)) ∧ ((x**2 ≤ 64) → (x ∈ A))

тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?'''

# def f(x,y,a):
#     return (5 < y ) or (x >32) or (x + 2 *y <a)

# for a in range(1,100):
#     if all(f(x,y,a) for x in range(1,100) for y in range(1,100)):
#         print(a)
#         break

m = []
for a1 in range(-100, 100):
    for a2 in range(a1+1, 100):
        k = 0
        for x in range(-100,100):
            if (((a1<=x<=a2) <= (x**2 <= 100)) and ((x**2 <= 64) <= (a1<=x<=a2))) == False:
                k = 1
        if k == 0:
             m.append(a2 - a1)
print(max(m))

# 20