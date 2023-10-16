def are_numbers_equal(num_list):
    different_numbers = len(set(num_list))
    if different_numbers == 1:
        return 'Все числа равны'
    if different_numbers == len(num_list):
        return 'Все числа разные'
    return 'Есть равные и неравные числа'


print(are_numbers_equal([1, 1, 1, 1]))
print(are_numbers_equal([1, 2, 3, 4]))
print(are_numbers_equal([1, 2, 2, 3]))