from ClassCat import Cat

baron = Cat('Барон', 'Мальчик', 2)
sam = Cat('Сэм', 'Мальчик', 2)

print(baron.get_name(), baron.get_gender(), baron.get_age(), sep=', ')
print(sam.get_name(), sam.get_gender(), sam.get_age(), sep=', ')