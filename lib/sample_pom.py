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
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="event-header-name"]')))
        return self.driver.title
        
    def get_event_title(self) -> str:
        event_title = self.driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="event-header-name"]')
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(event_title))
        return event_title.text

    def close_browser(self) -> None:
        self.driver.close()

    
if __name__ == '__main__':
    pom = sample_pom()
    page_title = pom.navigate_to_url('https://app.say.rocks/apple-load-test-event-4')
    print(f"page title: {page_title}")
    event_title = pom.get_event_title()
    print(f"event title: {event_title}")
    pom.close_browser()