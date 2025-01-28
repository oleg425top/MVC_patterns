from shoes_controller import ShoesController
from shoes_model import Shoes
from shoes_view import ShoesView

if __name__ == '__main__':
    filename = r'shoes_user.json'
    model = Shoes()
    controller = ShoesController(model)
    view = ShoesView(controller)
    view.display_add_shoes('Мужская', 'Кроссовки', 'Черный', 5000, 'Nike', 42, 'NK-12345', filename)
    view.display_get_shoes_list_auth('admin')
