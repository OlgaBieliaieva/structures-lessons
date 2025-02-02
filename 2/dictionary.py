# створення
my_dict = {'name': 'John', 'age': 25}
print(my_dict) # Output: {'name': 'John', 'age': 25}

# читання
my_dict = {'name': 'John', 'age': 25}
print(my_dict['name']) # Output: John

# зміна
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26
print(my_dict) # Output: {'name': 'John', 'age': 26}

# додавання
my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict) # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

# видалення
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
print(my_dict) # Output: {'name': 'John', 'age': 25}