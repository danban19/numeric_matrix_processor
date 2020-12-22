from copy import deepcopy


def greetings():  # prints greetings and actions to choose from
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    action = input('Your choice:')
    if action == '1':
        add_matrices()
    elif action == '2':
        multiply_by_constant()
    elif action == '3':
        multiply_matrices()
    elif action == '4':
        transposition()
    elif action == '5':
        determinant_calculation()
    elif action == '6':
        matrix_inversion()
    elif action == '0':
        exit()
    else:
        greetings()


def add_matrices():  # adds 2 matrices
    matrix1 = []
    matrix2 = []
    output_matrix = []
    matrix1_dimensions = [int(element) for element in input('Enter size of first matrix:').split(' ')]
    print('Enter first matrix:')
    for i in range(matrix1_dimensions[0]):
        matrix1.append([float(element) for element in input().split(' ')])
    matrix2_dimensions = [int(element) for element in input('Enter size of second matrix:').split(' ')]
    print('Enter second matrix:')
    for i in range(matrix2_dimensions[0]):
        matrix2.append([float(element) for element in input().split(' ')])

    if matrix1_dimensions == matrix2_dimensions:  # checks if dimensions of matrices are the same
        for i in range(matrix1_dimensions[0]):
            output_matrix.append([str(matrix1[i][j] + matrix2[i][j]) for j in range(matrix1_dimensions[1])])
        print('The result is:')
        for row in output_matrix:
            print(' '.join(row))
    else:  # if dimensions aren't the same, the operation cannot be performed
        print('The operation cannot be performed.')
    greetings()


def multiply_by_constant():  # multiplies an array by a constant
    matrix1 = []
    output_matrix = []
    matrix1_dimensions = [int(element) for element in input('Enter size of matrix:').split(' ')]
    print('Enter matrix:')
    for i in range(matrix1_dimensions[0]):
        matrix1.append([float(element) for element in input().split(' ')])
    constant = float(input('Enter constant:'))
    for i in range(matrix1_dimensions[0]):
        output_matrix.append([str(matrix1[i][j] * constant) for j in range(matrix1_dimensions[1])])
    print('The result is:')
    for row in output_matrix:
        print(' '.join(row))
    greetings()


def multiply_matrices():  # multiplies 2 matrices
    matrix1 = []
    matrix2 = []
    matrix1_dimensions = [int(element) for element in input('Enter size of first matrix:').split(' ')]
    print('Enter first matrix:')
    for i in range(matrix1_dimensions[0]):
        matrix1.append([float(element) for element in input().split(' ')])
    matrix2_dimensions = [int(element) for element in input('Enter size of second matrix:').split(' ')]
    print('Enter second matrix:')
    for i in range(matrix2_dimensions[0]):
        matrix2.append([float(element) for element in input().split(' ')])

    output_matrix = [[0 for row in range(matrix2_dimensions[1])] for col in range(matrix1_dimensions[0])]
    if matrix1_dimensions[1] == matrix2_dimensions[0]:
        for i in range(matrix1_dimensions[0]):
            for j in range(matrix2_dimensions[1]):
                for k in range(matrix1_dimensions[1]):
                    output_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        print('The result is:')
        for row in output_matrix:
            print(' '.join([str(element) for element in row]))
    else:
        print('The operation cannot be performed.')
    greetings()


def transposition():  # transposition of an array
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    matrix1 = []
    transposition_action = input('Your choice:')
    matrix1_dimensions = [int(element) for element in input('Enter matrix size:').split(' ')]
    output_matrix = []
    print('Enter matrix:')
    for i in range(matrix1_dimensions[0]):
        matrix1.append([float(element) for element in input().split(' ')])
    if transposition_action == '1':  # transposition by main diagonal
        for i in range(matrix1_dimensions[0]):
            output_matrix.append([str(matrix1[j][i]) for j in range(matrix1_dimensions[1])])
        print('The result is:')
        for row in output_matrix:
            print(' '.join(row))

    elif transposition_action == '2':  # transposition side diagonal
        for i in range(matrix1_dimensions[0]):
            output_matrix.append([str(matrix1[matrix1_dimensions[0] - j - 1][matrix1_dimensions[0] - i - 1])
                                  for j in range(matrix1_dimensions[1])])
        print('The result is:')
        for row in output_matrix:
            print(' '.join(row))

    elif transposition_action == '3':  # transposition vertical diagonal
        for i in range(matrix1_dimensions[0]):
            output_matrix.append([str(matrix1[i][matrix1_dimensions[0] - j - 1]) for j in range(matrix1_dimensions[1])])
        print('The result is:')
        for row in output_matrix:
            print(' '.join(row))

    elif transposition_action == '4':  # transposition horizontal diagonal
        for i in range(matrix1_dimensions[0]):
            output_matrix.append([str(matrix1[matrix1_dimensions[0] - i - 1][j]) for j in range(matrix1_dimensions[1])])
        print('The result is:')
        for row in output_matrix:
            print(' '.join(row))


def determinant_calculation():  # calculates matrix determinant
    matrix = []
    matrix_dimensions = [int(element) for element in input('Enter matrix size:').split(' ')]
    print('Enter matrix:')
    for i in range(matrix_dimensions[0]):
        matrix.append([float(element) for element in input().split(' ')])
    determinant = laplace_expansion(matrix)  # goes to determinant calculation using laplace expansion
    print('The result is:')
    print(determinant)


def laplace_expansion(matrix):  # determinant calculation using laplace expansion
    determinant = 0
    if len(matrix) == 1:
        determinant += matrix[0][0]
    elif len(matrix) == 2:
        determinant += matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(len(matrix)):
            cofactor = (-1) ** i * matrix[0][i] * laplace_expansion(matrix_reduction(matrix, 0, i))
            determinant += cofactor
    return determinant


def matrix_reduction(original_matrix, row, column):  # reduces the matrix
    new_matrix = deepcopy(original_matrix)
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].pop(column)
    return new_matrix


def matrix_inversion():  # inverses a matrix
    matrix = []
    matrix_dimensions = [int(element) for element in input('Enter matrix size:').split(' ')]
    print('Enter matrix:')
    for i in range(matrix_dimensions[0]):
        matrix.append([float(element) for element in input().split(' ')])
    determinant = laplace_expansion(matrix)
    cof_array = []
    for i in range(len(matrix)):
        cof_row = []
        for j in range(len(matrix)):
            cof_row.append(cofactor_array(matrix, i, j))
        cof_array.append(cof_row)
    if determinant == 0:
        print("This matrix doesn't have an inverse.")
    ct = []
    for i in range(len(matrix)):
        ct.append([cof_array[j][i] for j in range(len(matrix))])
    inverse_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            if ct[i][j] == 0:
                row.append('0')
            else:
                row.append(str(int(ct[i][j] / determinant * 100) / 100))
        inverse_matrix.append(row)
    print('The result is:')
    for row in inverse_matrix:
        print('  '.join(row))


def cofactor_array(matrix, i, j):  # returns a cofactor array using matrix, i-row and j-column
    cofactor1 = 1
    if len(matrix) == 2:
        cofactor1 *= (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    else:
        cofactor1 *= (-1) ** (i + j) * laplace_expansion(matrix_reduction(matrix, i, j))
    return cofactor1


greetings()
