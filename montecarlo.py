'''
Idea: Generate two points in an XY plane from -1 to 1 and check if they are within a unit circle. If not, they're in a square.
Then, the ratio of points in the circle to total points approximates PI/4. To approximate PI, multiply the ratio by 4 to get PI = 4 * (points in circle / total points).
'''
import random
import matplotlib.pyplot as plt
import numpy as np


def estimate_pi(n):

    inside_circle = 0
    PI = 0
    total_points = 0
    # chosing a large number of points since this isn't a difficult computation
    for _ in range(n):
        x = random.uniform(-1, 1)  # generate a random x point from -1 to 1
        y = random.uniform(-1, 1)  # generate a random y point from -1 to 1
        if x**2 + y**2 <= 1:  # equation of a circle is x^2 + y^2 = r^2, here r=1. chatgpt was used to help recall the exponentiation operator in python
            inside_circle += 1
        total_points += 1

    # calculating PI using the ratio of points in circle to total points
    PI = 4 * (inside_circle / total_points)

    print(f"Approximation of PI given {n} trials is {PI}")
    return PI


# note, ai was used to help with the plotting code below. an explanation of the code and high level concepts will be documented in the pdf report
n_values = [10**i for i in range(1, 6)]  # [10, 100, 1000, 10000, 100000]
pi_estimates = []

for n in n_values:
    pi_est = estimate_pi(n)
    pi_estimates.append(pi_est)

plt.figure(figsize=(8, 6))
plt.semilogx(n_values, pi_estimates, 'bo-')
plt.axhline(y=3.14159, color='r', linestyle='--', label='True π')
plt.xlabel('Number of samples (n)')
plt.ylabel('π estimate')
plt.title('Monte Carlo π Convergence')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig('pi_convergence.png', dpi=300, bbox_inches='tight')
plt.close()

n_values_for_hist = [10**3, 10**4, 10**5]  # 1000, 10000, 100000

for n in n_values_for_hist:
    estimates = []
    print(f"\nRunning 500 trials for n={n}...")

    for _ in range(500):
        pi_est = estimate_pi(n)
        estimates.append(pi_est)

    plt.figure(figsize=(8, 6))
    plt.xlim(3.0, 3.3)
    plt.hist(estimates, bins=30, alpha=0.7, density=True)
    plt.axvline(x=3.14159, color='r', linestyle='--', label='True π')
    plt.xlabel('π estimate')
    plt.ylabel('Density')
    plt.title(f'Distribution of π estimates (n={n:,}, 500 trials)')
    plt.legend()
    plt.grid(True)

    plt.savefig(f'pi_distribution_n{n}.png', dpi=300, bbox_inches='tight')
    plt.close()
