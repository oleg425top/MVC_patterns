class ShoesController:

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return 'Добро пожаловать на склад обуви!!'

    def get_shoes_list_auth(self, user_roll = 'user'):
        if user_roll == 'admin':
            return self.model.get_shoes_list()
        elif user_roll:
            data = self.model.get_shoes_list()
            data_for_user = []
            for item in data:
                new_data = [
                    {'Вид обуви: ': item['Вид обуви: '], 'Размер: ': item['Размер: '], 'Цена: ': item['Цена: ']}, self]
                data_for_user.append(new_data)
            return data_for_user
        else:
            return 'ваш статус не определен в программе'