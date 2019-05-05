from typing import Tuple

Line = Tuple[int, int]


def is_number_inside_boundaries(number: int, boundaries: Line) -> bool:
    return min(boundaries) <= number <= max(boundaries)


def overlap_ordered(line1: Line, line2: Line) -> bool:
    return is_number_inside_boundaries(line1[0], line2) or is_number_inside_boundaries(line1[1], line2)


def overlap(line1: Line, line2: Line) -> bool:
    return overlap_ordered(line1, line2) or overlap_ordered(line2, line1)
