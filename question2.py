"""
В текущем файле рассмотрены три версии реализации неограниченного циклического
буфера FIFO:

1. BufferFifoList - Основывается на использовании обычного списка.
Направление добавления/извлечения элементов из списка не играет роли, т.к.
реализация основывается на паре методов списка: insert() и pop(), либо
append() и pop(0).
Сложность добавления/извлечение элемента из начало списка будет равно О(n) по
причине позиционного сдвига всех элементов.

2. BufferFifoDeque - Основывается на использовании двусвязного списка на основе
встроенного в Python класса deque модуля collections.
Направление добавления/извлечения элементов из списка не играет роли. Сложность
выполнения указанных методов равна О(1). Реализация данной версии является
самой быстрой из представленных.

3. BufferLinkedFifo - Основывается на использовании двусвязного списка,
собственной реализации. Время выполнения данной сортировки выше, чем
у 1основанного на классе deque по

"""

from collections import deque


class BufferFifoList:
    """
        Класс для реализации циклического буфера FIFO на основе списка.

        Methods
        -------
        add(element) : Any
            Добавляет элемент в начало очереди
        extract(element) : Any
            Извлекает элемент с конца очереди
        get_queue() : Any
            Возвращает список всех элементов находящихся в буфере
        head() : Any
            Получает первый элемент в очереди на извлечение
        tail() : Any
            Получает последний добавленный элемент в очередь
        """
    def __init__(self):
        self.queue = []

    def add(self, element):
        """Добавляет элемент в начало очереди"""
        return self.queue.insert(0, element)

    def extract(self):
        """Извлекает элемент с конца очереди"""
        return self.queue.pop()

    def get_queue(self):
        """Возвращает список всех элементов находящихся в буфере"""
        return self.queue

    def head(self):
        """Получает первый элемент в очереди на извлечение"""
        return self.queue[-1]

    def tail(self):
        """Получает последний добавленный элемент в очередь"""
        return self.queue[0]


def test_buffer_fifo_list():
    """Проверка выполнения работы буфера на основе списка"""
    buffer_fifo = BufferFifoList()
    buffer_fifo.add('first')
    buffer_fifo.add('second')
    buffer_fifo.add('third')
    print('Наполненный буфер: ', buffer_fifo.get_queue())
    print('Первый извлеченный элемент: ', buffer_fifo.extract())
    print('Второй извлеченный элемент: ', buffer_fifo.extract())
    print('Третий извлеченный элемент: ', buffer_fifo.extract())
    print('Текущее состояние буфера: ', buffer_fifo.get_queue())


# test_buffer_fifo_list()


class BufferFifoDeque:
    """
        Класс для реализации циклического буфера FIFO на основе встроенного
        в Python модуля deque.

        Methods
        -------
        add(element) : Any
            Добавляет элемент в начало очереди
        extract(element) : Any
            Извлекает элемент с конца очереди
        get_queue() : Any
            Возвращает список всех элементов находящихся в буфере
        head() : Any
            Получает первый элемент в очереди на извлечение
        tail() : Any
            Получает последний добавленный элемент в очередь
    """
    def __init__(self):
        self.queue = deque()

    def add(self, element):
        """Добавляет элемент в начало очереди"""
        return self.queue.appendleft(element)

    def extract(self):
        """Извлекает элемент с конца очереди"""
        return self.queue.pop()

    def get_queue(self):
        """Возвращает список всех элементов находящихся в буфере"""
        return self.queue

    def head(self):
        """Получает первый элемент в очереди на извлечение"""
        return self.queue[-1]

    def tail(self):
        """Получает последний добавленный элемент в очередь"""
        return self.queue[0]


def test_buffer_fifo_deque():
    """Проверка выполнения работы буфера на основе модуля deque"""
    buffer_fifo = BufferFifoDeque()
    buffer_fifo.add('first')
    buffer_fifo.add('second')
    buffer_fifo.add('third')
    print('Наполненный буфер: ', buffer_fifo.get_queue())
    print('Первый извлеченный элемент: ', buffer_fifo.extract())
    print('Второй извлеченный элемент: ', buffer_fifo.extract())
    print('Третий извлеченный элемент: ', buffer_fifo.extract())
    print('Текущее состояние буфера: ', buffer_fifo.get_queue())


# test_buffer_fifo_deque()


class BufferData:
    """Класс содержит сведения об элементе двусвязного списка.

    Attributes:
    ----------
    data : Any
        Содержит фактические данные элемента буфера
    next :
        Содержит ссылку на следующий элемент очереди
    prev :
        Содержит ссылку на предыдущий элемент очереди

    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BufferLinkedFifo:
    """
    Класс для реализации циклического буфера FIFO на основе двусвязного списка.

    Methods:
    -------
    add_at_start : Any
        Вставляет любой элемент в начало двусвязного списка
    add_at_end : Any
        Вставляет любой элемент в конец двусвязного списка
    del_at_start :
        Удаляет элемент, находящийся в начале двусвязного списка
    del_at_end :
        Удаляет элемент, находящийся в конце двусвязного списка
    """
    def __init__(self):
        self.start_el = None

    def __add_at_empty_buffer(self, data):
        """Вставка элемента в пустой список"""
        if self.start_el is None:
            new_el = BufferData(data)
            self.start_el = new_el
        else:
            print('Список не пустой')

    def add_at_start(self, data):
        """Вставка элемента в начало двусвязного списка"""
        if self.start_el is None:
            self.__add_at_empty_buffer(data)
        new_el = BufferData(data)
        new_el.next = self.start_el
        self.start_el.prev = new_el
        self.start_el = new_el

    def add_at_end(self, data):
        """Вставка элемента в конец двусвязного списка"""
        if self.start_el is None:
            self.__add_at_empty_buffer(data)
        el = self.start_el
        while el.next is not None:
            el = el.next
        new_el = BufferData(data)
        new_el.next = new_el
        new_el.prev = el

    def del_at_start(self):
        """Удаление элемента с начала связного списка"""
        if self.start_el is None:
            return print('Список не содержит элементов для удаления')
        if self.start_el.next is None:
            self.start_el = None
        self.start_el = self.start_el.next

    def del_at_end(self):
        """Удаление элемента с конца связного списка"""
        if self.start_el is None:
            print('Список не содержит элементов для удаления')
        if self.start_el.next is None:
            self.start_el = None
        el = self.start_el
        while el.next is not None:
            el = el.next
        el.prev.next = None

    def get_buffer(self):
        """Получение всего буфера"""
        if self.start_el is None:
            print('Буфер не содержит элементов')
        else:
            el = self.start_el
            while el is not None:
                print(el.data, ' ')
                el = el.next


def test_buffer_linked_list():
    """Проверка выполнения работы буфера на основе двусвязного списка"""
    linked_list = BufferLinkedFifo()
    linked_list.add_at_start(25)
    linked_list.add_at_start(35)
    linked_list.add_at_start(45)
    linked_list.add_at_start(55)
    linked_list.del_at_end()
    linked_list.del_at_end()
    linked_list.get_buffer()


# test_buffer_linked_list()
