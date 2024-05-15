from dataclasses import dataclass


@dataclass
class BankFees:
    name: str
    fees: float
    bond_fee: float

# Remark: According to .net MVC setup this corresponds to a Model/DTO.
