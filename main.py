# Необходимо написать программу для кулинарной книги.
# Исходный список рецептов  храниться в отдельном файле Cook_book
# Нужно прочитать и записать в словарь

print('Задание 1\n')
cook_book = {}
with open('Cook_book.txt', 'r', encoding='utf8') as recipes:
    for line in recipes:
        dish_name = line.strip()
        ingredient_amount = recipes.readline()
        dish_ingredients = []
        for i in range(int(ingredient_amount)):
            ingredient = recipes.readline()
            title, amount, unit = ingredient.split(' | ')  # это распаковка
            dish_ingredients.append({'ingredient_name': title, 'quantity': amount, 'measure': unit.strip()})
        cook_book[dish_name] = dish_ingredients
        recipes.readline()
for key, value in cook_book.items():
    print(key, ':', value)


# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
# # get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
# # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
# # {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


print('\nЗадание 2\n')


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}
    with open('Cook_book.txt', 'r', encoding='utf8') as recipes:
        for line in recipes:
            dish_name = line.strip()
            ingredient_amount = recipes.readline()
            dish_ingredients = []
            for i in range(int(ingredient_amount)):
                ingredient = recipes.readline()
                title, amount, unit = ingredient.split(' | ')  # это распаковка
                dish_ingredients.append({'ingredient_name': title, 'quantity': amount, 'measure': unit.strip()})
            cook_book[dish_name] = dish_ingredients
            recipes.readline()
    ingredients_quantity = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingredient in recipe:
            ingredient_title = ingredient['ingredient_name']
            unit_title = ingredient['measure']
            if ingredient_title in ingredients_quantity:
                ingredients_quantity[ingredient_title]['quantity'] += person_count * int(ingredient['quantity'])
            else:
                ingredients_quantity[ingredient_title] = {}
                ingredients_quantity[ingredient_title]['measure'] = unit_title
                ingredients_quantity[ingredient_title]['quantity'] = person_count * int(ingredient['quantity'])
    print(ingredients_quantity)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)



# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять тут
# # Необходимо объединить их в один по следующим правилам:
# # Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt
# # Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
# # Строка номер 1 файла номер 2
# Итоговый файл:
# # 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

print('\nЗадание 3\n')

file_names = ['1.txt', '2.txt', '3.txt']
file_names_and_rows = {}
for i in range(3):
    file_name = file_names[i]
    with open(file_name, 'r', encoding='windows-1251') as file:
        file_rows = len(file.readlines())
        file_names_and_rows[file_name] = file_rows

sorted_values = sorted(file_names_and_rows.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in file_names_and_rows.keys():
        if file_names_and_rows[k] == i:
            sorted_dict[k] = file_names_and_rows[k]
            break

with open('join.txt', 'w', encoding='windows-1251') as join_file:
    join_file.write('') # удаляем содержимое файла для последующей записи
with open('join.txt', 'a', encoding='windows-1251') as join_file:
    for file_name in sorted_dict.keys():
        with open(file_name, 'r', encoding='windows-1251') as file:
            join_file.write(file_name + '\n')
            join_file.write(str(sorted_dict[file_name]) + '\n')
            join_file.write(file.read() + '\n')
with open('join.txt', 'r', encoding='windows-1251') as join_file:
    join_text = join_file.read()
    print(join_text)