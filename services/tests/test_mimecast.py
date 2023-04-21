import unittest

from ..mimecast import ServiceProvider as Mimecast


class TestMimecast(unittest.TestCase):
    """Test Mimecast ServiceProvider"""

    def test_dkim_positive_spf(self):
        """Ensure that Mimecast is detected by the SPF record, and the DKIM key resolves."""

        domain = "example.com"
        mx_records = []
        spf_records = ["include:au._netblocks.mimecast.com"]
        txt_records = []

        sp_under_test = Mimecast(domain, mx_records, spf_records, txt_records)

        self.assertEqual(sp_under_test.is_active, True)

    def test_dkim_positive_mx(self):
        """Ensure that Mimecast is detected by the SPF record, and the DKIM key resolves."""

        domain = "example.com"
        mx_records = ["au-smtp-inbound-1.mimecast.com"]
        spf_records = []
        txt_records = []

        sp_under_test = Mimecast(domain, mx_records, spf_records, txt_records)

        self.assertEqual(sp_under_test.is_active, True)
