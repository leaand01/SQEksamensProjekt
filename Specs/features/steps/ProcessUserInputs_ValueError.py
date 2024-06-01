import pytest
from behave import given, when, then

from Core.Services.PrincipalCalculator import ProcessUserInputs


@given('some of the these user inputs "{house_price}", "{down_payment}", "{bond_price}", and "{bank}" are invalid')
def given_user_inputs(context, house_price, down_payment, bond_price, bank):
    context.user_inputs = {
        'house_price': house_price,  # loaded as string per default
        'down_payment': down_payment,
        'bond_price': bond_price,
        'dropdown': bank
        }
    print('context.user_inputs: ', context.user_inputs)


@when('the invalid user inputs are processed')
def assign_processor(context):
    context.processor = ProcessUserInputs()


@then('the processer fails and raises a ValueError')
def assert_processor_fails(context):
    with pytest.raises(ValueError):
        context.processor.process(context.user_inputs)
