
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Zendesk"
    dkim_selectors = ["zendesk1"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"support.zendesk.com"):
            return True

        return False
