
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "CampaignMonitor"
    dkim_selectors = ["cm"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"cmail20.com"):
            return True

        return False
