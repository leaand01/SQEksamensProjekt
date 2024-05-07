import unittest
from unittest.mock import MagicMock

from Core.Services.PrincipalCalculator import Principal


class TestPrincipalCalculator(unittest.TestCase):

    def setUp(self):
        """Setup test fixtures."""
        self.mock_bank_repository = MagicMock()
        self.mock_bank_object = MagicMock()
        self.mock_bank_object.fees = 0
        self.mock_bank_object.bond_fee = 0
        self.mock_bank_repository.get.return_value = self.mock_bank_object

        self.mock_processor = MagicMock()
        self.mock_user_inputs = {'house_price': '100', 'down_payment': '0', 'bond_price': '100', 'dropdown': 'FakeBank'}

        self.mock_processor.process.return_value = {'house_price': 100, 'down_payment': 0, 'bond_price': 1, 'dropdown': 'FakeBank'}
        # self.mock_processor.transform_data_to_view_format.return_value = 'irrelevant_for_testing_calculated_values'
        # self.mock_processor.transform_value_to_view_format.return_value = 'irrelevant_for_testing_calculated_values'

        self.mock_principal_calculator = Principal(self.mock_bank_repository, self.mock_processor)

    def test_principal_calculation_equals_100(self):
        expected_value = 100
        actual_value = self.mock_principal_calculator.calculate(self.mock_user_inputs)
        self.assertEqual(expected_value, actual_value)
