from abc import ABC, abstractmethod
from typing import Any, Union


class ICalculator(ABC):
    """Generic interface for calculator method."""

    @abstractmethod
    def calculate(self, data: Any) -> Union[int, float]:
        """Calculate something."""
