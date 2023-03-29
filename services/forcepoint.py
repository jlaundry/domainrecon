
import re

from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Forcepoint"

    @property
    def is_active(self) -> bool:
        if self._mx_includes(r"cust\d+-\d.in.mailcontrol.com"):
            return True

        if self._spf_includes(r"mailcontrol.com"):
            return True

        return False

    @property
    def dkim_selectors(self) -> list:
        fp_customer_id = None
        for mx in self._mx_records:
            try:
                fp_customer_id = re.search(r"cust(\d+)-\d.in.mailcontrol.com", mx).group(1)
                continue
            except AttributeError:
                pass

        if fp_customer_id is None:
            raise Exception("Couldn't determine Forcepoint customer ID (no matching MX records)")

        return [f"fpkey{fp_customer_id}-1", f"fpkey{fp_customer_id}-2"]
