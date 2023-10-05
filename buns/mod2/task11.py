'''s = input()
result = False
for i in range(10):
    if s.count(str(i)) > 1:
        result = True
        break
print(result)'''
s = input()
result = False
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j] and s[i] != ' ':
            result = True
            break
print(result)