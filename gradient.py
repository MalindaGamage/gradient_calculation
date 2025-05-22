"""
Numerical Gradient Calculation for Linear Regression

This script demonstrates how to calculate the numerical gradient
of a simple linear regression cost function.
"""

import numpy as np


def cost_function(w, x=None, y=None):
    """
    Calculate the mean squared error cost for simple linear regression.

    Args:
        w (float): Weight parameter
        x (np.array): Input features (default: [1, 2, 3])
        y (np.array): Target values (default: [2, 4, 6])

    Returns:
        float: Mean squared error cost
    """
    if x is None:
        x = np.array([1, 2, 3])
    if y is None:
        y = np.array([2, 4, 6])
    return np.mean((w * x - y) ** 2)


def numerical_gradient(w, cost_func, h=1e-5):
    """
    Calculate the numerical gradient of a cost function at point w.

    Args:
        w (float): Point at which to calculate gradient
        cost_func (function): Cost function to evaluate
        h (float): Small step size for numerical differentiation

    Returns:
        float: Numerical gradient approximation
    """
    return (cost_func(w + h) - cost_func(w)) / h


def analytical_gradient(w, x=None, y=None):
    """
    Calculate the analytical gradient of the MSE cost function.

    Args:
        w (float): Weight parameter
        x (np.array): Input features (default: [1, 2, 3])
        y (np.array): Target values (default: [2, 4, 6])

    Returns:
        float: Analytical gradient
    """
    if x is None:
        x = np.array([1, 2, 3])
    if y is None:
        y = np.array([2, 4, 6])
    return 2 * np.mean(x * (w * x - y))


def compare_gradients(w_values):
    """
    Compare numerical and analytical gradients at multiple points.

    Args:
        w_values (list): List of w values to evaluate
    """
    print("\nGradient Comparison:")
    print("w\tNumerical\tAnalytical\tDifference")
    print("----------------------------------------------")

    for w in w_values:
        num_grad = numerical_gradient(w, cost_function)
        ana_grad = analytical_gradient(w)
        diff = abs(num_grad - ana_grad)
        print(f"{w:.1f}\t{num_grad:.6f}\t{ana_grad:.6f}\t{diff:.6f}")


if __name__ == "__main__":
    print("=== Gradient Calculation Demo ===")

    # Test points
    test_points = [0, 1, 1.5, 2, 2.5]

    # Calculate and print gradients
    for w in test_points:
        print(f"\nAt w = {w}:")
        print(f"Cost: {cost_function(w):.4f}")
        print(f"Numerical gradient: {numerical_gradient(w, cost_function):.4f}")
        print(f"Analytical gradient: {analytical_gradient(w):.4f}")

    # Compare gradients at multiple points
    compare_gradients(np.linspace(-1, 3, 5))