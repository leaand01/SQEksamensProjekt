import ast

from behave import given, when, then

from Core.Services.PrincipalCalculator import ProcessUserInputs


@given('the user inputs for the processor are "{house_price}", "{down_payment}", "{bond_price}", and "{bank}"')
def given_user_inputs(context, house_price, down_payment, bond_price, bank):
    context.user_inputs = {
        'house_price': house_price,  # loaded as string per default
        'down_payment': down_payment,
        'bond_price': bond_price,
        'dropdown': bank
    }


@when('the user inputs are processed')
def process_user_inputs(context):
    processor = ProcessUserInputs()
    context.actual_processed_user_inputs = processor.process(context.user_inputs)


@then('the processer runs without errors and return "{expected_output}"')
def assert_processed_user_inputs(context, expected_output):
    expected_processed_user_inputs = ast.literal_eval(expected_output)
    assert context.actual_processed_user_inputs == expected_processed_user_inputs
