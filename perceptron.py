from random import uniform


class Perceptron (object):
    def __init__(self, input_size, weights=(), random=True, lr=0.1):
        if random:
            self.weights = [uniform(-1.0, 1.0) for i in range(input_size + 1)]
        else:
            assert len(weights) == input_size + 1
            self.weights = weights

        self.input_size = input_size
        self.lr = lr

    def __call__(self, inputs):
        if not isinstance(inputs, list):
            inputs = list(inputs)
        assert len(inputs) == self.input_size
        inputs.append(1)  # append the bias to the inputs, allways 1
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]

        return self.activate(sum)

    @staticmethod
    def activate(value):
        if value < 0:
            return -1
        return 1

    def train(self, inputs, answer):
        if not isinstance(inputs, list):
            inputs = list(inputs)
        output = self(inputs)
        inputs.append(1)  # again adding the bias

        error = answer - output
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr
