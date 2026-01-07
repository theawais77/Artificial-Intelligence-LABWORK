import random
import math

def f(x):
    return x * math.sin(x)

def hill_climbing():
    current_x = random.uniform(0, 20)
    step_size = 0.9

    while True:
        left = current_x - step_size
        right = current_x + step_size

        neighbors = []
        if 0 <= left <= 20:
            neighbors.append(left)
        if 0 <= right <= 20:
            neighbors.append(right)

        next_x = max(neighbors, key=f)

        if f(next_x) <= f(current_x):
            break

        current_x = next_x

    return current_x, f(current_x)


best_x, best_value = hill_climbing()

print("Hill Climbing result:")
print("x =", round(best_x, 3))
print("f(x) =", round(best_value, 3))