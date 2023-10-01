s = input()
sum1 = 0
sum2 = 0
for i in range(len(s)):
    if i % 2 == 0:
        sum1 += int(s[i])
    else:
        sum2 += int(s[i])
if (sum1 + 3*sum2) % 10 == 0:
    print('yes')
else:
    print('no')