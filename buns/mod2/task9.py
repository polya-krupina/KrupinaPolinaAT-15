consonants = 'бвгджзйклмнпрстфхцчшщ'
vowels = 'аеёиоуыэюя'
s = input()
consonants_count = 0
vowels_count = 0
for i in range(len(s)):
    if s[i] in consonants:
        consonants_count += 1
    if s[i] in vowels:
        vowels_count += 1
print(vowels_count, consonants_count)