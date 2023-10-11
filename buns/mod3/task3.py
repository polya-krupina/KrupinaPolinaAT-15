a = input()[::-1].split('.')
print(*[d[::-1] for d in a], sep='\n')