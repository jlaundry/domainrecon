
import re

from . import DKIMSelectorCheck

class Forcepoint(DKIMSelectorCheck):

    @property
    def is_active(self) -> bool:
        if self._mx_includes(r"cust\d+-1.in.mailcontrol.com"):
            return True

        if self._spf_includes(r"mailcontrol.com"):
            return True

        return False

    @property
    def selectors(self) -> list:
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
