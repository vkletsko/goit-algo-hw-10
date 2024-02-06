import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x**2 + 12 * x + 15


a = 1
b = 6
n = 1000

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

points_under_curve = np.sum(y_random <= f(x_random))

area = (b - a) * (f(b) * points_under_curve / n)

x_values = np.linspace(a, b, 400)
y_values = f(x_values)

result, error = spi.quad(f, a, b)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, "b-", label="f(x) = x^2 + 12x + 15")
plt.fill_between(x_values, y_values, color="gray",
                 alpha=0.3, label="Площа під кривою")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Графік функції та площа під кривою за методом Монте-Карло")
plt.legend()
plt.grid(True)
plt.show()

print("Площа під кривою:", area)
print("Інтеграл: ", result)
