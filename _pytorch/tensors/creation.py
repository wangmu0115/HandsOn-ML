import torch

import numpy as np


def directly_from_data() -> torch.Tensor:
    data = [[1, 2, 3], [4, 5, 6]]
    t_data = torch.tensor(data, dtype=torch.float32)
    print(f"Tensor: {t_data}")
    return t_data


def from_a_ndarray() -> torch.Tensor:
    n_data = np.array([[1.0, 2, 3], [4, 5, 6]])
    t_data = torch.from_numpy(n_data)
    print(f"Tensor: {t_data}")
    return t_data


def from_another_tensor(base: torch.Tensor):
    x_ones = torch.ones_like(base)
    print(f"Ones Tensor: {x_ones}")
    x_rand = torch.rand_like(base)
    print(f"Random Tensor: {x_rand}")


if __name__ == "__main__":
    print("\n" + "=" * 40, "Directly from data | torch.tensor()", "=" * 40)
    t1 = directly_from_data()
    print("\n" + "=" * 40, "From a ndarray | torch.from_numpy()", "=" * 40)
    t2 = from_a_ndarray()
    print("\n" + "=" * 40, "From another Tensor | torch.*_like()", "=" * 40)
    from_another_tensor(t1)
