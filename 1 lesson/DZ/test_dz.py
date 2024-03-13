import pytest
from dz import Product
from dz import Category
all_category = 0
a = Category('шарики', 'шары', ['красный', 'белый','второй'])
b = Category('кубики', 'кубы', ['черный', 'белый','третий'])
c = Product('шарик1','шарик резиновый', 3.5, 10)
print(Category.all_category)
def test_init():
    assert a.name =='шарики'
    assert c.price == 3.5

def test_all_prod():
    assert len(Category.all_product) == 5

def test_all_categ():
    assert Category.all_category == 2
