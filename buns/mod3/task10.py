def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=(', ' if j < len(matrix)-1 else ''))
        print()
def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_matrix.append([])
        for j in range(len(matrix)):
            transposed_matrix[i].append(first_matrix[j][i])
    return transposed_matrix
first_matrix = []
size = int(input())
for i in range(0, size):
    first_matrix.append([])
    for j in range(0, size):
        first_matrix[i].append(j+1)
print_matrix(first_matrix)
print()
print_matrix(transpose_matrix(first_matrix))