import sys

import selenium.common.exceptions
from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")

def test_scores_service():
    result = ""
    my_driver.get("http://127.0.0.1:5001")
    score_value = int(my_driver.find_element_by_id('score').text)
    if 0 < score_value < 1001:
        result = True
    else:
        result = False
    return result
    my_driver.close()


def main_function():
    result = test_scores_service()
    if result != True:
        sys.exit(-1)
    else:
        sys.exit(0)
