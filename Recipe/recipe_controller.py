class ControllerRecipe:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return f'Добро пожаловать в : {self.model.__class__.__name__}!!!!'

    """Список рецептов может посмотреть любой пользователь!!"""

    def get_recipe_list(self):
        data = self.model.get_recipe_list()
        if len(data) == 0:
            return 'Список рецептов пуст'
        else:
            return self.model.get_recipe_list()

    """А вот добавить рецепт только админ!!"""

    def add_recipe(self, recipe_name: str, recipe_author: str, recipe_type: str, recipe_description: str,
                   list_of_ingredients: list, kitchen_name: str, user_roll='user'):
        if user_roll == 'admin':
            # print(self.get_default_action())
            self.model.add_recipe(recipe_name, recipe_author, recipe_type, recipe_description,
                                  list_of_ingredients, kitchen_name)
            return 'Рецепт добавлен с список'
        else:
            # print(self.get_default_action())
            return 'Вы не можете добавлять рецепты'

    """Добавлять Ингридиенты по вкусу может любой желающий """

    def add_ingredient(self, dish_name, *args):
        data = self.model.get_recipe_list()
        if len(data) == 0:
            return 'список рецептов пуст'
        else:
            for items in data:
                if items['Название рецепта :'] == dish_name:
                    items['Ингридиенты: '].append({'Добавленные ингридиенты: ':args})
                    return f'Ингридиент/ы: {args} - успешно добавлен/ы в {dish_name}'


    """Посмотреть описание блюда по его названию (доступно всем пользователям)!"""

    def get_recipe_description(self, dish_name):
        if len(self.model.get_recipe_list()) != 0:
            for item in self.model.recipe_list:
                if item['Название рецепта :'] == dish_name:
                    # print(self.get_default_action())
                    return item['Описание: ']

        else:
            # print(self.get_default_action())
            return 'Список рецептов пуст!'

    """Запись списка рецептов в файл: доступно только для админов!!!"""

    def update_json_auth(self, filename, user_roll):
        if user_roll == 'admin':
            self.model.update_json(filename)
            return f'список рецептов записан в файл {filename}'
        else:
            return 'вы не можете записывать в файл'
