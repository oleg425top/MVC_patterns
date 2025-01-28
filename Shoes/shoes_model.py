import json


class Shoes:
    def __init__(self):
        self.shoes_list = []

    def get_shoes_list(self):
        return self.shoes_list

    def add_shoes(self, gender: str, shoe_type:str, color:str, prise: int or float, manufacturer:str, size:int, filename ):
        data = {'Тип обуви: ': gender, 'Вип обуви: ': shoe_type, 'Цвет: ': color,
                'Цена: ': prise, 'Производитель: ': manufacturer, 'Размер: ': size,}
        self.shoes_list.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.shoes_list, file, ensure_ascii=False, indent=3)
