from __future__ import annotations
from ._base_terrain import BaseTerrain

from ursina import Texture
from world.terrain.traits.land import buildable_flat_land


class HillsTundra(BaseTerrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "world.terrain.hills_tundra"

        self.movement_modifier = 0.5
        self.water_availability = 0.25

        self._model = "assets/models/tiles/hills_grass.obj"
        self._texture = Texture("assets/models/tiles/hills_grass.png")

        self.add_modifiers(buildable_flat_land)
