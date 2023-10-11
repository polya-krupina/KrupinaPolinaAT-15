s = input().split(' ')
print(*[word[-1] for word in s], sep='')