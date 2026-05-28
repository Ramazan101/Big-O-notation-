# Логлинейное время - O(n log n)
# Время выполнения алгоритма включает в себя как линейное, так и логарифмическое время.

# HeapSort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)     # O (n)
while nums:
    heapq.heappop(nums) # O (log n)

# MergeSort (and most built-in sorting functions)

