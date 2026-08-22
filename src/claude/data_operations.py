print("Hello, World!")
print(8**3)
print(7 // 2)
print(6 / 2)
print(5 % 2)
print(5 / 2)
print(5 // 2)
print(1.1 + 0.2 - 0.3)
print(type(1.1 + 0.2 - 0.3))
print(1.1 + 0.2 - 0.3 == 1.0)
print(round(1.14545 + 0.344352 - 0.345343, 10))
import math

result = 0.1 + 0.2 - 0.3
print(result == 0)  # False — fails due to floating-point noise
print(math.isclose(result, 0))  # False too! (see note below)
print(math.isclose(result, 0, abs_tol=1e-9))  # True
