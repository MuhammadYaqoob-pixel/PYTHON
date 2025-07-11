def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = 2
b = 9
c = 6
print(greatest(a, b, c))
