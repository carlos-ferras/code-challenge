import unittest

from ..overlap import is_number_inside_boundaries, overlap_ordered, overlap


class TestOverlap(unittest.TestCase):
    def test_number_inside_boundaries(self):
        self.assertEqual(
            is_number_inside_boundaries(5, (2, 8)),
            True,
            "Should return True if number is inside boundaries"
        )

    def test_number_bigger_than_boundaries(self):
        self.assertEqual(
            is_number_inside_boundaries(9, (2, 8)),
            False,
            "Should return False if number is bigger than the max boundary"
        )

    def test_number_smaller_than_boundaries(self):
        self.assertEqual(
            is_number_inside_boundaries(1, (2, 8)),
            False,
            "Should return False if number is smaller than the minor boundary"
        )

    def test_number_is_min_boundary(self):
        self.assertEqual(
            is_number_inside_boundaries(2, (2, 8)),
            True,
            "Should return True if number is the smaller boundary"
        )

    def test_number_is_max_boundary(self):
        self.assertEqual(
            is_number_inside_boundaries(8, (2, 8)),
            True,
            "Should return True if number is the bigger boundary"
        )

    def test_ordered_lines_overlap(self):
        self.assertEqual(
            overlap_ordered((1, 3), (2, 8)),
            True,
            "Should return True if the ordered lines overlap"
        )

    def test_ordered_lines_not_overlap(self):
        self.assertEqual(
            overlap_ordered((1, 3), (4, 8)),
            False,
            "Should return False if the ordered lines not overlap"
        )

    def test_ordered_lines_common_boundary(self):
        self.assertEqual(
            overlap_ordered((1, 4), (4, 8)),
            True,
            "Should return True if the ordered lines share a boundary"
        )

    def test_ordered_lines_contained(self):
        self.assertEqual(
            overlap_ordered((1, 4), (0, 8)),
            True,
            "Should return True if the second line contain the first"
        )

    def test_unordered_lines_overlap_case1(self):
        self.assertEqual(
            overlap((1, 3), (2, 8)),
            True,
            "Should return True if the unordered lines overlap [case 1]"
        )

    def test_unordered_lines_overlap_case2(self):
        self.assertEqual(
            overlap((2, 8), (1, 3)),
            True,
            "Should return True if the unordered lines overlap [case 2]"
        )

    def test_unordered_lines_not_overlap_case1(self):
        self.assertEqual(
            overlap((1, 3), (4, 8)),
            False,
            "Should return False if the unordered lines not overlap [case 1]"
        )

    def test_unordered_lines_not_overlap_case2(self):
        self.assertEqual(
            overlap((4, 8), (1, 3)),
            False,
            "Should return False if the unordered lines not overlap [case 2]"
        )

    def test_unordered_lines_common_boundary_case1(self):
        self.assertEqual(
            overlap((1, 4), (4, 8)),
            True,
            "Should return True if the unordered lines share a boundary [case1]"
        )

    def test_unordered_lines_common_boundary_case2(self):
        self.assertEqual(
            overlap((4, 8), (1, 4)),
            True,
            "Should return True if the unordered lines share a boundary [case2]"
        )

    def test_unordered_lines_contained_case1(self):
        self.assertEqual(
            overlap((1, 4), (0, 8)),
            True,
            "Should return True if the second line contain the first [case 1]"
        )

    def test_unordered_lines_contained_case2(self):
        self.assertEqual(
            overlap((0, 8), (1, 4)),
            True,
            "Should return True if the first line contain the second [case 2]"
        )

    def test_should_raise_error_if_not_number(self):
        with self.assertRaises(TypeError):
            is_number_inside_boundaries('test', (1, 2))

    def test_should_raise_error_if_not_tuple(self):
        with self.assertRaises(TypeError):
            is_number_inside_boundaries(2, 'test')


if __name__ == '__main__':
    unittest.main(verbosity=2)
