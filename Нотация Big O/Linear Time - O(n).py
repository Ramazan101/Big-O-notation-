# Линейное время - O(n)
# Время выполнения алгоритма возрастает линейно с размером входных данных.

nums = [1, 2, 3]
sum(nums)       # sum of array
for n in nums:  # looping
    print(n)

nums.insert(1, 100)
nums.remove(100)
print(100 in nums)

import heapq
heapq.heapify(nums)