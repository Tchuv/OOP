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
    products: list #список продуктов в категории
    all_category = 0 #количество категорий
    all_products = [] #список всех уникальных продуктов
    quantity_product = 0 #общее количествоуникальных продуктов


    def __init__(self, name, description, products):
        '''Инициализация обьекта Category'''
        self.name = name
        self.description = description
        self. __products = products
        Category.all_category += 1
        for i in range(len(self.__products)): #добавление новых уникальных продуктов
            if not self.__products[i] in Category.all_products:
                Category.all_products.append(self.__products[i])
        Category.quantity_product = len(Category.all_products) #количество уникальных продуктов

    def add_products(self, value):
        self.__products.append(value)

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product}\n'
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.quantity_product} шт.'

a = Category('шарики', 'шары надувные', [['красный', 'шарик резиновый', 3.5, 5], ['белый','шарик силиконовый', 5.5, 7]])
b = Category('кубики', 'кубы деревянные', ["'тяжёлый', 'куб свинцовый, 7, 2", "'легкий','куб деревянный', 2, 10"])
c = Product('шарик1','шарик резиновый', 3.5, 10)


