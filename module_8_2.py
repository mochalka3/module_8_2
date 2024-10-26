def personal_sum(numbers):
    """
    Подсчитывает сумму чисел в коллекции numbers.
    Обрабатывает исключения TypeError для нечисловых данных.

    Args:
        numbers (iterable): Коллекция чисел.

    Returns:
        tuple: Кортеж из двух значений:
            - result (int): Сумма чисел.
            - incorrect_data (int): Количество некорректных данных.
    """
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {number}")
    return result, incorrect_data


def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое чисел в коллекции numbers.
    Обрабатывает исключения ZeroDivisionError и TypeError.

    Args:
        numbers (iterable): Коллекция чисел.

    Returns:
        float: Среднее арифметическое, или None в случае ошибки.
    """
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if isinstance(numbers, (list, tuple, set, str)):
            return total_sum / len(numbers)
        else:
            print("В numbers записан некорректный тип данных")
            return None
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

# Пример использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
