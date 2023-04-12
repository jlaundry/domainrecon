
import re


class InsufficientDataError(Exception):
    "Raised when the ServiceProvider was unable to fully resolve a record"
    pass


class BaseServiceProvider():
    def __init__(self, domain, mx_records, spf_includes, txt_records):

        self._domain = domain

        self._mx_records = mx_records
        self._spf_includes_records = spf_includes
        self._txt_records = txt_records

    @property
    def is_active(self) -> bool:
        raise NotImplementedError

    @property
    def dkim_selectors(self) -> list:
        raise NotImplementedError

    @property
    def active_dkim_selectors(self) -> list:
        if self.is_active:
            return self.dkim_selectors
        return []

    def _mx_includes(self, regex:str) -> bool:
        for record in self._mx_records:
            if re.search(regex, record) is not None:
                return True
        return False

    def _spf_includes(self, regex:str) -> bool:
        for record in self._spf_includes_records:
            if re.search(regex, record) is not None:
                return True
        return False

    def _txt_includes(self, regex:str) -> bool:
        for record in self._txt_records:
            if re.search(regex, record) is not None:
                return True
        return False