# створення
my_set = set([1, 2, 3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

# додавання
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

# видалення
my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set) # Output: {2, 3, 4, 5}

# математичні операції над множинами, такі як 
# об'єднання (union), 
# перетин (intersection), 
# різниця (difference) та 
# симетрична різниця (symmetric_difference)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}

# повертає елемент на верхівці стеку без його видалення
def peek(stack):
  return stack[-1]

print(peek(stack)) # Output: 'b'

# перевіряє, чи стек порожній
def is_empty(stack):
  return len(stack) == 0

print(is_empty(stack)) # Output: False

class Stack:
  def __init__(self):
    self.stack = []

  # Додавання елемента до стеку
  def push(self, item):
    self.stack.append(item)

  # Видалення елемента зі стеку
  def pop(self):
    if len(self.stack) < 1:
      return None
    return self.stack.pop()

  # Перевірка, чи стек порожній
  def is_empty(self):
    return len(self.stack) == 0

  # Перегляд верхнього елемента стеку без його видалення
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]

# Цей код містить реалізацію структури даних стеку за допомогою класу Stack. 
# У конструкторі класу __init__ створюється порожній список self.stack, 
# який використовується для зберігання елементів стеку. Для класу реалізовано методи:

    # push — додає елемент до вершини стеку.
    # pop — видаляє верхній елемент стеку (якщо він існує) і повертає його. Якщо стек порожній, метод повертає None.
    # is_empty — перевіряє, чи стек порожній, повертаючи True або False.
    # peek — повертає верхній елемент стеку без його видалення. Якщо стек порожній, метод не повертає нічого.

# використання
s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.peek()) # Output: 'c'
print(s.pop())  # Output: 'c'
print(s.peek()) # Output: 'b'
print(s.is_empty()) # Output: False