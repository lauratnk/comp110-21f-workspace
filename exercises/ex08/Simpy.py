"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730318786"


class Simpy:
    """EX08 Thing!"""
    values: list[float]

    def __init__(self, ls1: list[float]):
        """Part 0."""
        self.values = ls1

    def __str__(self) -> str:
        """Part 1."""
        return f"Simpy({self.values})"

    def fill(self, fl: float, int: int) -> None:
        """Part 2."""
        self.values = []
        i = 0
        while i < int:
            self.values.append(fl)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Part 3."""
        assert step != 0.0
        ls1 = [start]
    
        i = 1
        while i < ((stop - start) / step):
            ls1.append(ls1[i - 1] + step)
            i += 1
        self.values = ls1

    def sum(self) -> float:
        """Part 4."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Part 5."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1

        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Part 6."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1

        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Part 7."""
        result: list[bool] = []
        
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Part 8."""
        result: list[bool] = []
        
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Part 9."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            i = 0
            while i < len(rhs):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result
