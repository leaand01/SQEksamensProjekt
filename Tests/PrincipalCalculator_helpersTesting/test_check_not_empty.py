import unittest

from parameterized import parameterized

from Core.Services.PrincipalCalculator_helpers import check_not_empty


class TestCheckNotEmpty(unittest.TestCase):

    @parameterized.expand([
        [''],
        [' '],
    ])
    def test_check_not_empty_raises_error_if_empty_string(self, input_string):
        with self.assertRaises(ValueError):
            check_not_empty(input_string)

    @parameterized.expand([
        ['.'],
        ['1'],
        ['a'],
    ])
    def test_check_not_empty_return_null_if_nonempty_string(self, input_string):
        actual_result = check_not_empty(input_string)
        self.assertIsNone(actual_result)
