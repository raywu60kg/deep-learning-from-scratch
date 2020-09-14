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
        pass

    def get_gradient(self):
        pass


class Cov2d(Operation):
    pass


class Cov3d(Operation):
    pass
