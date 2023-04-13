
import re

from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "HubSpot"

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"\d+.spf\d+.hubspotemail.net"):
            return True

        return False

    @property
    def dkim_selectors(self) -> list:
        hs_customer_id = None
        for spf in self._spf_includes_records:
            try:
                hs_customer_id = re.search(r"(\d+).spf\d+.hubspotemail.net", spf).group(1)
                continue
            except AttributeError:
                pass

        if hs_customer_id is None:
            raise Exception("Couldn't determine HubSpot customer ID (no SPF info)")

        return [f"hs1-{hs_customer_id}", f"hs2-{hs_customer_id}"]
