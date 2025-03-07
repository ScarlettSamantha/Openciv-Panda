from __future__ import annotations
from gameplay.improvement import Improvement
from gameplay.tile_yield import TileYield
from managers.i18n import _t


class Mine(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.mine",
            _t("content.improvements.core.mine.name"),
            _t("content.improvements.core.mine.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="Basic Mine", production=1.0, mode=TileYield.ADDITIVE)
