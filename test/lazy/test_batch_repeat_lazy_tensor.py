from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import torch
import unittest
from gpytorch.lazy import ToeplitzLazyTensor, BatchRepeatLazyTensor
from test.lazy._lazy_tensor_test_case import BatchLazyTensorTestCase


class TestBatchRepeatLazyTensor(BatchLazyTensorTestCase, unittest.TestCase):
    seed = 0

    def create_lazy_tensor(self):
        toeplitz_column = torch.tensor(
            [4, 0, 0, 1], dtype=torch.float, requires_grad=True
        )
        return BatchRepeatLazyTensor(ToeplitzLazyTensor(toeplitz_column), torch.Size((3,)))

    def evaluate_lazy_tensor(self, lazy_tensor):
        evaluated = lazy_tensor.base_lazy_tensor.evaluate()
        return evaluated.repeat(*lazy_tensor.batch_repeat, 1, 1)


class TestBatchRepeatLazyTensorBatch(BatchLazyTensorTestCase, unittest.TestCase):
    seed = 0

    def create_lazy_tensor(self):
        toeplitz_column = torch.tensor(
            [[4, 0, 0, 1], [3, 0, -0.5, -1]], dtype=torch.float, requires_grad=True
        )
        return BatchRepeatLazyTensor(ToeplitzLazyTensor(toeplitz_column), torch.Size((3,)))

    def evaluate_lazy_tensor(self, lazy_tensor):
        evaluated = lazy_tensor.base_lazy_tensor.evaluate()
        return evaluated.repeat(*lazy_tensor.batch_repeat, 1, 1)


if __name__ == "__main__":
    unittest.main()
