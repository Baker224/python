class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'structure matrix_1 and matrix_2 not equal'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'structure matrix_1 and matrix_2 not equal'
        return answer


matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]])
matrix_2 = Matrix([[2, 3, 4], [4, 5, 6], [6, 7, 8], [10, 11, 12]])
print(matrix_1 + matrix_2)
