class Product:
    ''' класс Product'''

    name: str # имя
    description: str #описание
    price: float #цена
    quantity: int #количество

    def __init__(self, name, description, price, quantity):
        '''Иницилизация обьекта Product'''
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    ''' класс Category'''
    name: str #имя
    description: str #описание
    product: list #список продуктов в категории
    all_category = 0 #количество категорий
    all_product = [] #список всех уникальных продуктов
    quantity_product = 0 #общее количествоуникальных продуктов


    def __init__(self, name, description, product):
        '''Инициализация обьекта Category'''
        self.name = name
        self.description = description
        self.product = product
        Category.all_category += 1
        for i in range(len(self.product)): #добавление новых уникальных продуктов
            if not self.product[i] in Category.all_product:
                Category.all_product.append(self.product[i])
        Category.quantity_product = len(Category.all_product) #количество уникальных продуктов




