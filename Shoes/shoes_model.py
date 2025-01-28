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

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.shoes_list, file, ensure_ascii=False, indent=3)

    def get_full_prise(self):
        full_prise = 0
        for shoe in self.shoes_list:
            full_prise += shoe['Цена: ']
        print('Общая стоимость: ')
        return full_prise

if __name__ == '__main__':
    filename = r'shoes.json'
    shoe_list = Shoes()
    shoe_list.get_shoes_list()
    shoe_list.add_shoes('Мужская', 'Кроссовки', 'Черный', 5000, 'Nike', 42, 'NK-12345', filename)
    shoe_list.add_shoes('Мужская', 'Туфли', 'Серый', 6000, 'Clarks', 43, 'CL-23456', filename)
    shoe_list.add_shoes('Женская', 'Сапоги', 'Красный', 10000, 'Timberland', 37, 'TB-67890', filename)
    shoe_list.add_shoes('Женская', 'Сандали', 'Бежевый', 1000, 'Birkenstock', 36, 'BK-78901', filename)
    print(shoe_list.get_shoes_list())
    print(shoe_list.get_full_prise())
