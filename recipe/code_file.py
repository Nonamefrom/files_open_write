from pprint import pprint


file_name = 'recipes.txt'  # переменная пути к файлу


def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='UTF-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(' | ')
                ingredient_name, quantity, measure = ingredient_line
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между блюдами
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list


# Пример использования функции
cook_book = create_cook_book(file_name)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)) #тест пример к задаче
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)) #тест на подсчет помидоров одной строкой в обоих рецептах