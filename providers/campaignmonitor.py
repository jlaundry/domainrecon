
from . import DKIMSelectorCheck

class CampaignMonitor(DKIMSelectorCheck):
    selectors = ["cm"]

    @property
    def is_active(self) -> bool:
        raise NotImplementedError
