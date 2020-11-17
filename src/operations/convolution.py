from src.operations.operation import Operation
import math
import numpy as np


class Conv1d(Operation):
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


class Conv2d(Operation):
    # https://d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html
    def __init__(
            self,
            input_tensor,
            padding,
            stride,
            filter_size,
            name,
            initializer):
        "padding can be 'SAME' or 'VALID'"
        if padding == 'SAME':
            self.padding_input = self.get_padding_input(
                input_tensor=input_tensor,
                filter_size=filter_size,
                stride=stride)
        elif padding == "VALID":

            self.padding_input = input_tensor
        else:
            raise ValueError("Padding should be 'SAME' or 'VALID'")
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
    def get_padding_input(input_tensor, filter_size, stride):

        if min(filter_size) < 1:
            raise ValueError("filter_size should greater than zero")

        # compute padding shape
        extend_shape = [x - 1 for x in filter_size]
        padding_shape = [
            x+y for x, y in zip(
                extend_shape, np.shape(input_tensor))]
        padding_result = np.zeros(padding_shape)

        # padding the input
        input_tensor_loc = []
        for x, y in zip(extend_shape, padding_shape):
            if x % 2 == 0:
                input_tensor_loc.append(slice(x/2, y-x/2))
            else:
                input_tensor_loc.append(slice(math.ceil(x/2), y-math.floor(x/2)))
        padding_result[input_tensor_loc] = input_tensor

        return padding_result


class Conv3d(Operation):
    # TODO
    pass
