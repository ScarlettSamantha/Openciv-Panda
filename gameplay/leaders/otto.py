from __future__ import annotations

from gameplay.leader import Leader
from gameplay.effect import Effects
from managers.i18n import t_


class Otto(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.otto",
            name=t_("civilization.germany.leaders.otto.name"),
            description=t_("civilization.germany.leaders.otto.description"),
            icon="civilization/germany/leaders/otto/leader_icon.png",
        )
        self._effects = Effects()
