from shoes_controller import ShoesController
from shoes_model import Shoes
from shoes_view import ShoesView

if __name__ == '__main__':
    model = Shoes()
    controller = ShoesController(model)
    view = ShoesView(controller)