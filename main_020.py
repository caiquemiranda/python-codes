a = 1
b = 5
c = 4

delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** (1/2)

x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)

print(f'x1 = {x1}')
print(f'x2 = {x2}')
