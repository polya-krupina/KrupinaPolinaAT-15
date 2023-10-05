'''s = input()
if s.count('1') == s.count('0'):
    print('yes')
else:
    print('no')'''
s = input()
count0 = 0
count1 = 0
for i in range(len(s)):
    if s[i] == '1':
        count1 += 1
    elif s[i] == '0':
        count0 += 1
if count0 == count1:
    print('yes')
else:
    print('no')