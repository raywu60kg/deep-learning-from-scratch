from src.operations.convolution import Conv1d, Conv2d, Conv3d
import numpy as np


class TestConvolution:

    def test_conv2d_padding_input(self):
        res = Conv2d.get_padding_input(
            input_tensor=np.array([range(9)]).reshape([3, 3]),
            filter_size=[2, 2])
        print(res, np.shape(res))
        assert np.shape(res) == (4, 4)

    def test_conv2d_get_output_tensor(self):
        conv = Conv2d(
            input_tensor=np.array([range(9)]).reshape([3, 3]),
            padding="SAME",
            stride=[1, 1],
            filter_size=[2, 2],
            name="test",
            initializer="test"
        )
        res = conv.get_output_tensor()
        print("@@@", res)
        assert np.shape(res) == (3, 3)
