m = []
s = input()
winner = ''
while s != '':
    m.append([])
    for i in s:
        m[-1].append(i)
    s = input()
flag_d1 = True
flag_d2 = True
for i in range(len(m)):
    if len(set(m[i])) == 1 and m[i][0] != '_':
        winner = m[i][0]
    flag_v = True
    for j in range(1, len(m)):
        if m[j][i] != m[j-1][i]:
            flag_v = False
    if flag_v:
        winner = m[0][i]
    if m[i][i] != m[i-1][i-1]:
        flag_d1 = False
    if m[i][-1-i] != m[-1-i][i]:
        flag_d2 = False
if flag_d1:
    winner = m[0][0]
if flag_d2:
    winner = m[0][-1]
print(winner if winner != '' else 'Ничья')