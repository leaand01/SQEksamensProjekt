import locale
from dataclasses import dataclass, field
from itertools import accumulate
from typing import Dict, Union

from Core.Interfaces.ICalculator import ICalculator
from Core.Interfaces.IProcessor import IProcessor
from Core.Interfaces.IRepository import IRepository

import string


def convert_str_to_numeric(value: str) -> float:  # maybe do BDD on this
    check_not_empty(value)
    check_no_invalid_punctuations(value)
    check_no_letters(value)
    # value = as_float(value)
    # value = as_numeric(value)
    value = as_numeric_using_dk_punctuation(value)
    return value


def check_not_empty(value: str) -> None:
    if not value.replace(' ', ''):
        raise ValueError('Empty input!')


def check_no_invalid_punctuations(value: str) -> None:
    invalid_punctuations = string.punctuation.replace(',', '').replace('.', '')
    if any([x in invalid_punctuations for x in value]):
        raise ValueError('Invalid input!')


def check_no_letters(value: str) -> None:
    letters = string.ascii_lowercase
    if any([x in letters for x in value.lower()]):
        raise ValueError('The input must only contain digits!')


def as_float(value: str) -> float:  # TODO: not handled if user inputs numbers with 1000 seperators
    """Convert string to float. String can only contain decimal seperator otherwise exception is raised."""
    max_one_dot_or_comma(value)
    value = float(value.replace(',', '.'))
    return value


# def as_numeric(value: str) -> Union[float, int]:  # TODO: not handled if user inputs numbers with 1000 seperators
#     """Convert string to float. String can only contain decimal seperator otherwise exception is raised."""
#     max_one_dot_or_comma(value)
#     value = value.replace(',', '.')
#     return float(value) if '.' in value else int(value)

def as_numeric_using_dk_punctuation(value: str) -> Union[float, int]:  # TODO: not handled if user inputs numbers with 1000 seperators
    """Convert string to float. String must only contain danish punctuations if any."""
    # max_one_dot_or_comma(value)
    try:
        locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
        return locale.atof(value)
    except ValueError:
        raise ValueError('Incorrect number: Danish punctuation uses "," for decimal and "." for 1000 seperator.')


def max_one_dot_or_comma(value: str) -> None:
    id_puncs = [x in ',.' for x in value]
    if id_puncs.count(True) > 1:
        raise ValueError('Input can max contain 1 comma or dot for decimal seperator!')



def check_not_negative(value: float) -> None:
    if isinstance(value, float) and value < 0:
        raise ValueError('Inputted number must be >= 0!')


# def check_is_positive(value: float) -> None:
#     if value <= 0:
#         raise ValueError('Bond price must be > 0!')  # TODO: Bond price skal være større end 2% ellers div med 0 eller neg

def check_is_greather_than_two(value: float) -> None:
    if value <= 2:
        raise ValueError('Bond price must be greather than 2, due to bank bond fees.!')  # TODO: Bond price skal være større end 2% ellers div med 0 eller neg

def convert_to_percentage(value: float) -> float:
    if value >= 1:
        return value / 100


def convert_back_to_input_percentage(value: Union[float, int]) -> Union[float, int]:
    return value * 100


def convert_back_to_input_percentage_string(value: Union[float, int]) -> str:
    n_dec = min(n_decimals(value) - 2, 3)
    return '{:.{}%}'.format(value, n_dec).replace('.', ',').replace('%', '')
    # if n_dec > 0:
    #     return '{:.3%}'.format(value).replace('.', ',').replace('%', '')
    # else:
    #     return '{:.3%}'.format(value).replace('.', ',').replace('%', '')


def n_decimals(value: Union[int, float]) -> int:
    try:
        n_decimals = len(str(value).split('.')[1])
    except IndexError:
        n_decimals = 0
    return n_decimals


# def is_decimal(value: Union[float, int]) -> bool:
#     return value % 1 > 0

def convert_numeric_to_string_dk_punctuation(value: Union[float, int]) -> str:
# def convert_numeric_to_string_dk_punctuation(value: Union[float, int], n_decimals: int = 0) -> str:
#     return f'{value:,}'
    return '{:,}'.format(value).replace(',', '.')
    # return '{:,}'.format(value).replace(',', '_').replace('.', ',').replace('_', '.')



#
# import locale
# value = 1000000.5
# value = 1000000
# f'{value:,}'
# locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
# locale.format_string(f"%.2f", value)
# print('{:n}'.format(value))
# f'{value:n}'
#
# '{:,}'.format(value)
# '{:.2%}'.format(0.955).replace('.', ',').replace('%', '') # percentage

    # return locale.format_string(f"%.{n_decimals}f", value)


# def transform_to_view_format(data: Dict[str, Union[str, float, int]]) -> Dict[str, Union[str, str]]:
#     view_data = data.copy()
#
#     key_value_pairs = view_data.items()
#     for key, value in key_value_pairs:
#         if key == 'dropdown':
#             continue
#
#         if key == 'bond_price':
#             view_data[key] = convert_back_to_input_percentage(value)
#             view_data[key] = convert_numeric_to_string_dk_punctuation(value, 2)
#             continue
#
#         view_data[key] = convert_numeric_to_string_dk_punctuation(value)
#
#     return view_data



@dataclass
class ProcessUserInputs(IProcessor):

    def process(self, data: Dict[str, Union[str, float]]) -> Dict[str, Union[str, float]]:
        """Convert dict values of types int and float to numerics."""
        processed_data = data.copy()
        key_value_pairs = processed_data.items()
        for key, value in key_value_pairs:
            if key == 'dropdown':
                continue

            value = convert_str_to_numeric(value)
            check_not_negative(value)

            if key in ['house_price', 'down_payment']:
                value = round(value)

            if key == 'bond_price':
                # check_is_positive(value)
                check_is_greather_than_two(value)
                value = convert_to_percentage(value)

            processed_data[key] = value

        # self.data = processed_data
        return processed_data

    def transform_data_to_view_format(self, data: Dict[str, Union[str, float, int]]) -> Dict[str, Union[str, str]]:
        view_data = data.copy()

        key_value_pairs = view_data.items()
        for key, value in key_value_pairs:
            if key == 'dropdown':
                continue

            if key == 'bond_price':
                view_data[key] = convert_back_to_input_percentage_string(value)
                continue
                # value = convert_back_to_input_percentage(value)
                # value = convert_back_to_input_percentage(value)
                # view_data[key] = convert_numeric_to_string_dk_punctuation(value)
                # continue

            view_data[key] = convert_numeric_to_string_dk_punctuation(value)
            # view_data[key] = convert_numeric_to_string_dk_punctuation(int(round(value)))

        return view_data

    def transform_value_to_view_format(self, value: Union[float, int]) -> str:
        # return convert_numeric_to_string_dk_punctuation(value)
        return convert_numeric_to_string_dk_punctuation(int(round(value)))


@dataclass
class Principal(ICalculator):
    """Calculater for calculating principal and capital loss."""
    banks: IRepository
    processor: IProcessor

    # defined when calling calculate
    user_inputs: Dict[str, Union[str, float]] = field(init=False, default_factory=dict)
    principal: int = field(init=False, default=None)
    capital_loss: int = field(init=False, default=None)

    def calculate(self, user_inputs: Dict[str, Union[str, float]]) -> str:
    # def calculate(self, processor: ProcessUserInputs):

        self.user_inputs = self.processor.process(user_inputs)
        # self.user_inputs = processor.process(self.user_inputs)

        bank_name = self.user_inputs['dropdown']
        bank_details = self.banks.get(bank_name)

        loan_amount = self.user_inputs['house_price'] + bank_details.fees - self.user_inputs['down_payment']
        net_bond_price = self.user_inputs['bond_price'] - bank_details.bond_fee
        principal = loan_amount / net_bond_price
        capital_loss = principal - loan_amount

        self.user_inputs = self.processor.transform_data_to_view_format(self.user_inputs)
        self.principal = self.processor.transform_value_to_view_format(principal)
        self.capital_loss = self.processor.transform_value_to_view_format(capital_loss)
        # self.principal = "{:,}".format(round(principal))
        # self.capital_loss = "{:,}".format(round(capital_loss))

        # self.user_inputs['bond_price'] *= 100

    # self.capital_loss = round(principal - loan_amount)
        # self.principal = round(principal)

        return self.principal






############################
#
# @dataclass
# class ProcessUserInputs(IProcessor):
#     _digits: str = field(init=False, default_factory=lambda: '0123456789')
#     _letters: str = field(init=False, default_factory=lambda: string.ascii_letters + 'æøå')
#
#     def process(self, data: Dict[str, Union[str, float]]):
#     # def process(self, user_inputs: Dict[str, Union[str, float]]):
#         self.user_inputs = data.copy()
#
#         self._convert_numeric_inputs_to_floats()
#         self._validate_bond_price_is_positive()
#         self._validate_bond_price_is_percentage()
#
#         return self.user_inputs
#
#     def _convert_numeric_inputs_to_floats(self):   # maybe do BDD on this
#         key_value_pairs = self.user_inputs.items()
#         for key, value in key_value_pairs:
#             self._is_empty_string(value)
#             # self._contains_successive_punctuations(value)
#             self._contains_invalid_punctuations(value)
#             self._contains_letters_and_numerics(value)
#             if not self._is_text(value):
#                 self._as_float(key, value)
#                 self._validate_not_negative(value)
#
#     def _is_empty_string(self, value):
#         if not value.replace(' ', ''):
#             raise ValueError('Empty input!')
#
#     def _contains_invalid_punctuations(self, value):
#         invalid_punctuations = string.punctuation.replace(',', '').replace('.', '')
#         if any([x in invalid_punctuations for x in value]):
#             raise ValueError('Invalid input!')
#
#     def _contains_letters_and_numerics(self, value):
#         if any([x in self._digits for x in value]) & any([x in self._letters for x in value.lower()]):
#             raise ValueError('The input must only contain digits!')
#
#     def _is_text(self, value):
#         return all([x in self._letters for x in value.lower()])
#
#     def _as_float(self, key, value: str):  # TODO: not handled if user inputs numbers with 1000 seperators
#         """Convert string to float. String can only contain decimal seperator otherwise exception is raised."""
#         self._max_one_dot_or_comma(value)
#         value = float(value.replace(',', '.'))
#
#         self.user_inputs[key] = value
#         return value
#
#     def _max_one_dot_or_comma(self, value):
#         id_puncs = [x in ',.' for x in value]
#         if id_puncs.count(True) > 1:
#             raise ValueError('Input can max contain 1 comma or dot for decimal seperator!')
#
#     # def _as_float(self, key, value: str):  # TODO: not handled if user inputs numbers with 1000 seperators
#     #     self._contains_successive_punctuations(value)
#     #     first_punc = self._first_punctuation(value)
#     #     if first_punc == '.':
#     #         locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
#     #         value = locale.atof(value)
#     #
#     #     elif first_punc == ',':
#     #         locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#     #         value = locale.atof(value)
#     #
#     #     else:
#     #         raise NotImplementedError('Case not accounted for!')
#     #
#     #     # try:
#     #     #     value = float(value.replace(',', '.'))
#     #     # except ValueError:
#     #     #     try:
#     #     #         locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')
#     #     #         value = locale.atof(value)
#     #     #     except ValueError:
#     #     #         try:
#     #     #             locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#     #     #             value = locale.atof(value)
#     #     #         except ValueError:
#     #     #             raise ValueError('The input cannot be converted to a numeric!')
#     #
#     #     self.user_inputs[key] = value
#     #     return value
#     #
#     # def _contains_successive_punctuations(self, value):
#     #     binary_id_of_puncs = [int(x in ',.') for x in value]
#     #     for i, _ in enumerate(binary_id_of_puncs[:-1]):
#     #         if binary_id_of_puncs[i] + binary_id_of_puncs[i + 1] == 2:
#     #             raise ValueError('Successive comma or dot punctuations.')
#     #
#     # def _first_punctuation(self, value):
#     #     id_of_puncs = [x in ',.' for x in value]
#     #     if any(id_of_puncs):
#     #         index_of_first_punc = id_of_puncs.index(True)
#     #         return value[index_of_first_punc]
#     #     else:
#     #         return '.'
#
#     def _validate_not_negative(self, value):
#         if isinstance(value, float) and value < 0:
#             raise ValueError('Inputted number must be >= 0!')
#
#     def _validate_bond_price_is_positive(self, key='bond_price'):
#         if self.user_inputs[key] <= 0:
#             raise ValueError('Bond price must be >= 0!')
#
#     def _validate_bond_price_is_percentage(self, key='bond_price'):
#         if self.user_inputs[key] >= 1:
#             self.user_inputs[key] /= 100
#
#
# @dataclass
# class Principal(ICalculator):
#     """Calculater for calculating principal and capital loss."""
#     banks: IRepository
#     user_inputs: dict
#
#     # def __post_init__(self):
#     #     self._user_inputs = self.user_inputs.copy()
#     #     self.calculate()
#
#     def calculate(self, processor: ProcessUserInputs):
#         self._user_inputs = processor.process(self.user_inputs)
#
#         bank_name = self._user_inputs['dropdown']
#         bank_details = self.banks.get(bank_name)
#
#         loan_amount = self._user_inputs['house_price'] + bank_details.fees - self._user_inputs['down_payment']
#         net_bond_price = self._user_inputs['bond_price'] - bank_details.bond_fee
#         principal = loan_amount / net_bond_price
#
#         self.capital_loss = round(principal - loan_amount)
#         self.principal = round(principal)
#
#         return self.principal
#
#
#
#
# # @dataclass
# # class Principal(ICalculator):
# #     """Calculater for calculating principal and capital loss."""
# #     banks: IRepository
# #     user_inputs: dict
# #
# #     def __post_init__(self):
# #         self._user_inputs = self.user_inputs.copy()
# #         self._user_inputs_to_floats()
# #         self._validate_bond_price_is_percentage()
# #         self.calculate()
# #
# #     def calculate(self):
# #         bank_name = self._user_inputs['dropdown']
# #         bank_details = self.banks.get(bank_name)
# #
# #         loan_amount = self._user_inputs['house_price'] + bank_details.fees - self._user_inputs['down_payment']
# #         net_bond_price = self._user_inputs['bond_price'] - bank_details.bond_fee
# #         principal = loan_amount / net_bond_price
# #
# #         self.capital_loss = round(principal - loan_amount)
# #         self.principal = round(principal)
# #
# #         return self.principal
# #
# #     # def _user_inputs_to_floats(self):
# #     #     self._as_float('house_price')
# #     #     self._as_float('bond_price')
# #     #     self._as_float('down_payment')
# #     def _user_inputs_to_floats(self, list_keys: List[str]):
# #         for key in list_keys:
# #             self._as_float(key)
# #
# #     def _as_float(self, key: str):
# #         value = self._user_inputs[key].replace(',', '.')
# #         try:
# #             value = float(value)
# #         except ValueError:
# #             raise ValueError('Input must be a number!')
# #
# #         self._validate_not_negative(value)
# #         self._user_inputs[key] = value
# #
# #     def _validate_not_negative(self, value):
# #         if value < 0:
# #             raise ValueError('Inputted number must be >= 0!')
# #
# #     def _validate_bond_price_is_percentage(self, key='bond_price'):
# #         if self._user_inputs[key] <= 0:
# #             raise ValueError('Bond price must be >= 0!')
# #
# #         if self._user_inputs[key] >= 100:
# #             self._user_inputs[key] /= 100
# #
#
#
#
