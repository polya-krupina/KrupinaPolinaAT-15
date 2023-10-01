s = input()
current_domain = ''
for i in range(len(s)):
    if s[i] == '.':
        print(current_domain)
        current_domain = ''
    else:
        current_domain += s[i]
print(current_domain)