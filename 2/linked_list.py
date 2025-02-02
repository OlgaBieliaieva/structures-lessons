# Вузол (Node) — основна частина зв'язаного списку, яка містить значення й посилання на наступний вузол. 
# Вузол — це об'єкт, який містить два атрибути: data (дані), які представляють значення вузла, і 
# next, який вказує на наступний вузол у списку.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Оскільки у зв’язаному списку кожен вузол має посилання на наступний вузол, 
# то потрібно задавати атрибут self.head, який вказує на перший вузол.
class LinkedList:
    def __init__(self):
        self.head = None

# Вставка нового вузла у список
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
# Додавання в початок
    def insert_at_beginning(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
# вставка після заданого вузла
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
# пошук вузлів
    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
# видалення вузлів
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
  print(element.data)