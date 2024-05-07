from unittest.mock import MagicMock

from behave import given, when, then

from Core.Services.PrincipalCalculator import Principal


@given('the user inputs are "{house_price}", "{down_payment}", "{bond_price}", and "{bank}"')
def given_user_inputs(context, house_price, down_payment, bond_price, bank):
    context.user_inputs = {
        'house_price': int(house_price),
        'down_payment': int(down_payment),
        'bond_price': float(bond_price),
        'dropdown': bank
    }


@given('bank_fees equals "{bank_fees}" and bank_bond_fee equals "{bank_bond_fee}"')
def mock_bank_object(context, bank_fees, bank_bond_fee):
    context.mock_bank_object = MagicMock()
    context.mock_bank_object.fees = int(bank_fees)
    context.mock_bank_object.bond_fee = float(bank_bond_fee)


@when('the user press the beregn button')
def calculate_mocked_principal(context):
    mock_bank_repository = MagicMock()
    mock_bank_repository.get.return_value = context.mock_bank_object

    mock_processor = MagicMock()
    mock_processor.process.return_value = context.user_inputs

    mock_principal = Principal(mock_bank_repository, mock_processor)
    context.actual_principal = mock_principal.calculate(context.user_inputs)


@then('the principal amount is calculated and equals "{expected_principal}"')
def assert_principal_calculation(context, expected_principal):
    assert context.actual_principal == int(expected_principal)
