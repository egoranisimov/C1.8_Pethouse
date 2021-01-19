from ClassCat import Cat

cats = [Cat('Барон', 'Мальчик', 2), Cat('Сэм', 'Мальчик', 2)]

for i in cats:
    print(i.get_name(), i.get_gender(), i.get_age(), sep=', ')