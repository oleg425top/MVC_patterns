class ControllerRecipe:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return f'Наш список рецептов: {self.model.__class__.__name__}!!!!'

    """Список рецептов может посмотреть любой пользователь!!"""

    def get_recipe_list(self):
        return self.model.get_recipe_list()

    """А вот добавить рецепт только админ!!"""

    def add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                   list_of_ingredients, kitchen_name, user_roll):
        if user_roll == 'admin':
            self.model.add_recipe(self, recipe_name, recipe_author, recipe_type, recipe_description,
                                  list_of_ingredients, kitchen_name)
