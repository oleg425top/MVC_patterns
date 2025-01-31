import json


class ModelRecipe:
    def __init__(self):
        self.recipe_list = []

    def get_recipe_list(self):
        return self.recipe_list

    def add_recipe(self, recipe_name: str, recipe_author: str, recipe_type: str, recipe_description: str,
                   list_of_ingredients: list, kitchen_name: str, filename):
        data = {'Название рецепта :': recipe_name, 'Автор: ': recipe_author, 'Тип рецепта :': recipe_type,
                'Описание: ': recipe_description, 'Ингридиенты:  ': list_of_ingredients, 'Кухня :': kitchen_name}
        self.recipe_list.append(data)
        self.update_json(filename)

    def add_ingredient(self, dish_name, *args):
        self.recipe_list[dish_name['Ингридиенты:  ']].append(args)

    def get_recipe_description(self,dish_name):
        return self.recipe_list[dish_name['Описание: ']]

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.recipe_list, file, ensure_ascii=False, indent=4)
            return f'Рецепт сохранен в файл: {filename}!'