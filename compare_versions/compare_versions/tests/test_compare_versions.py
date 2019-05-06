import unittest

from ..compare_versions import compare_versions


class TestCompareVersions(unittest.TestCase):
    def test_versions_same_length_first_bigger_case1(self):
        self.assertGreater(
            compare_versions('1.2.1', '1.2.0'),
            0,
            "Should return a positive number if first version is bigger than the second with same length [case 1]"
        )

    def test_versions_same_length_first_bigger_case2(self):
        self.assertGreater(
            compare_versions('1.4.  1.0', ' 1.4.0.6'),
            0,
            "Should return a positive number if first version is bigger than the second with same length [case 2]"
        )

    def test_versions_same_length_first_bigger_case3(self):
        self.assertGreater(
            compare_versions(' 5', '1  '),
            0,
            "Should return a positive number if first version is bigger than the second with same length [case 3]"
        )

    def test_versions_same_length_second_bigger_case1(self):
        self.assertLess(
            compare_versions(' 1 .2.0  ', ' 1.2 .1'),
            0,
            "Should return a negative number if first version is smaller than the second with same length [case 1]"
        )

    def test_versions_same_length_second_bigger_case2(self):
        self.assertLess(
            compare_versions('1.4.0.6  ', '  1.4.1.0'),
            0,
            "Should return a negative number if first version is smaller than the second with same length [case 2]"
        )

    def test_versions_same_length_second_bigger_case3(self):
        self.assertLess(
            compare_versions('1', '  5'),
            0,
            "Should return a negative number if first version is smaller than the second with same length [case 3]"
        )

    def test_versions_same_length_equals(self):
        self.assertEqual(
            compare_versions(' 1.2.3  ', '1.2.3'),
            0,
            "Should return zero if are equal with same length"
        )

    def test_versions_different_length_first_bigger_case1(self):
        self.assertGreater(
            compare_versions('1.2.1.0.0.0.1', '1.2.0.2.9.0.1.2.1.2.3.5'),
            0,
            "Should return a positive number if first version is bigger than the second with different length [case 1]"
        )

    def test_versions_different_length_first_bigger_case2(self):
        self.assertGreater(
            compare_versions('1.4.  1.0.0.0.0.0.0', ' 1.4.0.6'),
            0,
            "Should return a positive number if first version is bigger than the second with different length [case 2]"
        )

    def test_versions_different_length_first_bigger_case3(self):
        self.assertGreater(
            compare_versions(' 5', '1  .0.0.0. 0'),
            0,
            "Should return a positive number if first version is bigger than the second with different length [case 3]"
        )

    def test_versions_different_length_second_bigger_case1(self):
        self.assertLess(
            compare_versions(' 1 .2.0.2.2.3.5.7.1  ', ' 1.2 .1.0.0.1'),
            0,
            "Should return a negative number if first version is smaller than the second with different length [case 1]"
        )

    def test_versions_different_length_second_bigger_case2(self):
        self.assertLess(
            compare_versions('1.4.0.6.0.0  ', '  1.4.1.0.0.9.0.5'),
            0,
            "Should return a negative number if first version is smaller than the second with different length [case 2]"
        )

    def test_versions_different_length_second_bigger_case3(self):
        self.assertLess(
            compare_versions('1.0', '  5.9.8.5.2'),
            0,
            "Should return a negative number if first version is smaller than the second with different length [case 3]"
        )

    def test_versions_different_length_equals_case1(self):
        self.assertEqual(
            compare_versions(' 1.2.3  .0.0.0.0.0.0', '1.2.3'),
            0,
            "Should return zero if are equal with different length [case 1]"
        )

    def test_versions_different_length_equals_case2(self):
        self.assertEqual(
            compare_versions(' 1.2.3.0.0.1.0', '1.2.3.0.0.1.0.0.0'),
            0,
            "Should return zero if are equal with different length [case 2]"
        )

    def test_should_raise_error_if_not_string_parameter(self):
        with self.assertRaises(AttributeError):
            compare_versions('1', 2.5)

    def test_should_raise_error_if_unexpected_character(self):
        with self.assertRaises(ValueError):
            compare_versions('1.2.c', '1.b.1.a')


if __name__ == '__main__':
    unittest.main(verbosity=2)
