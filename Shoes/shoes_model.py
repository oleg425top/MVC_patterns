import json


class Shoes:
    def __init__(self):
        self.shoes_list = []

    def get_shoes_list(self):
        return self.shoes_list

    def add_shoes(self, gender: str, shoe_type: str, color: str, prise: int or float, manufacturer: str, size: int,
                  article, filename):
        data = {'Тип обуви: ': gender, 'Вид обуви: ': shoe_type, 'Цвет: ': color,
                'Цена: ': prise, 'Размер: ': size, 'Производитель: ': manufacturer, 'Артикул: ': article}
        self.shoes_list.append(data)
        self.update_json(filename)
        # return self.shoes_list

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.shoes_list, file, ensure_ascii=False, indent=3)

    def get_full_prise(self):
        full_prise = 0
        for shoe in self.shoes_list:
            full_prise += shoe['Цена: ']

        return f'Общая стоимость обуви на складе: \n {full_prise} рублей.'


