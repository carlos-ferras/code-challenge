from typing import Tuple

Line = Tuple[int, int]


def is_number_inside_boundaries(number: int, boundaries: Line) -> bool:
    return min(boundaries) <= number <= max(boundaries)
