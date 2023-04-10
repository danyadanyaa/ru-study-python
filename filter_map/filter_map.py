from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result_list = []
        for element in input_array:
            flag, value = func(element)
            if flag:
                result_list.append(value)
        return result_list
