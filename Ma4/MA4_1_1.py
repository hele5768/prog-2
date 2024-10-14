
"""
Solutions to module 4
Review date:
"""

student = "Henrik Levin Johansson"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    
    for _ in range(n):
        x, y = r.uniform(-1, 1), r.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    # Approximation of pi
    pi_approx = 4 * inside_circle / n
    print(f"Number of points inside the circle: {inside_circle}")
    print(f"Approximated π: {pi_approx}")
    
    # Plotting the points
    plt.figure(figsize=(6, 6))
    plt.scatter(x_inside, y_inside, color='red', s=1, label='Inside circle')
    plt.scatter(x_outside, y_outside, color='blue', s=1, label='Outside circle')
    plt.legend()
    plt.title(f"Monte Carlo Approximation of π with {n} points")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(f"pi_approximation_{n}.png")
    plt.show()

def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
    main()
