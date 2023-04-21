
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Email Octopus"
    dkim_selectors = ["eo"]

    @property
    def is_active(self) -> bool:
        if self._txt_includes(r"\w+.\w+.eoidentity.com"):
            return True

        return False
