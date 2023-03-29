
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "AmazonSES"

    @property
    def is_active(self) -> bool:
        if self._mx_includes(r"inbound-smtp\.[\w\-]+\.amazonaws.com"):
            return True
        return False

    @property
    def dkim_selectors(self) -> list:
        if self.is_active:
            # It looks like AWS' DKIM selectors are completely random?
            raise NotImplementedError
        else:
            return []
