def make_palindrome(word):
    palindrome = []
    for i in range(len(word)):
        palindrome.append('')
    letters_in_word = list(set(word))
    for i in range(len(letters_in_word)):
        if word.count(letters_in_word[i]) % 2 == 0:
            for j in range(len(palindrome)):
                if palindrome[j] == '':
                    palindrome[j] = letters_in_word[i]
                    palindrome[-j-1] = letters_in_word[i]
                    break
        elif len(word) % 2 == 1 and palindrome[len(palindrome) // 2] == '':
            palindrome[len(palindrome) // 2] = letters_in_word[i]
        else:
            break
    palindrome = ''.join(palindrome)
    if len(palindrome) == len(word):
        return palindrome
    return 'Невозможно составить палиндром'


print(make_palindrome('abcabc'))
print(make_palindrome('abcabcd'))
print(make_palindrome('abcabcde'))
print(make_palindrome('leelv'))