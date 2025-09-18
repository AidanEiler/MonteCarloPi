'''
Idea: Generate two points in an XY plane from -1 to 1 and check if they are within a unit circle. If not, they're in a square.
Then, the ratio of points in the circle to total points approximates PI/4. To approximate PI, multiply the ratio by 4 to get PI = 4 * (points in circle / total points).
'''
import random  # for generating random points


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


estimate_pi(1000)  # one thousand
estimate_pi(100000)  # one hundred thousand
estimate_pi(100000000)  # ten million
