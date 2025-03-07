from __future__ import annotations
from gameplay.improvement import Improvement
from gameplay.tile_yield import TileYield
from managers.i18n import _t


class Dam(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.dam",
            _t("content.improvements.core.resource.dam.name"),
            _t("content.improvements.core.resource.dam.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="Dam", food=1.0, mode=TileYield.ADDITIVE)
