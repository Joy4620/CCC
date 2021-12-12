procedure = input()
h, v = procedure.count('H')%2, procedure.count('V')%2
a, b, c, d = 1, 2, 3, 4

if h:
    x = a
    a = c
    c = x
    x = d
    d = b
    b = x

if v:
    x = a
    a = b
    b = x
    x = d
    d = c
    c = x

print(f'{a} {b} \n{c} {d}')
