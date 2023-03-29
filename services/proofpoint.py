
from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Proofpoint"

    @property
    def is_active(self) -> bool:
        if self._mx_includes(r"mx\w-\w{8}.gslb.pphosted.com"):
            return True

        return False

    @property
    def dkim_selectors(self) -> list:
        # looks like r"email\d{2,}"... not sure how it relates to the proofpoint mxa record?
        raise NotImplementedError
