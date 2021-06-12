 ### Разработать фрагмент электронного ресурса, посвященного шаблону проектирования «Абстрактная фабрика». Привести пример фрагмента кода, реализующего указанный шаблон,публиковать его в портфолио.

**Абстрактная фабрика** — это порождающий паттерн проектирования, который решает проблему создания целых семейств связанных продуктов, без указания конкретных классов продуктов.

Применяется в случаях:

* Когда программа должна быть независимой от процесса и типов создаваемых новых объектов.

* Когда необходимо создать семейства или группы взаимосвязанных объектов исключая возможность одновременного использования объектов из разных этих наборов в одном контексте

#### Плюсы

* изолирует конкретные классы;

* упрощает замену семейств продуктов;

* гарантирует сочетаемость продуктов.

#### Минусы

* сложно добавить поддержку нового вида продуктов.

#### Применение

* Система не должна зависеть от того, как создаются, компонуются и представляются входящие в неё объекты.

* Входящие в семейство взаимосвязанные объекты должны использоваться вместе и вам необходимо обеспечить выполнение этого ограничения.

* Система должна конфигурироваться одним из семейств составляющих её объектов.

* Требуется предоставить библиотеку объектов, раскрывая только их интерфейсы, но не реализацию.

```python
class AbstractFactory(object):
  def create_drink(self):
    raise NotImplementedError()
  def create_food(self):
    raise NotImplementedError()
 
class Drink(object):
  def __init__(self, name):
    self._name = name
  def __str__(self):
    return self._name
 
class Food(object):
  def __init__(self, name):
    self._name = name
  def __str__(self):
    return self._name
 
class ConcreteFactory1(AbstractFactory):
  def create_drink(self):
    return Drink('Coca-cola')
  def create_food(self):
    return Food('Hamburger')
 
class ConcreteFactory2(AbstractFactory):
  def create_drink(self):
    return Drink('Pepsi')
  def create_food(self):
    return Food('Cheeseburger')
 
def get_factory(ident):
  if ident == 0:
    return ConcreteFactory1()
  elif ident == 1:
    return ConcreteFactory2()
 
factory = get_factory(1) # 0 or 1
print(factory.create_drink())
print(factory.create_food())
```

```
Pepsi
Cheeseburger
```
