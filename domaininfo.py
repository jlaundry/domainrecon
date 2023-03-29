
import importlib
import logging
import pkgutil


SERVICES = [name for loader, name, is_pkg in pkgutil.iter_modules(['services']) if not is_pkg]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.debug("DEBUG active")
logging.info("info active")
logging.warning("warning active")
logging.error("error active")


class DomainInfo():
    def __init__(self, domain, extra_dkim_selectors=[]):
        self.domain = domain
        self.extra_dkim_selectors = extra_dkim_selectors

        self.__active_services = []

    def _get_services(self) -> list:
        if len(self.__active_services) > 0:
            return self.__active_services

        for service in SERVICES:
            service_module = importlib.import_module(f"services.{service}")
            service_class = service_module.ServiceProvider
            inst = service_class(self.domain, self.dns_mx_records, self.dns_spf_record, self.dns_txt_records)

            logging.debug(f"services.{inst.name} is_active:{inst.is_active}")

            if inst.is_active:
                self.__active_services.append(inst)

        logging.info(f"{len(self.__active_services)}/{len(SERVICES)} active services")
        return self.__active_services

    def dkim_selectors(self):
        for service in self._get_services():
            logging.debug(service.name)

    @property
    def dns_mx_records(self):
        # TODO
        return []

    @property
    def dns_spf_record(self):
        # TODO
        return []

    @property
    def dns_txt_records(self):
        # TODO
        return []
