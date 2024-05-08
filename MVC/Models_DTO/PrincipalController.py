from Core.Services.BankFeeRepository import LocalDB, Banks
from Core.Services.PrincipalCalculator import Principal, ProcessUserInputs
from Infrastructure.DbInitializer import dict_banks


local_db = LocalDB(dict_banks)
banks = Banks(local_db)

principal = Principal(banks=banks, processor=ProcessUserInputs())


# For debugging:
# user_inputs = {'house_price': '1.000.000', 'down_payment': '50.000', 'bond_price': '200', 'dropdown': 'Totalkredit'}
# principal.calculate(user_inputs)
