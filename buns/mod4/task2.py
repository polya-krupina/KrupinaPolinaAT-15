def power(a, n):
    if n == 1:
        return a
    if n % 2 == 1:
        return a * power(a, n-1)
    return power(a**2, n//2)


print(power(2, 10))
print(power(2, 11))