class ViewRecipe:
    def __init__(self, controller):
        self.controller = controller

    def display_recipe_list(self):
        data = self.controller.get_recipe_list()
        if len(data) == 0:
            print('Список рецептов пуст!')
        else:
            print(data)

    def display_add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                   list_of_ingredients, kitchen_name, user_roll):
        data = self.controller.add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                   list_of_ingredients, kitchen_name, user_roll)
        if data == 'Вы не можете добавлять рецепты':
            print(data)
        else:
            print(self.controller.get_recipe_list())

    def display_add_ingredient(self, dish_name, *args):
        data = self.controller.add_ingredient(self, dish_name, *args)
        if data == 'Рецепт не найден':
            print(data)
        else:
            print(self.controller.get_recipe_list())

    def display_recipe_description(self, dish_name):
        data = self.controller.get_recipe_description()
        if data:
            print(data)
        else:
            print('Рецепт не найден')

    def display_json_update_auth(self, filename, user_roll):
        data = self.controller.update_json_auth(filename, user_roll)
        if data == f'список рецептов записан в файл {filename}':
            print(data)
        else:
            print(data)
