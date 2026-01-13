import torch

import numpy as np


def tensor_to_ndarray():
    t = torch.ones(5)
    print(f"Tensor: {t}")
    n = t.numpy()
    print(f"ndarray: {n}")
    print("-" * 40, "change Tensor", "-" * 40)
    t.add_(42)
    print(f"Tensor: {t}")
    print(f"ndarray: {n}")


def ndarray_to_tensor():
    n = np.ones(5)
    print(f"ndarray: {n}")
    t = torch.from_numpy(n)
    print(f"Tensor: {t}")
    np.add(n, 3.14, out=n)
    print(f"ndarray: {n}")
    print(f"Tensor: {t}")


if __name__ == "__main__":
    print("\n" + "=" * 40, "Tensor to NumPy ndarray", "=" * 40)
    tensor_to_ndarray()

    print("\n\n" + "=" * 40, "NumPy ndarray to Tensor", "=" * 40)
    ndarray_to_tensor()
