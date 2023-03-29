
from . import DKIMSelectorCheck

class Office365(DKIMSelectorCheck):
    selectors = ["selector1", "selector2"]

    @property
    def is_active(self) -> bool:
        if self._spf_includes(r"spf.protection.outlook.com"):
            return True
        
        if self._txt_includes(r"^MS=ms\d+"):
            return True

        return False        
