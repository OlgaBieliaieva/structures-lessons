import numpy as np

# створення
arr = np.array([1, 2, 3, 4, 5])
print(arr) # Output: array([1, 2, 3, 4, 5])

# арифметичні операції на всьому масиві
arr = np.array([1, 2, 3, 4, 5])
print(arr + 2) # Output: array([3, 4, 5, 6, 7])

# операції на двох масивах
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2) # Output: array([5, 7, 9])

# функції агрегації sum(), mean(), max(), min() 
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # Output: 15
print(np.mean(arr)) # Output: 3.0 (середнє значення)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)