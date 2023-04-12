
import unittest

from ..hubspot import ServiceProvider as HubSpot


class TestHubSpot(unittest.TestCase):
    """Test HubSpot ServiceProvider"""

    def test_dkim_positive(self):
        """Ensure that HubSpot is detected by the SPF record, and the DKIM key resolves."""

        domain = "example.com"
        mx_records = []
        spf_records = ["1234.spf42.hubspotemail.net"]
        txt_records = []

        sp_under_test = HubSpot(domain, mx_records, spf_records, txt_records)

        self.assertEqual(sp_under_test.active_dkim_selectors, [
            "hs1-1234",
            "hs2-1234"
        ])

    def test_dkim_negative(self):
        """Ensure that HubSpot is not detected."""

        domain = "example.com"
        mx_records = ["example-com.mail.protection.outlook.com"]
        spf_records = ["spf.protection.outlook.com"]
        txt_records = ["MS=ms00000000"]

        sp_under_test = HubSpot(domain, mx_records, spf_records, txt_records)

        self.assertEqual(sp_under_test.active_dkim_selectors, [])
