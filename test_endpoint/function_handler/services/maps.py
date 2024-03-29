from typing import Literal
import numpy

color_mapper: dict[Literal['red', 'green', 'blue'], int] \
    = {'red': 0, 'green': 1, 'blue': 2}


def function_mapper(function: str, value_1: float, value_2: float) -> float:
    function_lst = ['pow', 'sum', 'prod']
    with_numpy_str = f'numpy.{function}([{value_1},{value_2}])'
    without_numpy_str = f'{function}({value_1},{value_2})'

    if function in function_lst:  # TODO How to implement function call without eval?
        try:
            return float(eval(with_numpy_str))
        except AttributeError:
            return eval(without_numpy_str)
