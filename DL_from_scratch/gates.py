import numpy as np


def AND(x1, x2):
    """AND gate"""
    weights = np.array([0.5, 0.5])
    bias = -0.7
    y = np.array([x1, x2]) @ weights + bias
    return 0 if y <= 0 else 1


def NAND(x1, x2):
    """Not AND gate"""
    weights = np.array([-0.5, -0.5])
    bias = 0.7
    y = np.array([x1, x2]) @ weights + bias
    return 0 if y <= 0 else 1


def OR(x1, x2):
    """OR gate"""
    weights = np.array([0.5, 0.5])
    bias = -0.2
    y = np.array([x1, x2]) @ weights + bias
    return 0 if y <= 0 else 1


def XOR(x1, x2):
    x21 = NAND(x1, x2)
    x22 = OR(x1, x2)
    return AND(x21, x22)


def demo_gates(gate):
    name = gate.__name__
    for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"{name}(x1={x1}, x2={x2}) = {gate(x1, x2)}")


if __name__ == "__main__":
    print("\n" + "=" * 40, "AND gate", "=" * 40)
    demo_gates(AND)

    print("\n" + "=" * 40, "NAND gate", "=" * 40)
    demo_gates(NAND)

    print("\n" + "=" * 40, "OR gate", "=" * 40)
    demo_gates(OR)

    print("\n" + "=" * 40, "XOR gate", "=" * 40)
    demo_gates(XOR)
