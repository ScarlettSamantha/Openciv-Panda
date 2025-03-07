from __future__ import annotations
from gameplay.tile_yield import TileYield
from copy import deepcopy

from typing import Dict, List, Type, Self


class TileYieldModifier:
    MODE_ADDITIVE = 0
    MODE_PERCENTAGE = 1
    MODE_SET = 2
    MODE_BASE = 3

    def __init__(self, values: TileYield | List[TileYield] | None = None, mode: int = MODE_ADDITIVE) -> None:
        self.mode = mode

        self.base: TileYield = TileYield.nullYield()

        self._calulated_cache: TileYield | None = None

        self._addative: Dict[int, TileYield] = {}
        self._percentage_cummulative: Dict[int, TileYield] = {}
        self._percentage_addative: Dict[int, TileYield] = {}

        self._raw_recoverable_yields: Dict[int, List[TileYield]] = {}

        self._internal_list: List[TileYield] = []
        # If enabled it will not be able to try to recover tile yield corruption or recovery states due to reconstruction being random at that point.
        self.disable_recoverable_storage: bool = False

        if values is not None and isinstance(values, TileYield):
            self.add(values)
        elif values is not None and isinstance(values, List):
            for item in values:
                self.add(item)
        elif values is not None and isinstance(values, Dict):
            self.add(values)

    def add_addative(self, value: TileYield) -> None:
        self._addative[len(self._addative)] = value

    def add_percentage_cumulative(self, value: TileYield) -> None:
        self._percentage_cummulative[len(self._percentage_cummulative)] = value

    def add_percentage_addative(self, value: TileYield) -> None:
        self._percentage_addative[len(self._percentage_addative)] = value

    def get_addative(self) -> Dict[int, TileYield]:
        return self._addative

    def get_percentage_cummulative(self) -> Dict[int, TileYield]:
        return self._percentage_cummulative

    def get_percentage_addative(self) -> Dict[int, TileYield]:
        return self._percentage_addative

    def calculate(self, cache: bool = False) -> TileYield:
        # Hope for cache hit.
        if cache and self._calulated_cache is not None:
            return deepcopy(self._calulated_cache)
        # We need to decouple the base from this value otherwise its a ref so it will change the original and we wont be able to recalculate.
        # That is also the reason this function returns a calulated version of everything instead of us change our selfs.
        current: TileYield = deepcopy(self.base)
        percentage: TileYield = TileYield.nullYield()
        for _, _yield in self.get_addative().items():
            result = current + _yield
            current = result
        i = False
        for _, _yield in self.get_percentage_addative().items():
            i = True
            percentage = percentage + _yield

        if i:
            current = current * percentage
        for _, _yield in self.get_percentage_cummulative().items():
            current = current * _yield
        if cache:
            self._calulated_cache = deepcopy(current)

        return current

    def __repr__(self):
        return str(self.calculate())

    def get_yield(self, from_cache: bool = True) -> TileYield:
        if from_cache and self._calulated_cache is not None:
            return self._calulated_cache
        return self.calculate()

    def get(self) -> Dict:
        return self.__dict__

    def props(self) -> TileYield:
        return self.calculate()

    def add(
        self,
        obj_ref: TileYield | Type["TileYieldModifier"] | List[TileYield] | Dict[str, TileYield] | TileYieldModifier,
    ) -> Self:
        def _add(self: Self, obj: TileYield) -> None:
            if not self.disable_recoverable_storage:
                self._raw_recoverable_yields[len(self._raw_recoverable_yields)] = [obj]
            if obj.mode == TileYield.ADDITIVE:
                self.add_addative(obj)
            elif obj.mode == TileYield.PERCENTAGE_ADDATIVE:
                self.add_percentage_addative(obj)
            elif obj.mode == TileYield.PERCENTAGE_CUMMULATIVE:
                self.add_percentage_cumulative(obj)

        if isinstance(obj_ref, List):
            for item in obj_ref:
                if isinstance(item, TileYield):
                    _add(self=self, obj=item)
        elif isinstance(obj_ref, Dict):
            for _, item in obj_ref.items():
                if isinstance(item, TileYield):
                    _add(self=self, obj=item)
        elif isinstance(obj_ref, TileYield):
            _add(self=self, obj=obj_ref)
        elif isinstance(obj_ref, TileYieldModifier):
            for _, item in obj_ref.get_addative().items():
                self.add_addative(item)
            for _, item in obj_ref.get_percentage_cummulative().items():
                self.add_percentage_cumulative(item)
            for _, item in obj_ref.get_percentage_addative().items():
                self.add_percentage_addative(item)
        return self

    def __add__(
        self,
        a: Type["TileYieldModifier"] | List[TileYield] | Dict[str, TileYield] | TileYieldModifier,
    ) -> Self:
        self.add(a)
        return self

    def __str__(self) -> str:
        if self._calulated_cache is not None:
            return str(self._calulated_cache)
        return str(self.calculate())
