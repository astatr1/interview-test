def isEven(value):
    """Реализация из тестового задания"""
    return value % 2 == 0


def is_even(value: int) -> bool:
    """Определяет четность числа"""
    if not isinstance(value, int):
        raise TypeError('Переданный параметр должен быть целым числом!')
    else:
        return value % 2 == 0


def test_is_even():
    """Проверка функции определения четности числа"""
    print(is_even(6))
    print(is_even(5))
    # print(is_even('string'))
    # print(is_even(4.2))
    # print(is_even([4]))


test_is_even()

"""
1. Наименование функций согласно pep8 не может содержать заглавных букв.

2. Функция isEven принимает любой тип данных. Реализация аннотации параметров
функции помогает предотвратить передачу неподдерживаемых типов данных. Так же
при выполнении проверки статическим анализатором, например mypy, позволяет
находить ошибки несоответствия типов в коде перед деплоем проекта.

3. Реализация проверки переданного параметра внутри функции позволяет к
примеру вызвать исключение.

"""