
from . import DKIMSelectorCheck

class SendGrid(DKIMSelectorCheck):
    selectors = ["s1", "s2"]

    @property
    def is_active(self) -> bool:
        raise NotImplementedError
