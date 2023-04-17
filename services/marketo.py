
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Marketo"
    dkim_selectors = ["m1"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"mktomail.com"):
            return True

        return False
