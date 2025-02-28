from typing import Dict, Tuple
from data.terrain._base_terrain import BaseTerrain
from gameplay.resources.core.basic._base import BasicBaseResource
from managers.i18n import T_TranslationOrStr, _t


class Housing(BasicBaseResource):
    key: str = "resource.core.basic.housing"
    name: T_TranslationOrStr = _t("content.resources.core.housing.name")
    description: T_TranslationOrStr = _t("content.resources.core.housing.description")
    spawn_chance: float | Dict[BaseTerrain, float] = 0  # noqa: F821
    spawn_amount: float | Tuple[float, float] = 0

    def __init__(self, value: int = 0):
        super().__init__(value=value)
