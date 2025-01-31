class ControllerRecipe:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return f'Наш список рецептов: {self.model.__class__.__name__}!!!!'

    """Список рецептов может посмотреть любой пользователь!!"""

    def get_recipe_list(self):
        print(self.get_default_action())
        return self.model.get_recipe_list()

    """А вот добавить рецепт только админ!!"""

    def add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                   list_of_ingredients, kitchen_name, user_roll):
        if user_roll == 'admin':
            print(self.get_default_action())
            self.model.add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                                  list_of_ingredients, kitchen_name)
            return 'Рецепт добавлен с список'
        else:
            print(self.get_default_action())
            return 'Вы не можете добавлять рецепты'

    """Добавлять Ингридиенты по вкусу может любой желающий """

    def add_ingredient(self, dish_name, *args):
        if len(self.model.recipe_list) == 0:
            print(self.get_default_action())
            return 'список рецептов пуст'
        else:
            for items in self.model.recipe_list:
                if dish_name == items['Название рецепта :']:
                    items['Ингридиенты: '].append({'Добавлены ингридиенты: ': (args)})
                    print(self.get_default_action())
                    print('Ингридиент/ы успешно добавлен/ы')
                else:
                    return 'Рецепт не найден'

                return self.model.recipe_list

    """Посмотреть описание блюда по его названию (доступно всем пользователям)!"""

    def get_recipe_description(self, dish_name):
        if self.model.get_recipe_list():
            for item in self.model.recipe_list:
                if dish_name == item['Название рецепта :']:
                    print(self.get_default_action())
                    return item['Описание: ']
                else:
                    return None
        else:
            print(self.get_default_action())
            return 'Список рецептов пуст!'

    """Запись списка рецептов в файл: доступно только для админов!!!"""

    def update_json_auth(self, filename, user_roll):
        if user_roll == 'admin':
            self.model.update_json(filename)
            return f'список рецептов записан в файл {filename}'
        else:
            return 'вы не можете записывать в файл'
