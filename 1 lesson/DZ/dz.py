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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def creat_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <=0:
            print('Некорректная цена')
        else:
            self.__price = new_price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.price * other.quantity



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
        self. __product = product
        Category.all_category += 1
        for i in range(len(self.__product)): #добавление новых уникальных продуктов
            if not self.__product[i] in Category.all_product:
                Category.all_product.append(self.__product[i])
        Category.quantity_product = len(Category.all_product) #количество уникальных продуктов

    def add_product(self, value):
        self.__product.append(value)

    @property
    def list_prod(self):
        list=[]
        for list in self.product:
            list.append (f'{product.name},{product.price} руб. Остаток {product.quantity}')
            return list

    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.quantity_product} шт.'






