from recipe_model import ModelRecipe
from recipe_view import ViewRecipe
from recipe_controller import ControllerRecipe

if __name__ == '__main__':
    model = ModelRecipe()
    controller = ControllerRecipe(model)
    view = ViewRecipe(controller)


    view.display_add_recipe('Оливье', 'Людмила Иванова', 'салат',
                               'Оливье — это традиционный русский салат, который обычно подают на праздничные столы.',
                               ['300 г вареного картофеля', '200 г вареной моркови', '200 г вареной колбасы или ветчины',
                                '100 г зеленого горошка', '100 г соленых огурцов', '3 вареных яйца', '200 г майонеза',
                                'Соль и перец по вкусу'], 'Русская', 'admin')
    view.display_add_recipe('Паста с томатным соусом', 'Антонио Росси', 'Второе блюдо',
                           'Паста с томатным соусом — это простое и вкусное итальянское блюдо, которое можно приготовить за считанные минуты.',
                           ['400 г пасты', '400 г консервированных помидоров', '2 зубчика чеснока',
                            '2 столовые ложки оливкового масла', 'Соль и перец по вкусу',
                            'Свежий базилик для украшения'], 'Итальянская', 'user')
    view.display_add_recipe('Круассаны', 'Пьер Дюпон', ' Выпечка',
                           'Круассаны — это знаменитая французская выпечка, которая  идеально подходит для завтрака или перекуса с чашечкой кофе.',
                           ['500 г муки', '250 мл теплого молока', '10 г сухих дрожжей', '50 г сахара',
                            '1 чайная ложка соли', '200 г сливочного масла', '1 яйцо для смазывания'], 'Французская', 'admin')
    print()
    view.display_recipe_list()
    print()
    view.display_recipe_description('Круассаны')
    print()
    view.display_recipe_description('Оливье')
    print()
    view.display_json_update_auth(r'recipe_list.json', 'admin')
    view.display_add_ingredient('Оливье', 'горчица', 'кукуруза')
    view.display_add_ingredient('Круассаны', 'ванилин', 'джем')
    print()
    view.display_recipe_list()
    view.display_json_update_auth(r'new_recipe_list.json', 'admin')
    view.display_json_update_auth(r'new_recipe_list.json', 'user')

