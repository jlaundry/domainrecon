


from . import BaseServiceProvider

class ServiceProvider(BaseServiceProvider):
    name = "Mimecast"

    @property
    def is_active(self) -> bool:
        if self._mx_includes(r"\w+-smtp-inbound-\d.mimecast.com"):
            return True

        if self._spf_includes(r"_netblocks.mimecast.com"):
            return True

        return False

    @property
    def dkim_selectors(self) -> list:
        # User configurable - most follow selector\d{4,8}...
        raise NotImplementedError
