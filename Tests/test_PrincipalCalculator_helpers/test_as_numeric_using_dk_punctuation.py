import unittest

from parameterized import parameterized

from Core.Services.PrincipalCalculator_helpers import as_numeric_using_dk_punctuation


class TestAsNumericUsingDkPunctuation(unittest.TestCase):

    @parameterized.expand([
        ['1,000,1'],
        ['1,000,000.1'],
        ['1,000,000'],
        ['1,000.000,1'],
    ])
    def test_as_numeric_using_dk_punctuation_raises_error(self, input_string):
        with self.assertRaises(ValueError):
            as_numeric_using_dk_punctuation(input_string)

    @parameterized.expand([
        ['1,0.1', 1.01],
        ['0.1', 1],
        ['.01', 1],
        ['.1', 1],
        ['1.1', 11],
        ['1.11', 111],
        ['1.111', 1_111],
        ['1.000', 1_000],
        ['1.000,0', 1_000.0],
        ['1,000.1', 1.0001],
        ['1.000.000', 1_000_000],
        ['1.000.000,0', 1_000_000.0],
        ['1.000.000,1', 1_000_000.1],
        ['1,000.000.1', 1.000_000_1],
        ['1.000,000.1', 1_000.0001],
    ])
    def test_as_numeric_using_dk_punctuation_ignores_dot_separators(self, input_string, expected_result):
        actual_result = as_numeric_using_dk_punctuation(input_string)
        self.assertEqual(expected_result, actual_result)
