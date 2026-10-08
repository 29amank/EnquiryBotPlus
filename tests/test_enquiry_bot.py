"""Offline tests for the EnquiryBotPlus demonstration.

These tests never send email and use synthetic contact details only.
"""
import csv
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from enquiry_bot import EnquiryBot


class TestEnquiryBot(unittest.TestCase):
    def setUp(self):
        sample = {
            "SENDER_EMAIL": "sender@example.test",
            "RECIPIENT_EMAIL": "recipient@example.test",
            "EMAIL_PASSWORD": "test-only-placeholder",
        }
        with patch("enquiry_bot.load_dotenv"), patch.dict(os.environ, sample):
            self.bot = EnquiryBot()

    def test_phone_validation(self):
        with patch("builtins.input", side_effect=["123", "9876543210"]):
            with patch("builtins.print"):
                self.assertEqual(self.bot.get_valid_phone_number(), "9876543210")

    def test_email_validation(self):
        with patch("builtins.input", side_effect=["invalid-email", "test@example.com"]):
            with patch("builtins.print"):
                self.assertEqual(self.bot.get_valid_email(), "test@example.com")

    def test_enquiry_lookup(self):
        self.assertIn("control panels", self.bot.retrieve_information("1").lower())
        self.assertEqual(self.bot.retrieve_information("wrong"), "Invalid product choice.")

    def test_csv_storage_uses_local_temporary_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test-only.csv"
            self.bot.customer_file = str(path)
            self.bot.store_customer_details("Test User", "9876543210", "test@example.com")
            with path.open(newline="") as stream:
                self.assertEqual(
                    list(csv.reader(stream)),
                    [["Test User", "9876543210", "test@example.com"]],
                )

    def test_smtp_is_mocked_without_network(self):
        with patch("enquiry_bot.smtplib.SMTP") as smtp, patch("builtins.print"):
            self.bot.send_email(
                "Test User", "9876543210", "test@example.com", "Test query"
            )
        smtp.assert_called_once_with("smtp.gmail.com", 587)
        conn = smtp.return_value.__enter__.return_value
        conn.starttls.assert_called_once_with()
        conn.login.assert_called_once_with(
            "sender@example.test", "test-only-placeholder"
        )
        conn.sendmail.assert_called_once()
        args, _ = conn.sendmail.call_args
        self.assertEqual(args[0:2], ("sender@example.test", "recipient@example.test"))


if __name__ == "__main__":
    unittest.main()
