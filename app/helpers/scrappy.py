import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def initialize_selenium():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument("--start-minimized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = uc.Chrome(options=options, use_subprocess=False)
    driver.delete_all_cookies()

    return driver


def scrape_data(category: str) -> list:
    url = f"https://webscraper.io/test-sites/e-commerce/static/{category}"
    all_products = []

    driver = initialize_selenium()
    driver.get(url)
    time.sleep(3)

    driver.save_screenshot('screenshot.png')

    try:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = []

            for product in soup.find_all('div', 'thumbnail'):
                product_data = {
                    "title": product.find('a', class_='title').text.strip(),
                    "image": product.find('img', class_='img-fluid card-img-top image img-responsive')['src'],
                    "link": product.find('a', class_='title')['href'],
                    "price": product.find('h4', class_='float-end price card-title pull-right').text.strip(),
                    "description": product.find('p', class_='description card-text').text.strip(),
                    "reviews": product.find('p', class_='float-end review-count').text.strip(),
                }
                products.append(product_data)
            all_products.extend(products)

            next_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="static-pagination"]/nav/ul/li[4]/a'))
            )

            next_button.click()
            time.sleep(2)

    except TimeoutException:
        pass
    finally:
        driver.quit()

    return all_products
