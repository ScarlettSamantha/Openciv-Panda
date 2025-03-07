from __future__ import annotations
from typing import List
from typing import TypeVar

_T = TypeVar("_T")


class TileModifier:
    MODIFIER_MODE_SET = 0
    MODIFIER_MODE_PERCENTAGE_OFFSET = 1

    def __init__(self, property: str, value, mode: int = MODIFIER_MODE_SET):
        self._property = property
        self._value = value
        self._mode = mode


class TileModifiers:
    def __init__(self):
        self._modifiers: List[TileModifier] = []

    @property
    def modifiers(self) -> List[TileModifier]:
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers: List[TileModifier]) -> None:
        self._modifiers = modifiers

    def add_modifier(self, modifier: TileModifier) -> None:
        self._modifiers.append(modifier)

    def add_modifiers(self, items: List[TileModifier]) -> None:
        for item in items:
            self.add_modifier(item)

    def __getitem__(self, __key) -> _T:
        return self._modifiers.__getitem__(__key)

    def __setitem__(self, __key: int, __value: TileModifier):
        self._modifiers.__setitem__(__key, __value)

    def append(self, item):
        self._modifiers.append(item)

    def get(self, __key: type[_T]) -> _T | None:
        for item in self._modifiers:
            if isinstance(item, __key):
                return item
        return None

    def get_modifiers(self) -> List[TileModifier]:
        return self._modifiers

    def __iter__(self):
        return iter(self._modifiers)
