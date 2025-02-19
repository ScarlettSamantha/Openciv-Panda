from __future__ import annotations
from ._base_terrain import BaseTerrain

from ursina import Texture
from openciv.world.terrain.traits.land import buildable_flat_land

class FlatTundra(BaseTerrain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = 'world.terrain.flatland_grass'

        self.movement_modifier = 1
        self.water_availability = 0.25

        self._model = 'openciv/assets/models/tiles/grass2.obj'
        self._texture = Texture('openciv/assets/models/tiles/grass2.png')

        self.add_modifiers(buildable_flat_land)
