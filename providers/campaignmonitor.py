
from . import DKIMSelectorCheck

class CampaignMonitor(DKIMSelectorCheck):
    selectors = ["cm"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"cmail20.com"):
            return True

        return False
