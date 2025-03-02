from typing import Dict, Tuple, Type
from data.terrain._base_terrain import BaseTerrain
from gameplay.resources.core.mechanics.mechanic_resource import MechanicBaseResource
from managers.i18n import T_TranslationOrStr, _t


class Contentment(MechanicBaseResource):
    key: str = "resource.core.mechanic.contentment"
    name: T_TranslationOrStr = _t("content.resources.core.contentment.name")
    description: T_TranslationOrStr = _t("content.resources.core.contentment.description")
    spawn_chance: float | Dict[Type[BaseTerrain], float] = 0
    spawn_amount: float | Tuple[float, float] = 0

    def __init__(self, value: int = 0):
        super().__init__(value=value)
