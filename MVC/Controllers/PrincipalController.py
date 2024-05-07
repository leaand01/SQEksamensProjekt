from functools import partial
from Core.Services.BankFeeRepository import LocalDB, Banks
from Core.Services.PrincipalCalculator import Principal, ProcessUserInputs
from Infrastructure.DbInitializer import dict_banks


local_db = LocalDB(dict_banks)
banks = Banks(local_db)

principal = Principal(banks=banks, processor=ProcessUserInputs())
# principal = partial(Principal, banks=banks, processor=ProcessUserInputs())
# principal_partial = partial(Principal, banks=banks, processor=ProcessUserInputs())
# process_user_inputs = ProcessUserInputs()
# principal_partial = partial(Principal, banks=banks)

#
# user_inputs = {'house_price': '1.000.000', 'down_payment': '50.000', 'bond_price': '95,558', 'dropdown': 'Totalkredit'}
# principal.calculate(user_inputs)
#
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
# value = locale.atof(value)
