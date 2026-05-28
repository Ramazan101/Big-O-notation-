# Время вычисления квадратного корня - O(√n)
# Время выполнения алгоритма увеличивается пропорционально квадратному корню из размера входных данных.


# Get all factors of n
import math
n = 12
factors = 12
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.__add__(i)
        factors.__add__(n//i)