
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Trend Micro HES"

    @property
    def is_active(self) -> bool:
        if self._txt_includes(r"spf.tmes.trendmicro.com"):
            return True

        if self._mx_includes(r"\w+.in.tmes-\w+.trendmicro.com"):
            return True

        return False

    @property
    def dkim_selectors(self) -> list:
        # defined per domain?
        raise NotImplementedError
