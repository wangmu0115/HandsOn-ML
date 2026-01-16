"""Activation Functions (AFs)"""

import numpy as np


def step_function(x: float) -> int:
    return 1 if x > 0.0 else 0


def sigmoid_af(x: np.ndarray) -> np.ndarray:
    """Logistic Sigmoid"""
    return 1 / (1 + np.exp(-x))


if __name__ == "__main__":
    from visualization import show_plot

    x = np.array([1.0, 2.0, 3.0])

    print("\n" + "=" * 40 + "Logistic Sigmoid" + "=" * 40)
    print(sigmoid_af(x))
    show_plot(np.arange(-5, 5, 0.1), sigmoid_af(np.arange(-5, 5, 0.1)))
