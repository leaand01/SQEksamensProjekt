from abc import ABC, abstractmethod
from typing import Any


class IRepository(ABC):
    """Generic interface for accessing data."""

    @abstractmethod
    def get_all(self) -> Any:
        """Return all data."""

    @abstractmethod
    def get(self, name: str) -> Any:
        """Return name's data."""
