from Page_tests.base_test_case import BaseTestCase
from time import sleep
import unittest
from selenium import webdriver

import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from time import sleep, time
import pytest
import pytest_ordering

class selenium_TestSuite(BaseTestCase):

    def setUp(self):
        self.set_up()

    def tearDown(self):
        self.tear_down()

    def test_current_time_python(self):
        ts = time.time()
        readable_time = datetime.datetime.fromtimestamp(ts).isoformat()
        print(readable_time)

    def test_go_to_URL(self):
        self.driver.get("https://www.abc.com")

    def test_login_page_title(self):
        page_title = self.driver.title
        print(page_title)
        # Facebook - Log In or Sign Up
        #self.assertIn(page_title, "Facebook - Log In or Sign Up")

    def test_login_page_button(self):
        buttons = self.driver.find_elements_by_tag_name('button')
        total_buttons = len(buttons)
        print("Total number {0} buttons for front page of facebook".format(total_buttons))

    """
    # 1. Find all links displayed on login page
    
    """

    @pytest.mark.order1
    def test_login_page_total_links(self):
        alinks = self.driver.find_elements_by_tag_name('a')

        alinks_text = []

        for x in alinks:
            alinks_text.append(x.text)
            print(x.text)

        total_links = len(alinks)
        print("Total number {0} links for login page of facebook".format(total_links))

        print("sign up link passed")

    
if __name__ == '__main__':
    unittest.main()





