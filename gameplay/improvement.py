from __future__ import annotations

from gameplay.tile_yield import TileYield
from gameplay.effect import Effects
from gameplay.conditions import Conditions
from gameplay.exceptions.improvement_exceptions import ImprovementUpgradeException
from mixins.callbacks import CallbacksMixin
from system.entity import BaseEntity
from system.saving import SaveAble
from managers.i18n import T_TranslationOrStr, T_TranslationOrStrOrNone
from managers.tags import Taggable

from typing import Tuple, TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from data.tiles.base_tile import BaseTile


class Improvement(CallbacksMixin, SaveAble, Taggable, BaseEntity):
    # Will always finish in 1 turn.
    SINGLE_TURN = 0
    # Will finish in a fixed amount of turns.
    MULTI_TURN_FIXED = 1
    # Will finish when an certain production resource is used.
    MULTI_TURN_PRODUCTION = 2

    def __init__(
        self,
        key: str,
        name: str,
        tile: BaseTile,
        health: int = 100,
        max_health: int = 100,
        *args,
        **kwargs,
    ):
        CallbacksMixin.__init__(self, *args, **kwargs)
        Taggable.__init__(self, *args, **kwargs)
        SaveAble.__init__(self, *args, **kwargs)

        self.key: str = key
        self.active: bool = True
        self.destroyed: bool = False

        self.health: int = health
        self.max_health: int = max_health

        self.upgradable: bool = False
        self.upgrade_into: Improvement | None = None

        self.constructable_builder: bool = True
        self.constructable_on_tile: bool = True

        self.placeable_by_player: bool = False
        self.placeable_on_tiles: bool = False
        self.placeable_on_city: bool = False
        self.placeable_on_condition: Conditions | bool = False

        self.player_enabled: bool = True

        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStrOrNone = None

        self.multi_turn_mode = self.SINGLE_TURN
        self.tile: BaseTile = tile

        # Following 3 are not needed in single turn mode.
        self.production_needed = None
        self.turns_needed = None
        self.build_progress = None
        self.cost = TileYield.nullYield()

        self.tile_yield_improvement: TileYield = TileYield.nullYield()
        self.effects: Effects = Effects(name)
        self.conditions: Conditions = Conditions()

        self._model = None
        self._model_offset: Tuple[int, int, int] = (0, 0, 0)
        self._mesh = None
        self._texture = None
        self._owner = None
        self._tile_ref = None

    def _validate_state(self) -> bool:
        return True

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, value):
        self._mesh = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, data):
        self._owner = data

    @property
    def tile_ref(self):
        return self._tile_ref

    @tile_ref.setter
    def tile_ref(self, value):
        self._tile_ref = value

    @property
    def tile_yield(self) -> TileYield:
        return self._tile_yield_improvement

    @tile_yield.setter
    def tile_yield(self, value: TileYield) -> None:
        if not isinstance(value, TileYield):
            raise TypeError(f"Tileyield cannot be type {type(value)}")
        self._tile_yield_improvement = value

    def set_price_free(self):
        self.cost = TileYield.nullYield()

    def on_construct(self, callback: Callable):
        self.register_callback("on_construct", callback)

    def trigger_on_construct(self):
        self.trigger_callback("on_construct")

    def on_destroy(self, callback: Callable):
        self.register_callback("on_destory", callback)

    def trigger_on_destory(self):
        self.trigger_callback("on_destroy")

    def on_remove(self, callback: Callable):
        self.register_callback("on_remove", callback)

    def trigger_on_remove(self):
        self.trigger_callback("on_remove")

    def upgrade(self):
        if self.upgrade_into is None:
            raise ImprovementUpgradeException("Cant upgrade into a null object. needs to be an improvement effect")
        self.replace(self.upgrade_into)

    def replace(self, _with: Improvement):
        pass

    @staticmethod
    def basic_resource_improvement(
        name: str,
        tile: BaseTile,
        property: str,
        delta: float,
        mode: int = TileYield.ADDITIVE,
        health: int = 100,
    ) -> Improvement:
        ref = Improvement(key=name, name=name, tile=tile, health=health)
        _yield = TileYield(f"{name} yield")
        _yield.mode = mode
        _yield.set_prop(property, delta)
        ref.tile_yield = _yield
        return ref
