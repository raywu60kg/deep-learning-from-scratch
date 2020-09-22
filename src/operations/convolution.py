from src.operations.operation import Operation
import numpy as np


class Cov1d(Operation):
    def __init__(self, input, padding, stride, filter_size, name, initializer):
        self.input = input
        self.padding = padding
        self.stride = stride
        self.filter_size = filter_size
        self.name = name
        self.initializer = initializer
        if initializer == "random_normal":

            self.object = np.random.randn(filter_size)
        else:
            self.object = np.random.randn(filter_size)

    def get_output(self):
        # add padding on input

        # calculate output shape

        # fill the output
        pass

    def get_gradient(self):
        pass


class Cov2d(Operation):
    def __init__(self, input, padding, stride, filter_size, name, initializer):
        "padding can be 'SAME' or 'VALID'"
        if padding == 'VALID':
            self.padding_input = self.get_padding_input(input)
        else:
            self.padding_input = input
        self.padding = padding
        self.stride = stride
        self.filter_size = filter_size
        self.name = name
        self.initializer = initializer
        if initializer == "random_normal":
            self.filter = np.random.randn(filter_size)
        else:
            self.filter = np.random.randn(filter_size)

    def get_output(self):
        # calculate output shape
        #  input_size + 2 * padding_size-(filter_size-1)

        # fill the output
        pass

    def get_gradient(self):
        pass

    @staticmethod
    def padding_input(input, filter_size, stride):
        # assume filter_size is square
        # padding_size = (filter_size-1) / 2
        padding_shape = (filter_size[0]-1)/2
        tmp = tuple(map(lambda x: x+padding_shape, np.shape(input)))
        print("@@@@", tmp)
        paddding_input = np.zeros(tmp)
        paddding_input[padding_shape:, padding_shape:] = input

        return padding_shape


class Cov3d(Operation):
    # TODO
    pass
