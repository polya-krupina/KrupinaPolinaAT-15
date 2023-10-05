alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
i = s[0]
n = int(s[s.index(',')+1:])
print(alphabet[(alphabet.index(i)+n) % len(alphabet)])