from src.operations.convolution import Conv1d, Conv2d, Conv3d
import numpy as np


class TestConvolution:
    def test_cov1d(self):
        print(np.random.randn(3))
        assert 1 == 1

    def test_cov2d_padding_input(self):
        print(tuple(map(lambda x: x+1, (1,2))))
        res = Conv2d.get_padding_input(
            input_tensor=np.array([range(9)]).reshape([3, 3]),
            filter_size=[2, 2],
            stride=1)
        print(res, np.shape(res))
        assert 1 == 2
