import random
import time

def bubble_sort(arr):
    """
    Пузырьковая сортировка.
    Проходим по списку, сравнивая соседние элементы и меняя их местами, если они не в порядке.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    """
    Сортировка выбором.
    На каждом шаге выбирается минимальный элемент в неотсортированной части списка и меняется с текущим элементом.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    """
    Сортировка слиянием.
    Рекурсивное разбиение массива на две части, их сортировка и слияние.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Слияние отсортированных списков
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Добавление оставшихся элементов из left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Добавление оставшихся элементов из right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    """
    Быстрая сортировка.
    Рекурсивно разделяет массив на подмассивы относительно опорного элемента.
    Возвращает новый отсортированный список.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Создаем случайный тестовый набор данных.
    # Размер можно увеличивать, но учитывайте, что O(n²) алгоритмы (пузырьковая и выбором) могут работать медленно.
    N = 1000  # Размер массива
    test_data = [random.randint(0, 10000) for _ in range(N)]

    results = []

    # Тестируем пузырьковую сортировку
    data = test_data.copy()
    start_time = time.perf_counter()
    bubble_sort(data)
    elapsed = time.perf_counter() - start_time
    results.append(("Пузырьковая сортировка", elapsed))

    # Тестируем сортировку выбором
    data = test_data.copy()
    start_time = time.perf_counter()
    selection_sort(data)
    elapsed = time.perf_counter() - start_time
    results.append(("Сортировка выбором", elapsed))

    # Тестируем сортировку слиянием
    data = test_data.copy()
    start_time = time.perf_counter()
    merge_sort(data)
    elapsed = time.perf_counter() - start_time
    results.append(("Сортировка слиянием", elapsed))

    # Тестируем быструю сортировку (возвращает новый список)
    data = test_data.copy()
    start_time = time.perf_counter()
    sorted_data = quick_sort(data)
    elapsed = time.perf_counter() - start_time
    results.append(("Быстрая сортировка", elapsed))

    # Выводим результаты работы алгоритмов
    print("Результаты сортировки:")
    for algorithm, time_taken in results:
        print(f"{algorithm}: {time_taken:.6f} секунд")
