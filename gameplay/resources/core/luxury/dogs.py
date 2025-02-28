from __future__ import annotations
from gameplay.resource import BaseResource, ResourceTypeLuxury, ResourceValueType

from managers.i18n import _t


class Dogs(BaseResource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.dogs",
            _t("content.resources.core.dogs"),
            value,
            ResourceTypeLuxury,
            ResourceValueType.INT,
        )
