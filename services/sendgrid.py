
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "SendGrid"
    dkim_selectors = ["s1", "s2"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"sendgrid.net"):
            return True

        return False
