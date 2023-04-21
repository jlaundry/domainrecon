
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "GSuite"
    dkim_selectors = ["google"]

    @property
    def is_active(self) -> bool:
        if self._mx_includes("aspmx.l.google.com"):
            return True

        if self._mx_includes(r"alt\d.aspmx.l.google.com"):
            return True

        if self._mx_includes(r"aspmx\d.googlemail.com"):
            return True

        if self._spf_includes(r"_spf.google.com"):
            return True

        return False
