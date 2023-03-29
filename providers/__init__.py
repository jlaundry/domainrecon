
import re


class DKIMSelectorCheck():
    def __init__(self, domain, mx_records, spf_records, txt_records):

        self._domain = domain

        self._mx_records = mx_records
        self._spf_records = spf_records
        self._txt_records = txt_records

    @property
    def selectors(self) -> list:
        raise NotImplementedError

    @property
    def is_active(self) -> bool:
        raise NotImplementedError

    @property
    def active_selectors(self) -> list:
        if self.is_active:
            return self.selectors
        return []
        
    def _mx_includes(self, regex:str) -> bool:
        for record in self._mx_records:
            if re.search(regex, record) is not None:
                return True
        return False
    
    def _spf_includes(self, regex:str) -> bool:
        for record in self._spf_records:
            if re.search(regex, record) is not None:
                return True
        return False
    
    def _txt_includes(self, regex:str) -> bool:
        for record in self._txt_records:
            if re.search(regex, record) is not None:
                return True
        return False