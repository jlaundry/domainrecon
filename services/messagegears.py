
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "MessageGears"
    dkim_selectors = ["gears"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"_spf.messagegears.net"):
            return True

        return False
