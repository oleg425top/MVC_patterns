class User:
    def __init__(self, user_roll= None):
        self.user_roll = user_roll


    def get_auth_user(self):
        if self.user_roll == 'admin':
            return True
        else:
            return False

class ShoesView:
    def __init__(self, controller):
        self.controller = controller

    def display_get_shoes_list_auth(self, user_roll):
        result = self.controller.get_shoes_list_auth(user_roll)
        if not result:
            print(self.controller.get_default_action())
            print('у вас нет прав доступа')
        else:
            print(self.controller.get_default_action())
            print(self.controller.get_shoes_list_auth(user_roll))

    def display_get_only_female_shoes(self):
        female = self.controller.get_only_female_shoes()
        print(self.controller.get_default_action())
        print(f'Подборка только женской обуви со склада:\n{female}')

    def display_get_only_male_shoes(self):
        male = self.controller.get_only_male_shoes()
        print(self.controller.get_default_action())
        print(f'Подборка только мужской обуви со склада:\n{male}')

    def display_add_shoes(self, gender, shoe_type, color, prise, manufacturer,size, article, filename, user_roll):
        result = self.controller.add_shoes(gender, shoe_type, color, prise, manufacturer, size, article, filename, user_roll)
        if result == 'У вас нет прав доступа для данной операции!!!':
            print(self.controller.get_default_action())
            print(result)
        else:
            print(self.controller.get_default_action())
            print(result)

    def display_get_full_prise(self, user_roll):
        result = self.controller.get_full_prise(user_roll)
        if result == 'У вас нет прав доступа для данной операции!!!':
            print(self.controller.get_default_action())
            print(result)
        else:
            print(self.controller.get_default_action())
            print(result)
