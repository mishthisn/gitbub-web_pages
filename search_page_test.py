from Page_tests.base_test_case import BaseTestCase
import unittest

class fb_selenium_TestSuite(BaseTestCase):

    def setUp(self):
        self.set_up()

    def tearDown(self):
        self.tear_down()

    def test_go_to_URL(self):
        self.driver.get("https://www.searchwebsite.com")

    def test_all_table(self):
        all_tables = self.driver.find_elements_by_xpath()("//table")

        print(all_tables)

if __name__ == '__main__':
    unittest.main()
