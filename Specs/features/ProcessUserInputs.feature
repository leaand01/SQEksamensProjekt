Feature: Validate ProcessUserInput with correct inputs Feature
  If my user inputs are valid
  I want the processor to return the processed user inputs

  @ProcessUserInputs_valid_inputs
  Scenario Outline: Process valid user inputs
    Given the user inputs for the processor are "<house_price>", "<down_payment>", "<bond_price>", and "<bank>"
    When the user inputs are processed
    Then the processer runs without errors and return "<expected_output>"

    Examples:
      | house_price | down_payment | bond_price | bank | expected_output                                                                         |
      | 0           | 1            | 3          | A    | {'house_price': 0, 'down_payment': 1, 'bond_price': 0.03, 'dropdown': 'A'}              |
      | 1           | 0            | 3          | A    | {'house_price': 1, 'down_payment': 0, 'bond_price': 0.03, 'dropdown': 'A'}              |
      | 1           | 1            | 2,001      | A    | {'house_price': 1, 'down_payment': 1, 'bond_price': 0.02001, 'dropdown': 'A'}           |
      | 10.000.000  | 1            | 3          | A    | {'house_price': 10_000_000, 'down_payment': 1, 'bond_price': 0.03, 'dropdown': 'A'}     |
      | 1           | 10.000.000   | 3          | A    | {'house_price': 1, 'down_payment': 10_000_000, 'bond_price': 0.03, 'dropdown': 'A'}     |
      | 1           | 1            | 200        | A    | {'house_price': 1, 'down_payment': 1, 'bond_price': 2, 'dropdown': 'A'}                 |
      | 1.000.000   | 50.000       | 95         | A    | {'house_price': 1_000_000, 'down_payment': 50_000, 'bond_price': 0.95, 'dropdown': 'A'} |
