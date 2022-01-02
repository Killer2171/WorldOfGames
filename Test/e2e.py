import sys

import selenium.common.exceptions
from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")


def test_scores_service():
    result = ""
    my_driver.get("http://127.0.0.1:8777")
    score_value = int(my_driver.find_element_by_id('score').text)

    if 0 < score_value < 1001:
        result = True
    else:
        result = False
    return result


def main_function():
    result = test_scores_service()
    if result != True:
        return sys.exit(-1)
    else:
        return sys.exit(0)

main_function()

