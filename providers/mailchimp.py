
from . import DKIMSelectorCheck

class Mailchimp(DKIMSelectorCheck):
    selectors = ["k2", "k3"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"servers.mcsv.net"):
            return True

        return False
