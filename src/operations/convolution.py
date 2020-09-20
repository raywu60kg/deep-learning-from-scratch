from src.operations.operation import Operation
import numpy as np


class Cov1d(Operation):
    def __init__(self, input, padding, stride, kernel_size, name, initializer):
        self.input = input
        self.padding = padding
        self.stride = stride
        self.kernel_size = kernel_size
        self.name = name
        self.initializer = initializer
        if initializer == "random_normal":

            self.object = np.random.randn(kernel_size)
        else:
            self.object = np.random.randn(kernel_size)

    def get_output(self):
        # add padding on input

        # calculate output shape

        # fill the output
        pass

    def get_gradient(self):
        pass


class Cov2d(Operation):
    def __init__(self, input, padding, stride, kernel_size, name, initializer):
        "padding can be 'SAME' or 'VALID'"
        if padding == 'VALID':
            self.input = self.padding_input(input)
        else:
            self.input = input
        self.padding = padding
        self.stride = stride
        self.kernel_size = kernel_size
        self.name = name
        self.initializer = initializer
        if initializer == "random_normal":

            self.filter = np.random.randn(kernel_size)
        else:
            self.filter = np.random.randn(kernel_size)

    def get_output(self):
        # calculate output shape

        # fill the output

    def get_gradient(self):
        pass

    @staticmethod
    def padding_input(self, input, kernel_size):
        padding_shape = 123
        pass


class Cov3d(Operation):
    # TODO
    pass
