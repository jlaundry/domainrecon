
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "GSuite"
    dkim_selectors = ["google"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"_spf.google.com"):
            return True

        return False
