from abc import ABC, abstractmethod

class ABC_product(ABC):
    @abstractmethod
    def creat_product (cls, name, description, price, quantity):
        pass

class LogMixin:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__}({self.__dict__.items()})'


class Product(LogMixin, ABC_product):
    ''' класс Product'''

    name: str # имя
    description: str #описание
    price: float #цена
    quantity: int #количество

    def __init__(self, name, description, price, quantity):
        '''Иницилизация обьекта Product'''
        self.name = name
        self.description = description
        self.__price =  price
        try:
            self.quantity = quantity
        except ValueError:
            print("Товар с нулевым количеством не может быть добавлен")
            quit()
    @classmethod
    def creat_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Некорректная цена')
        else:
            self.__price = new_price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

class Category:
    ''' класс Category'''
    name: str  # имя
    description: str  # описание
    products: list  # список продуктов в категории
    all_category = 0  # количество категорий
    all_products = []  # список всех уникальных продуктов
    quantity_product = 0  # общее количествоуникальных продуктов

    def __init__(self, name, description, products):
        '''Инициализация обьекта Category'''
        self.name = name
        self.description = description
        self.__products = products
        Category.all_category += 1
        for i in range(len(self.__products)):  # добавление новых уникальных продуктов
            if not self.__products[i] in Category.all_products:
                Category.all_products.append(self.__products[i])
        Category.quantity_product = len(Category.all_products)  # количество уникальных продуктов

    def add_products(self, value):
        if not isinstance(value, Product ):
            raise TypeError('Ошибка. Обьект другого типа')
        self.__products.append(value)

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product}\n'
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.quantity_product} шт.'

class Smartphone(Product):
    """ дочерний класс телефоны"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


#ggg
class Lawn_grass(Product):
    """Дочерний класс Газонная трава"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country:str, germ_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germ_period = germ_period
        self.color = color















a = Category('шарики', 'шары надувные',
             [['красный', 'шарик резиновый', 3.5, 5], ['белый', 'шарик силиконовый', 5.5, 7]])
b = Category('кубики', 'кубы деревянные', ["'тяжёлый', 'куб свинцовый, 7, 2", "'легкий','куб деревянный', 2, 10"])
c = Product('шарик1', 'шарик резиновый', 3.5, 10)


