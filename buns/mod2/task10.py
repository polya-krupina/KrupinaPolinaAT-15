s = input()
result = ''
for i in range(len(s)):
    if s[i] == ' ':
        result += s[i-1]
print(result+s[-1])