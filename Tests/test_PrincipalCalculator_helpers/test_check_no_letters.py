import unittest

from parameterized import parameterized

from Core.Services.PrincipalCalculator_helpers import check_no_letters


class TestCheckNoLetters(unittest.TestCase):

    @parameterized.expand([
        ['a'],
        [' a'],
        ['.a'],
        ['0a'],
        ['A'],
        [' A'],
        ['.A'],
        ['0A'],
    ])
    def test_check_no_letters_raises_error(self, input_string):
        with self.assertRaises(ValueError):
            check_no_letters(input_string)

    @parameterized.expand([
        [''],
        [' '],
        ['1'],
        ['.'],
    ])
    def test_check_no_letters_returns_none(self, input_string):
        actual_result = check_no_letters(input_string)
        self.assertIsNone(actual_result)
