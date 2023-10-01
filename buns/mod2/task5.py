alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
i = s[0]
n = int(s[s.index(' '):])
print(alphabet[(alphabet.index(i)+n) % len(alphabet)])