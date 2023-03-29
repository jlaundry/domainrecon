
import unittest

from .. import domainrecon


class TestDomainRecon(unittest.TestCase):
    """Test DomainRecon ServiceProvider"""

    def test_basic(self):
        """Ensure that DomainRecon can be loaded."""

        domain = "example.com"

        domain_recon = domainrecon.DomainRecon(domain)

        