import time

from question2 import BufferFifoList, BufferFifoDeque, BufferLinkedFifo


n = 100_000

buffer_list = BufferFifoList()
buffer_deque = BufferFifoDeque()
buffer_linked_list = BufferLinkedFifo()


def average_time(func, count):
    start = time.time()
    for i in range(count):
        func(i)
    end = time.time()
    return end - start


list_time = average_time(lambda i: buffer_list.add(i), n)
deque_time = average_time(lambda i: buffer_deque.add(i), n)
linked_time = average_time(lambda i: buffer_linked_list.add_at_start(i), n)

print(f'Время добавления в список: {list_time} ms')
print(f'Время добавления в deque: {deque_time} ms')
print(f'Время добавления в linked_list: {linked_time} ms')
print(f'Соотношение list / deque: {list_time / deque_time}')
print(f'Соотношение list / linked: {list_time / linked_time}')
print(f'Соотношение linked / deque: {linked_time / deque_time}')