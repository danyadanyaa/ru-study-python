from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result_list = []
        for element in input_array:
            res = func(element)
            if res[0]:
                result_list.append(res[1])
        return result_list
