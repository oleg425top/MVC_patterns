class ShoesController:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return f'Добро пожаловать на склад обуви!!{self.model.__class__.__name__}'

    def get_shoes_list_auth(self, user_roll='user'):
        print(self.get_default_action())
        if user_roll == 'admin':
            return self.model.get_shoes_list()
        elif user_roll:
            # эти действия наверное должны быть в модели, в виде отдельной функции?
            data = self.model.get_shoes_list()
            data_for_user = []
            for item in data:
                new_data = [
                    {'Вид обуви: ': item['Вид обуви: '], 'Размер: ': item['Размер: '], 'Цена: ': item['Цена: '],
                     'Производитель: ': item['Производитель: ']}]
                data_for_user.append(new_data)
            return data_for_user
        else:
            return None  # 'ваш статус не определен в программе'

    """выбор только женской обуви"""

    def get_only_female_shoes(self):
        print(self.get_default_action())
        female_shoes = []
        data = self.model.get_shoes_list()
        for elem in data:
            if elem['Тип обуви: '] == 'Женская':
                female_shoes.append(elem)
            return female_shoes

    """выбор только мужской обуви"""

    def get_only_male_shoes(self):
        print(self.get_default_action())
        male_shoes = []
        data = self.model.get_shoes_list()
        for elem in data:
            if elem['Тип обуви: '] == 'Мужская':
                male_shoes.append(elem)
            return male_shoes
        return None

    def add_shoes(self,gender: str, shoe_type: str, color: str, prise: int or float, manufacturer: str, size: int,
                  article, filename, user_roll='user'):
        if user_roll == 'admin':
            print(self.get_default_action())
            return self.model.add_shoes(gender, shoe_type, color, prise, manufacturer,article, filename)
        else:
            print(self.get_default_action())
            return 'У вас нет прав доступа для данной операции!!!'

    def get_full_prise(self, user_roll):
        if user_roll == 'admin':
            print(self.get_default_action())
            return self.model.get_full_prise()
        else:
            return 'У вас нет прав доступа для данной операции!!!'
