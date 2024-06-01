Feature: Principal Calculation Feature
  As a user
  I want to be able to calculate the principal value
  based on my inputs when pressing the Beregn-button

  @mock_principal
  Scenario Outline: Calculate principal amount
    Given the user inputs are "<house_price>", "<down_payment>", "<bond_price>", and "<bank>"
    And bank_fees equals "<bank_fees>" and bank_bond_fee equals "<bank_bond_fee>"
    When the user press the beregn button
    Then the principal amount is calculated and equals "<expected_principal>"

    Examples:
      | house_price | down_payment | bond_price | bank | bank_fees | bank_bond_fee | expected_principal |
      | 0           | 0            | 1          | A    | 0         | 0             | 0                  |
      | 0           | 0            | 1          | A    | 100       | 0             | 100                |
      | 0           | 0            | 0.5        | A    | 100       | 0             | 200                |
      | 0           | 0            | 1          | A    | 100       | 0.5           | 200                |
      | 100         | 0            | 0.25       | A    | 0         | 0             | 400                |
      | 100         | 0            | 0.25       | A    | 100       | 0             | 800                |
      | 100         | 0            | 0.25       | A    | 100       | 0.05          | 1000               |
      | 100         | 50           | 0.25       | A    | 0         | 0             | 200                |
      | 100         | 50           | 0.25       | A    | 100       | 0             | 600                |
      | 100         | 50           | 0.25       | A    | 100       | 0.05          | 750                |
      | 0           | 0            | 1.02       | A    | 20_000    | 0.02          | 20_000             |
      | 200         | 100          | 1.02       | A    | 18_000    | 0.02          | 18_100             |
