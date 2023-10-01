s = input()
result = False
for i in range(10):
    if s.count(str(i)) > 1:
        result = True
        break
print(result)