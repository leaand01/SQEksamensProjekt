Feature: Validate ProcessUserInput with incorrect inputs Feature
  If my user inputs are invalid
  I want the processor to fail

  @ProcessUserInputs_invalid_inputs
  Scenario Outline: Process invalid user inputs
    Given some of the these user inputs "<house_price>", "<down_payment>", "<bond_price>", and "<bank>" are invalid
    When the invalid user inputs are processed
    Then the processer fails and raises a ValueError

    Examples:
      | house_price | down_payment | bond_price | bank |
      | 0           | -1           | 3          | A    |
      | 1           | 0            | 2          | A    |
      | -1          | 1            | 3          | A    |
      | -1          | -1           | 3          | A    |
      | 1           | -1           | 2          | A    |
      | -1          | 1            | 2          | A    |
      | -1          | -1           | 2          | A    |
      | 0           | a            | 3          | A    |
      | 1           | 0            | a          | A    |
      | a           | 1            | 3          | A    |
      | 0           | '            | 3          | A    |
      | 1           | 0            | '          | A    |
      | '           | 1            | 3          | A    |
      | 0           | ''           | 3          | A    |
      | 1           | 0            | ''         | A    |
      | ''          | 1            | 3          | A    |