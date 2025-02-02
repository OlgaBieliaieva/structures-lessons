from queue import Queue
import random

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue) # Output: deque(['a', 'b', 'c'])

# Видаляємо елемент
q.get()
print(q.queue) # Output: deque(['b', 'c'])

# qsize(): Повертає поточний розмір черги.
# empty(): Повертає True, якщо черга порожня, в іншому випадку — False.
# full(): Повертає True, якщо черга повна (якщо вона має обмежений розмір), в іншому випадку — False
# Створюємо чергу
q = Queue(maxsize = 3)

# Перевіряємо, чи черга порожня
print(q.empty()) # Output: True

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

# Перевіряємо, чи черга повна
print(q.full()) # Output: True

# Перевіряємо розмір черги
print(q.qsize()) # Output: 3

# Видаляємо елементи
print(q.get()) # Output: 'a'
print(q.get()) # Output: 'b'

class Client:
  def __init__(self, name):
    self.name = name
    self.operations = random.randint(1, 5) # Випадкова кількість операцій

class Bank:
  def __init__(self):
    self.clients = Queue()

  def new_client(self, client):
    self.clients.put(client)

  def serve_clients(self):
    while not self.clients.empty():
      current_client = self.clients.get()
      print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
      # Тут можна додати час обслуговування та іншу логіку

# Створюємо банк
bank = Bank()

# Додаємо клієнтів
for i in range(5):
  bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
bank.serve_clients()
# У цьому прикладі ми створили два класи — Client і Bank. 
# Клієнт має ім'я та випадкову кількість операцій, які потрібно виконати. 
# Банк використовує чергу для зберігання клієнтів і обслуговує їх у порядку приходу. 
# Ми можемо додавати нових клієнтів у будь-який час, і банк продовжує обслуговувати їх у порядку приходу.
