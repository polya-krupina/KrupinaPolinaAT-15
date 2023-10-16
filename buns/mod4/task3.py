def find_greatest_common_divisor(x, y):
    if x == y:
        return x
    if x > y:
        return find_greatest_common_divisor(x-y, y)
    return find_greatest_common_divisor(x, y-x)


print(find_greatest_common_divisor(100, 10))
print(find_greatest_common_divisor(13, 5))
print(find_greatest_common_divisor(451, 287))