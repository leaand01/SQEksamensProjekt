from Core.Services.BankFeeRepository import LocalDB, Banks
from Core.Services.PrincipalCalculator import Principal, ProcessUserInputs
from Infrastructure.DbInitializer import dict_banks


local_db = LocalDB(dict_banks)
banks = Banks(local_db)

principal = Principal(banks=banks, processor=ProcessUserInputs())
