class ViewRecipe:
    def __init__(self, controller):
        self.controller = controller

    def display_recipe_list(self):
        data = self.controller.get_recipe_list()
        if data == 'Список рецептов пуст':
            print(self.controller.get_default_action())
            print(data)
        else:
            for recipe in data:
                print(recipe)


    def display_add_recipe(self, recipe_name: str, recipe_author: str, recipe_type: str, recipe_description: str,
                   list_of_ingredients: list, kitchen_name: str, user_roll = 'user'):
        data = self.controller.add_recipe(recipe_name, recipe_author, recipe_type, recipe_description,
                   list_of_ingredients, kitchen_name, user_roll)
        if data == 'Вы не можете добавлять рецепты':
            print(self.controller.get_default_action())
            print(data)
        else:
            print(self.controller.get_default_action())
            print(data)

    def display_add_ingredient(self, dish_name, *args):
        data = self.controller.add_ingredient(dish_name, *args)
        if not data:
            print('Такого рецепта нет в списке')
        if data == f'Ингридиент/ы: {args} - успешно добавлен/ы в {dish_name}':
            print(self.controller.get_default_action())
            print(data)


    def display_recipe_description(self, dish_name):
        data = self.controller.get_recipe_description(dish_name)
        if data:
            print(self.controller.get_default_action())
            print(data)
        else:
            print(self.controller.get_default_action())
            print('Рецепт не найден')

    def display_json_update_auth(self, filename, user_roll):
        data = self.controller.update_json_auth(filename, user_roll)
        if data == f'список рецептов записан в файл {filename}':
            print(self.controller.get_default_action())
            print(data)
        else:
            print(self.controller.get_default_action())
            print(data)
