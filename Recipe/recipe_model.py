import json


class ModelRecipe:
    def __init__(self):
        self.recipe_list = []

    def get_recipe_list(self):
        return self.recipe_list

    def add_recipe(self, recipe_name: str, recipe_author: str, recipe_type: str, recipe_description: str,
                   list_of_ingredients: list, kitchen_name: str):
        data = {'Название рецепта :': recipe_name, 'Автор: ': recipe_author, 'Тип рецепта :': recipe_type,
                'Описание: ': recipe_description, 'Ингридиенты: ': list_of_ingredients, 'Кухня :': kitchen_name}
        self.recipe_list.append(data)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.recipe_list, file, ensure_ascii=False, indent=4)

# if __name__ == '__main__':
#     recipe_list = ModelRecipe()
#     recipe_list.add_recipe('Оливье', 'Людмила Иванова', 'салат',
#                            'Оливье — это традиционный русский салат, который обычно подают на праздничные столы.',
#                            ['300 г вареного картофеля', '200 г вареной моркови', '200 г вареной колбасы или ветчины',
#                             '100 г зеленого горошка', '100 г соленых огурцов', '3 вареных яйца', '200 г майонеза',
#                             'Соль и перец по вкусу'], 'Русская')

# recipe_list.add_recipe('Паста с томатным соусом', 'Антонио Росси', 'Второе блюдо',
#                        'Паста с томатным соусом — это простое и вкусное итальянское блюдо, которое можно приготовить за считанные минуты.',
#                        ['400 г пасты', '400 г консервированных помидоров', '2 зубчика чеснока',
#                         '2 столовые ложки оливкового масла', 'Соль и перец по вкусу',
#                         'Свежий базилик для украшения'], 'Итальянская')
# recipe_list.add_recipe('Круассаны', 'Пьер Дюпон', ' Выпечка',
#                        'Круассаны — это знаменитая французская выпечка, которая  идеально подходит для завтрака или перекуса с чашечкой кофе.',
#                        ['500 г муки', '250 мл теплого молока', '10 г сухих дрожжей', '50 г сахара',
#                         '1 чайная ложка соли', '200 г сливочного масла', '1 яйцо для смазывания'], 'Французская')

# recipe_list.update_json(r'recipe_list.json')
# recipe_list.add_ingredient('Оливье', 'чесночный соус', 'петрушка')
# recipe_list.update_json(r'recipe_list1.json')
