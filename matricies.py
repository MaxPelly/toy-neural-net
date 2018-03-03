from random import uniform

class Matrix(object):
    def __init__(self, rows, columns, random=False, rand_min=-1, rand_max=1):
        self.rows = rows
        self.cols = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]
        if random:
            self.randomise(rand_min, rand_max)

    def __repr__(self):
        return str(self.data)

    def __add__(self, other):
        output = Matrix(self.rows, self.cols)
        if isinstance(other, Matrix):
            assert self.rows == other.rows and self.cols == other.cols
            for row in range(self.rows):
                for column in range(self.cols):
                    output.data[row][column] = self.data[row][column] + other.data[row][column]

        elif isinstance(other, int) or isinstance(other, float):
            for row in range(self.rows):
                for column in range(self.cols):
                    output.data[row][column] = self.data[row][column] + other

        return output

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        output = None
        if isinstance(other, Matrix):
            assert self.cols == other.rows
            output = Matrix(self.rows, other.cols)
            for row in range(self.rows):
                for column in range(other.cols):
                    sum = 0
                    for n in range(self.cols):
                        sum += self.data[row][n] * other.data[n][column]
                    output.data[row][column] = sum

        elif isinstance(other, int) or isinstance(other, float):
            output = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for column in range(self.cols):
                    output.data[row][column] = self.data[row][column] * other

        return output

    def __rmul__(self, other):
        return self.__mul__(other)

    def add(self, other):
        """
        adds a number or matrix to the current matrix, changing it in place

        :param other: the thing to add
        :return: None
        """
        output = self + other
        self.data, self.cols, self.rows = output.data, output.cols, output.rows

    def mul(self, other):
        """
        multiplies the matrix by a number or matrix, changing it in place

        :param other: the thing to multiply by
        :return: None
        """
        output = self * other
        self.data, self.cols, self.rows = output.data, output.cols, output.rows

    def randomise(self, rand_min, rand_max):
        """
        randomises the matricies values to values between rand_min and rand_max

        :param rand_min: minimum value, int
        :param rand_max: maximum value, int
        :return: None
        """
        for row in range(self.rows):
            for column in range(self.cols):
                self.data[row][column] = uniform(rand_min, rand_max)

    def transpose(self):
        """
        transposes the current matrix inplace

        :return: None
        """
        output = Matrix(self.cols, self.rows)
        for row in range(self.rows):
            for column in range(self.cols):
                output.data[column][row] = self.data[row][column]
        return output

    def map(self, f):
        """
        applies f to the each of the values in the current matrix, GENERATES A NEW MATRIX WITHOUT ALTERING CURRENT

        :param f: a function to apply to the values, should expect (value, row, column)
        :return: Matrix
        """
        output = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for column in range(self.cols):
                output.data[row][column] = f(self.data[row][column], row, column)
        return output


if __name__ == '__main__':
    from random import randint as uniform

    m = Matrix(2, 5, True, 0, 10)
    n = Matrix(5, 3, True, 0, 10)
    print(m)
    print(n)
    b = m * n
    print(b)
    print(m.transpose(), m)
