class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        return [max(input_list) if i > 0 else i for i in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if not input_list:
            return -1
        mid = len(input_list) // 2
        if input_list[mid] == query:
            return mid
        elif input_list[mid] < query:
            new_mid = mid + 1
            result = ListExercise.search(input_list[new_mid:], query)
            if result == -1:
                return -1
            else:
                return mid + result + 1
        else:
            return ListExercise.search(input_list[:mid], query)
