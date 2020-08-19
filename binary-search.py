def binary_search(value, array, start_idx=None, end_idx=None):
    """
    Выболняет бинарный поиск значения в отсортированном по возрастанию массиве.

    :param value: Значение, которое необходимо найти.
    :param array: Массив поиска.
    :param start_idx: Начальный индекс поиска (для рекурсивного вызова)
    :param end_idx: Конечный индекс поиска (для рекурсивного вызова)
    :return: Возвращает индекс элемента массива, содержащего искомое значение. Либо -1, если такой элемент не найден.
    """
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(array)

    array_length = end_idx - start_idx

    if array_length == 1:   # Базовый случай рекурсии
        if array[start_idx] == value:
            return start_idx
        else:
            return -1
    elif array_length <= 0:
        return

    middle_idx = start_idx + array_length // 2

    if value == array[middle_idx]:
        return middle_idx
    elif value < array[middle_idx]:
        return binary_search(value, array, start_idx, middle_idx)
    elif value > array[middle_idx]:
        return binary_search(value, array, middle_idx, end_idx)


if __name__ == '__main__':
    from random import randint

    # Сгенерировать массив случайной длины состоящий из случайных чисел
    array = [randint(0, 100) for _ in range(randint(10, 100))]
    array.sort()

    # Получить число, входящее в массив.
    number_in_array = array[randint(0, len(array))]

    # Получить число, не входящее в массив
    for number_not_in_array in range(len(array)):
        if number_not_in_array not in array:
            break

    assert binary_search(number_in_array, array) >= 0, "Поиск числа, входящего в массив"
    assert binary_search(number_not_in_array, array) == -1, "Поиск числа, не входящего в массив"

    array = [0, 2, 3, 5, 8, 10, 11, 45, 94]
    number = 5
    assert binary_search(number, array) == 3, 'Определение индекса числа, входящего в массив'
