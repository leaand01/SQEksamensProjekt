import unittest

from parameterized import parameterized

from Core.Services.PrincipalCalculator_helpers import check_no_invalid_punctuations


class TestCheckNoInvalidPunctuations(unittest.TestCase):

    @parameterized.expand([
        ['!'],
        ['"'],
        ['#'],
        ['$'],
        ['%'],
        ['&'],
        ['\''],
        ['('],
        [')'],
        ['*'],
        ['+'],
        ['-'],
        ['/'],
        [':'],
        [';'],
        ['<'],
        ['='],
        ['>'],
        ['?'],
        ['@'],
        ['['],
        ['\\'],
        [']'],
        ['^'],
        ['_'],
        ['`'],
        ['{'],
        ['|'],
        ['}'],
        ['~'],
    ])
    def test_check_no_invalid_punctuations_raises_error(self, input_string):
        with self.assertRaises(ValueError):
            check_no_invalid_punctuations(input_string)

    @parameterized.expand([
        [''],
        [' '],
        ['.'],
        [','],
        ['a'],
        ['1'],
    ])
    def test_check_no_invalid_punctuations_return_none(self, input_string):
        actual_result = check_no_invalid_punctuations(input_string)
        self.assertIsNone(actual_result)
