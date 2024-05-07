from abc import ABC, abstractmethod
from typing import Any


class IDB(ABC):
    """Generic interface for calling some database."""

    @abstractmethod
    def query(self) -> Any:
        """Returns all data from database."""
