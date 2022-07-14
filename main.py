class rec:
    pass # Объект пустого пространства имён

rec.name = "Bob" # просто объект с атрибутами
rec.age = 40

print(rec.name)

x = rec() # Экземпляры наследуют имена класса
y = rec()
print(x.name, y.name)

x.name = "Alina"

print(x.name, y.name)

nnn = list(rec.__dict__.keys()) # Атрибуты класса rec
print(nnn)
nnnn = list(name for name in rec.__dict__ if not name.startswith("__"))
print(nnnn)
nnnnn = list(x.__dict__.keys()) # Атрибуты объекта x
print(nnnnn)
nnnnnn = list(y.__dict__.keys()) # Атрибуты объекта y
print(nnnnnn)

mmm = x.name, x.__dict__["name"] # Представленные здесь атрибуты являются ключами словаря
print(mmm)
mmmm = x.age
print(mmmm) # Но извлечение атрибута проверяет также классы
#x.__dict__["age"] # Индексирвоание словаря не производит поиск в иерархии наследования. ВЫЙДЕТ ОШИБКА
mmmmm = x.__class__ # Связь экземпляра с классом
print(mmmmm)
mmmmmm = rec.__bases__ # Связь с суперклассами
print(mmmmmm)

def uppername(obj): # По - прежнему неободходим аргумент self(obj)
    return obj.name.upper()
aaa = uppername(x)
print(aaa)
rec.method = uppername # Теперь это метод класса
bbb = x.method() # Запустить метод для обработки x
bbbb = y.method() # То же самое, но передать y для self
print(bbb)
print(bbbb)
bbbb = rec.method(x)
print(bbbb)





