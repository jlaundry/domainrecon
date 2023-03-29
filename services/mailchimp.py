
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Mailchimp"
    dkim_selectors = ["k2", "k3"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"servers.mcsv.net"):
            return True

        return False
