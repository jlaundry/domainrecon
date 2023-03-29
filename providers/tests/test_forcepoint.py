import unittest

from ..forcepoint import Forcepoint

class TestForcepoint(unittest.TestCase):
    
    def test_positive(self):
        domain = "example.com"
        mx_records = ["cust1234-1.in.mailcontrol.com", "cust1234-2.in.mailcontrol.com"]
        spf_records = ["mailcontrol.com", "spf.protection.outlook.com"]
        txt_records = [
            "v=spf1 include:mailcontrol.com include:spf.protection.outlook.com -all"
            "google-site-verification=bla"
            "MS=ms00000000"
        ]
        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        self.assertEqual(fp.active_selectors, [
            "fpkey1234-1",
            "fpkey1234-2"
        ])

    def test_negative(self):
        domain = "example.com"
        mx_records = ["example-com.mail.protection.outlook.com"]
        spf_records = ["spf.protection.outlook.com"]
        txt_records = [
            "v=spf1 include:mailcontrol.com include:spf.protection.outlook.com -all"
            "google-site-verification=bla"
            "MS=ms00000000"
        ]
        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        self.assertEqual(fp.active_selectors, [])

    def test_partial(self):
        domain = "example.com"
        mx_records = ["example-com.mail.protection.outlook.com"]
        spf_records = ["mailcontrol.com", "spf.protection.outlook.com"]
        txt_records = [
            "v=spf1 include:mailcontrol.com include:spf.protection.outlook.com -all"
            "google-site-verification=bla"
            "MS=ms00000000"
        ]
        fp = Forcepoint(domain, mx_records, spf_records, txt_records)

        with self.assertRaises(Exception) as context:
            active_selectors = fp.active_selectors
        self.assertTrue('no matching MX records', context)

