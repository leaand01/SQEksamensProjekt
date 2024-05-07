#Feature: Principal Calculation Feature
#
#  @mock_principal
#  Scenario Outline: Calculate principal amount
#    Given the user inputs are "<house_price>", "<down_payment>", "<bond_price>", and "<bank>"
#    And bank_fees equals "<bank_fees>" and bank_bond_fee equals "<bank_bond_fee>"
#    When the user press the beregn button
#    Then the principal amount is calculated and equals "<expected_principal>"
#
#    Examples:
#      | house_price | down_payment | bond_price | bank | bank_fees | bank_bond_fee | expected_principal |
#      | 0           | 0            | 1          | A    | 0         | 0             | 0                  |
#      | 0           | 0            | 1          | A    | 100       | 0             | 100                |
#      | 0           | 0            | 0.5        | A    | 100       | 0             | 200                |
#      | 0           | 0            | 0.021      | A    | 0         | 0             | 0                  |
#      | 100         | 50           | 1          | A    | 0         | 0             | 50                 |
#      | 100         | 50           | 0.25       | A    | 0         | 0             | 200                |
#      | 100         | 0            | 1          | A    | 20_000    | 0             | 20_100             |
#      | 100         | 0            | 0.5        | A    | 0         | 0             | 200                |
#      | 100         | 50           | 2          | A    | 100       | 0             | 75                 |
#      | 100         | 0            | 1.02       | A    | 20_000    | 0.02          | 20_100             |
#      | 100         | 0            | 1.02       | A    | 18_000    | 0.02          | 18_100             |
