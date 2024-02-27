"""
1. Используется два сгенерированных рандомно списка из целых чисел.
2. Выполняется замер скорости выполнения сортировок.
"""

import random
import time
from question3 import merge_sort, quick_sort


unsort_list1 = [random.randrange(-100_000, 100_000, 1) for i in range(100_000)]
unsort_list2 = [random.randrange(-100_000, 100_000, 1) for j in range(100_000)]

start_quick_sort = time.time()
quick_sort(unsort_list1, 0, len(unsort_list1) - 1)
end_quick_sort = time.time()
time_quick_sort = end_quick_sort - start_quick_sort

start_merge_sort = time.time()
merge_sort(unsort_list2)
end_merge_sort = time.time()
time_merge_sort = end_merge_sort - start_merge_sort

print(f'Время выполнения быстрой сортировки: {time_quick_sort}')
print(f'Время выполнения merge сортировки: {time_merge_sort}')
