from __future__ import annotations
from gameplay.resources.core.basic._base import BasicBaseResource
from managers.i18n import _t


class Science(BasicBaseResource):
    def __init__(self, value, *args, **kwargs):
        super().__init__(
            "core.basic.science",
            _t("content.resources.science.name"),
            _t("content.resources.science.description"),
            value,
            *args,
            **kwargs,
        )
