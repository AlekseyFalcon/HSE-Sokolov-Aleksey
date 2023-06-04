import random
import time

# Создать массив со случайным шагом
start = 10
end = 250000000
step = random.randint(3, 5)
arr = list(range(start, end, step))

# Сгенрировать 10 случайных чисел
random_nums = [random.randint(start, end) for _ in range(10)]

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Линейный поиск
start_time = time.time()
for num in random_nums:
    result = linear_search(arr, num)
    if result != -1:
        print(f"Элемент присутствует в индексе {str(result)} используя линейный поиск.")
    else:
        print("Элемент отсутствует в массиве.")
end_time = time.time()
print(f"Линейный поиск занял {(end_time - start_time)} секунд.")

# Бинарный поиск
start_time = time.time()
for num in random_nums:
    result = binary_search(arr, 0, len(arr)-1, num)
    if result != -1:
        print(f"Элемент присутствует в индексе {str(result)} используя бинарный поиск.")
    else:
        print("Элемент отсутствует в массиве.")
end_time = time.time()
print(f"Бинарный поиск занял  {(end_time - start_time)} секунд.")
