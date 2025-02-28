from __future__ import annotations
from gameplay.resource import BaseResource, ResourceTypeStrategic, ResourceValueType

from managers.i18n import _t


class Graphite(BaseResource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.strategic.graphite",
            _t("content.resources.core.graphite"),
            value,
            ResourceTypeStrategic,
            ResourceValueType.INT,
        )
