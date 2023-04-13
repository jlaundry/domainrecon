
import importlib
import logging
import pkgutil
import json

import dns.resolver
import checkdmarc

from .services import InsufficientDataError


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.debug("DEBUG active")
logging.info("info active")
logging.warning("warning active")
logging.error("error active")


def get_recursive_includes(parsed:str) -> list:
    result = []
    # TODO if parsed['redirect'] is not None: (i.e., facebook.com)
    for include in parsed['include']:
        result.append(include['domain'])
        result += get_recursive_includes(include['parsed'])
    return result


class DomainRecon():
    def __init__(self, domain, extra_dkim_selectors=[]):
        self.domain = domain
        self.extra_dkim_selectors = extra_dkim_selectors

        self.errors = []
        self.__active_services = []

        self.__spf_record = None
        self.__mx_records = []
        self.__txt_records = []

    def _get_services(self) -> list:
        if len(self.__active_services) > 0:
            return self.__active_services

        service_pkgs = [name for loader, name, is_pkg in pkgutil.iter_modules(['services']) if not is_pkg]

        for service in service_pkgs:
            service_module = importlib.import_module(f"services.{service}")
            service_class = service_module.ServiceProvider
            inst = service_class(self.domain, self.dns_mx_records, self.dns_spf_includes, self.dns_txt_records)

            logging.debug(f"services.{inst.name} is_active:{inst.is_active}")

            if inst.is_active:
                self.__active_services.append(inst)

        logging.info(f"{len(self.__active_services)}/{len(service_pkgs)} active services")
        return self.__active_services

    @property
    def identified_services(self):
        return [service.name for service in self._get_services()]

    @property
    def dkim_selectors(self):
        result = []
        
        if isinstance(self.extra_dkim_selectors, list):
            result += self.extra_dkim_selectors

        for service in self._get_services():
            try:
                result += service.dkim_selectors
            except InsufficientDataError as e:
                self.errors.append(str(e))
            except NotImplementedError as e:
                self.errors.append(f"{service.name} DKIM selectors not implemented")

        return sorted(result)

    @property
    def dns_mx_records(self):
        if len(self.__mx_records) == 0:
            result = dns.resolver.resolve(self.domain, 'MX')
            for rdata in result:
                self.__mx_records.append(rdata.exchange.to_text())
        return self.__mx_records

    @property
    def dns_spf_includes(self):
        if self.__spf_record is None:
            self.__spf_record = checkdmarc.get_spf_record(self.domain)
            #print(json.dumps(self.__spf_record, indent=4))

        include_domains = get_recursive_includes(self.__spf_record['parsed'])#
        return include_domains

    @property
    def dns_txt_records(self):
        if len(self.__txt_records) == 0:
            result = dns.resolver.resolve(self.domain, 'TXT')
            for rdata in result:
                self.__txt_records.append(rdata.to_text())
        return self.__txt_records
