class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        maximum = 0
        for i in range(len(input_list)):
            if input_list[i] > maximum:
                maximum = input_list[i]
        return [maximum if element > 0 else element for element in input_list]

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
