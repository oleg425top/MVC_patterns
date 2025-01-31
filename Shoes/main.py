from shoes_controller import ShoesController
from shoes_model import Shoes
from shoes_view import ShoesView

if __name__ == '__main__':
    model = Shoes()
    controller = ShoesController(model)
    view = ShoesView(controller)
    view.display_add_shoes('Мужская', 'Кроссовки', 'Черный', 5000, 'Nike', 45, 'NK-12345', r'shoes_user.json', 'admin')
    view.display_add_shoes('Мужская', 'Туфли', 'Серый', 6000, 'Clarks', 43, 'CL-23456', r'shoes_user.json', 'user')
    view.display_add_shoes('Женская', 'Сандали', 'Бежевый', 1000, 'Birkenstock', 36, 'BK-78901', r'shoes_user.json',
                           'admin')
    view.display_add_shoes('Женская', 'Сапоги', 'Красный', 10000, 'Timberland', 37, 'TB-67890', r'shoes_user.json',
                           'admin')
    print()
    view.display_get_shoes_list_auth('admin')
    print()
    view.display_get_shoes_list_auth('user')
    print()
    view.display_get_shoes_list_auth('uer')
    print()
    view.display_get_only_female_shoes()
    print()
    view.display_get_only_male_shoes()
    print()
    view.display_get_full_prise('admin')
