from collections import deque

d = deque()
print(d)  # deque([])

# додавання
d.append('right')
d.appendleft('left')
print(d)  # deque(['left', 'right'])

# видалення
d.pop()
d.popleft()
print(d)  # deque([])

# розширення
d.extend(['a', 'b', 'c'])
d.extendleft(['x', 'y', 'z'])
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

# обертання
# процес переміщення першого елемента черги на її кінець, відомий також як циклічний зсув
#     Видаляється перший елемент із черги.
#     Цей елемент додається на кінець черги.
# deque.rotate(n) робить циклічний зсув усіх елементів в deque на n позицій. 
# Він надає більш гнучкий підхід, дозволяючи зсувати елементи в обох напрямках
# Коли n додатне, елементи зсуваються вправо, тобто елементи з кінця переходять на початок. 
# Коли n від'ємне, зсув відбувається вліво, тобто елементи з початку черги переміщуються на кінець.
d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])
# Отже, в нашому прикладі:

    # d.rotate(2) переміщує два останні елементи на початок deque,
    # d.rotate(-2) переміщує два перші елементи на кінець deque.


# Це означає, що зсув вправо rotate(2) відповідає зсуву елементів з кінця на початок, 
# а зсув уліво rotate(-2) – переміщенню елементів з початку на кінець.

# обмеження розміру
d = deque(maxlen=3)
d.extend([1, 2, 3])
print(d)  # deque([1, 2, 3])

d.append(4)
print(d)  # deque([2, 3, 4])

# пошук у deque
d = deque([1, 2, 3, 4, 2, 5])
print(d.count(2))  # 2
