
import unittest

from ..forcepoint import ServiceProvider as Forcepoint


class TestForcepoint(unittest.TestCase):
    """Test Forcepoint ServiceProvider"""

    def test_dkim_positive(self):
        """Ensure that Forcepoint is detected by the MX record, and the DKIM key resolves."""

        domain = "example.com"
        mx_records = ["cust1234-1.in.mailcontrol.com", "cust1234-2.in.mailcontrol.com"]
        spf_records = []
        txt_records = []

        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        self.assertEqual(fp.active_dkim_selectors, [
            "fpkey1234-1",
            "fpkey1234-2"
        ])

    def test_dkim_negative(self):
        """Ensure that Forcepoint is not detected."""

        domain = "example.com"
        mx_records = ["example-com.mail.protection.outlook.com"]
        spf_records = ["spf.protection.outlook.com"]
        txt_records = ["MS=ms00000000"]

        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        self.assertEqual(fp.active_dkim_selectors, [])

    def test_dkim_partial(self):
        """Ensure that Forcepoint is detected by SPF, but DKIM key can't be resolved."""

        domain = "example.com"
        mx_records = ["example-com.mail.protection.outlook.com"]
        spf_records = ["mailcontrol.com", "spf.protection.outlook.com"]
        txt_records = ["MS=ms00000000"]

        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        with self.assertRaises(Exception) as context:
            _ = fp.active_dkim_selectors
        self.assertTrue(context, 'no matching MX records')
