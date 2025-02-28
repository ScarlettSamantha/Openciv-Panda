from __future__ import annotations
from gameplay.resource import BaseResource, ResourceValueType, ResourceTypeBasic


class BasicBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(configure_as_float_or_int=ResourceValueType.FLOAT, type=ResourceTypeBasic, *args, **kwargs)
