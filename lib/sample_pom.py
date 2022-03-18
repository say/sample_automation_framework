import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class sample_pom:

    def __init__(self) -> None:
        chrome_path = path.join(path.dirname(__file__), '..', 'config', 'chromedriver')        
        self.driver = webdriver.Chrome(chrome_path)
    
    def navigate_to_url(self, url: str) -> str:
        """
        navigates to the application pages and validates page displays
        :param url: the url of the page to navigate to
        """
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="event-header-name"]')))
        return self.driver.title
        
    def get_event_title(self) -> str:
        """
        Retrieves the title displayed on the event page
        """
        event_title = self.driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="event-header-name"]')
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(event_title))
        return event_title.text

    def close_browser(self) -> None:
        """
        closes the active session of the current browser
        """
        self.driver.close()