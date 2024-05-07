from dataclasses import dataclass
from typing import Any

from Core.Entities.BankFees import BankFees
from Core.Interfaces.IDB import IDB
from Core.Interfaces.IRepository import IRepository


@dataclass
class LocalDB(IDB):
    """Access locally defined database."""
    local_db: dict[BankFees]
    # local_db: dict[dict]

    def query(self) -> dict[BankFees]:
    # def query(self) -> dict[dict]:
        return self.local_db


@dataclass
class Banks(IRepository):
    """Object for accessing bank details."""
    db: IDB  # TODO: er det overflødigt at lave LocalDB og DB da Banks allerede er en konkret subclass af IRepository?
             ## virker som dobbelt arbejde for at undgå direkte afhængighed

    def get_all(self) -> Any:  # TODO: depending on interface instead of database (dependency inversion or dependency injection?)
    # def get_all(self) -> IDB:  # TODO: depending on interface instead of database (dependency inversion or dependency injection?)
        return self.db.query()

    def get(self, name: str) -> Any:
    # def get(self, name: str) -> BankFees:
    # def get(self, name: str) -> dict:
        return self.db.query()[name]
