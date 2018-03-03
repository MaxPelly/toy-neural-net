from math import e

from matricies import Matrix


class NeuralNet (object):
    def __init__(self, inputs, hidden_layer, outputs):
        """
        creates a 2 layer perceptron neural net
        :param inputs: the number of inputs
        :param hidden_layer: the number of nodes in the hidden layer
        :param outputs: the number of nodes in the output
        """

        self.inputs = inputs
        self.hl = hidden_layer
        self.outputs = outputs

        self.hidden_weights = Matrix(hidden_layer, inputs, True)
        self.hidden_bias = Matrix(hidden_layer, 1, True)

        self.output_weights = Matrix(outputs, hidden_layer, True)
        self.output_bias = Matrix(outputs, 1, True)

    def __call__(self, input_values, training=False):
        """
        feeds input through the network
        :param input_values: an array
        :return: an array of the result
        """

        input_values = Matrix.from_array(input_values)

        hidden = Matrix.map(((self.hidden_weights * input_values) + self.hidden_bias), self.activation)
        output = Matrix.map(((self.output_weights * hidden) + self.output_bias), self.activation)

        if training:
            return output, hidden, input_values

        return output.to_array()

    def train(self, inputs, answer, learning_rate=0.1):
        answer = Matrix.from_array(answer)
        guess, hidden, inputs = self(inputs, training=True)

        output_error = answer - guess
        self.output_weights += (Matrix.piecewise_mult(Matrix.map(guess, self.dsigmoind),
                                                      output_error) * learning_rate) * Matrix.transpose(hidden)
        self.output_bias += Matrix.piecewise_mult(Matrix.map(guess, self.dsigmoind), output_error) * learning_rate

        hidden_error = Matrix.transpose(self.output_weights) * output_error
        self.hidden_weights += (Matrix.piecewise_mult(Matrix.map(hidden, self.dsigmoind),
                                                      hidden_error) * learning_rate) * Matrix.transpose(inputs)
        self.hidden_bias += Matrix.piecewise_mult(Matrix.map(hidden, self.dsigmoind), hidden_error) * learning_rate

    @staticmethod
    def activation(value):
        return 1 / (1 + e ** (-value))

    @staticmethod
    def dsigmoind(value):
        return value * (1 - value)


if __name__ == '__main__':

    from random import choice


    def func(x, y):
        return 1


    data_set = [((1, 0), (1,)), ((0, 1), (1,)), ((0, 0), (0,)), ((1, 1), (0,))]

    brain = NeuralNet(2, 2, 1)
    for x in range(50000):
        data = choice(data_set)
        brain.train(data[0], data[1])

    print(brain((1, 0)))
    print(brain((0, 1)))
    print(brain((0, 0)))
    print(brain((1, 1)))
