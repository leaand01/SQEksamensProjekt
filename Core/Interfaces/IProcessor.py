from abc import ABC, abstractmethod
from typing import Any


class IProcessor(ABC):
    """Generic interface for processing some input"""

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Do some processing"""
