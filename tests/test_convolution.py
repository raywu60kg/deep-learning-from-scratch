from src.operations.convolution import Cov1d, Cov2d, Cov3d
import numpy as np


class TestConvolution:
    def test_cov1d(self):
        print(np.random.randn(3))
        assert 1 == 1

    def test_cov2d_padding_input(self):
        print(tuple(map(lambda x: x+1, (1,2))))
        res = Cov2d.padding_input(
            input=np.array([range(9)]).reshape([3, 3]),
            filter_size=[2, 2],
            stride=1)
        print(res)
        assert 1 == 2
