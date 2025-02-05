def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3


def exists_in_list(arr, x):
    return linear_search(arr, x) != -1

numbers = [1, 3, 5, 7, 9, 11]
print(exists_in_list(numbers, 7))  # Output: True
print(exists_in_list(numbers, 2))  # Output: False

# У найгіршому випадку (коли елемент або не знаходиться у списку, або є останнім елементом списку), 
# лінійний пошук має лінійну часову складність O(n)O(n), де nn — це кількість елементів у списку. 
# Однак, у середньому випадку, коли елемент може знаходитись на будь-якій позиції у списку, 
# очікувана часова складність становить O(n/2)O(n/2), що все ще лінійно. 
# Це робить лінійний пошук менш ефективним для великих впорядкованих даних, 
# де можуть бути використані ефективніші алгоритми, такі як двійковий пошук.