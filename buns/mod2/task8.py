s_i = input()
s = s_i[:s_i.index(',')]
i = s_i[s_i.index(',')+1:]
result = 0
for j in range(len(s)):
    if s[j] == i:
        result += 1
    else:
        break
print(result)