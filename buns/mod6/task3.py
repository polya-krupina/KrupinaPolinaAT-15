def is_armstrong_number(n):
    number = str(n)
    number_length = len(number)
    armstrong_sum = sum(int(figure) ** number_length for figure in number)
    return armstrong_sum == n


def armstrong_numbers_generator():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1


def get_armstrong_numbers():
    return next(armstrong_generator)


armstrong_generator = armstrong_numbers_generator()
for i in range(8):
    print(get_armstrong_numbers(), end=' ')