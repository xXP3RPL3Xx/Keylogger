import unittest
from Keylogger.keylogger import Keylogger
from Keylogger.report_methods import report_to_file


class MyTestCase(unittest.TestCase):
    """Test class for Keylogger class."""

    def setUp(self) -> None:
        self.keylogger = Keylogger(60, report_to_file)

    def test_reset_log(self):
        """Test Keylogger's reset method."""

    def test_report(self):
        """Test the report method."""


if __name__ == '__main__':
    unittest.main()