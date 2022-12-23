import numpy as np


def getting_input():
    num_of_equations = int(input())
    matrix_of_equation = []
    for _ in range(num_of_equations):
        equation = list(map(int, input().split()))
        matrix_of_equation.append(equation)
    return np.matrix(matrix_of_equation, dtype=np.float64)


def smallest_pivot_position(num_row):
    position_of_pivots = []
    for p in range(num_row, (matrix.shape[0])):
        m = matrix[p].tolist()
        index_first_match = next(
            (index for index, item in enumerate(m[0])
             if item != 0),
            None
        )
        if index_first_match is None:
            index_first_match = 100000000
        if index_first_match < num_row:
            continue
        position_of_pivots.append((p, index_first_match))
    return min(position_of_pivots, key=lambda tup: tup[1])



def greatest_pivot_position(num_row):
    position_of_pivots = []
    for p in range(num_row, -1, -1):
        m = matrix[p].tolist()
        index_first_match = next(
            (index for index, item in enumerate(m[0])
             if item != 0),
            None
        )
        if index_first_match is None:
            index_first_match = 100000000

        position_of_pivots.append((p, index_first_match))
    return max(position_of_pivots, key=lambda tup: tup[1])


def swap_rows(original_row, swapped_row):
    temp = np.array(matrix[original_row], dtype=np.float64)
    matrix[original_row] = matrix[swapped_row]
    matrix[swapped_row] = temp


def rows_operations(row1, row2, operand):
    matrix[row2] = matrix[row2] + matrix[row1] * operand


def row_reduce_1(row, operand):
    matrix[row] = matrix[row] / operand


def pivot_finder():
    position_of_pivots = []
    for p in range(matrix.shape[0]):
        m = matrix[p].tolist()
        index_first_match = next(
            (index for index, item in enumerate(m[0])
             if item != 0),
            None
        )
        if index_first_match is None:
            continue
        position_of_pivots.append((p, index_first_match))
    return position_of_pivots


def equation_solver(position_of_pivots):
    print('dafssssssss \n ', position_of_pivots)
    for pivot in position_of_pivots:
        answer = 0
        for i in range(pivot[1] + 1, matrix.shape[1] - 1):
            answer += matrix[pivot[0], i] * 10
        final_answer = matrix[pivot[0], matrix.shape[1] - 1] - answer
        print('x[{}] : {}'.format(pivot[1] + 1, final_answer))
    for j in range(matrix.shape[1] - 1):
        flag_in = False
        for pivot in position_of_pivots:
            if j == pivot[1]:
                flag_in = True
        if not flag_in:
            print('x[{}] : 10'.format(j + 1))


def find_coefficient(i,pivot):
    if matrix[pivot[0], pivot[1]] == 0:
        return None
    coefficient_f = -(matrix[i, pivot[1]] / matrix[pivot[0], pivot[1]])
    print('coefficient_f  ', coefficient_f)
    return coefficient_f


def is_consistent():
    for r in range(matrix.shape[0] - 1, -1, -1):
        m = matrix[matrix.shape[0] - 1].tolist()
        index_first_match = next(
            (index for index, item in enumerate(m[0])
             if item != 0),
            None
        )
        if index_first_match == matrix.shape[1] - 1:
            return False
    return True


# forward
def forward_phase():
    for r in range(matrix.shape[0] - 1):
        pivot = smallest_pivot_position(r)
        swap_rows(r, pivot[0])
        pivot = smallest_pivot_position(r)
        for i in range(pivot[0] + 1, matrix.shape[0]):
            if pivot[1] == 100000000:
                continue
            coefficient = find_coefficient(i,pivot)
            if coefficient is not None:
                rows_operations(pivot[0], i, coefficient)


# backward
def backward_phase():
    for r in range(matrix.shape[0] - 1, -1, -1):
        pivot = greatest_pivot_position(r)
        if pivot[1] == matrix.shape[1] - 1 and pivot[0] == matrix.shape[0] - 1:
            continue
        for i in range(pivot[0] - 1, -1, -1):
            if pivot[1] == 100000000:
                continue
            coefficient = find_coefficient(i,pivot)
            if coefficient is not None:
                rows_operations(pivot[0], i, coefficient)


def reduced_echelon_form():
    for r in range(matrix.shape[0] - 1):
        pivot = smallest_pivot_position(r)
        swap_rows(r, pivot[0])
    for r in range(matrix.shape[0]):
        pivot = smallest_pivot_position(r)
        if pivot[1] == 100000000:
            continue
        if pivot[1] == matrix.shape[1] - 1 and pivot[0] == matrix.shape[0] - 1:
            continue
        row_reduce_1(pivot[0], matrix[pivot[0], pivot[1]])


def main():
    forward_phase()
    backward_phase()
    reduced_echelon_form()
    print('Matrix is consistent: ', is_consistent())
    equation_solver(pivot_finder())


matrix = getting_input()
main()
