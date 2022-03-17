import sys
from os import path
import unittest
sys.path.append(path.join(path.dirname(__file__), ".."))

import warnings

from lib.sample_pom import sample_pom

class SampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pom = sample_pom()

    def test_open_event_page(self):
        page_title = self.pom.navigate_to_url('https://app.say.rocks/apple-load-test-event-4')
        self.assertIn("Apple", page_title)

    def test_validate_event_title(self):
        title = self.pom.get_event_title()
        self.assertEqual("Apple load test event 4", title)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.pom.close_browser()


if __name__ == '__main__':
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    unittest.main()