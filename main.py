from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import config
import time

option = Options()
option.add_argument("--headless")
option.add_argument("--headless")
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
option.add_experimental_option("detach", False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

# Navigate to the login page
login_url = "https://member.daraz.pk/user/login?redirect=https%3A%2F%2Fmember.daraz.pk%2Fuser%2Fprofile?redirect=https%3A%2F%2Fwww.daraz.pk"
driver.get(login_url)

# Wait for some time to load the page
time.sleep(3)

# Input email
email_input = driver.find_element('xpath', "//input[@placeholder='Please enter your Phone Number or Email']")
email_input.send_keys(config.email)  # Assuming email is stored in config.py

# Input password
password_input = driver.find_element('xpath', "//input[@placeholder='Please enter your password']")
password_input.send_keys(config.password)  # Assuming password is stored in config.py

# Click on the login button
login_button = driver.find_element('xpath', "//button[@class='next-btn next-btn-primary next-btn-large']")
login_button.click()

# Wait for login process to complete
time.sleep(5)

driver.get(
    f"https://www.daraz.pk/catalog/?q={config.search_Keyword}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34076TsDq6Vk")

product_links = driver.find_elements('xpath', "//div[contains(@class , 'box--ujueT')]")

# Open a CSV file to save the data
with open('product_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Rating', 'Price', 'Review']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for product in product_links:
        links = product.find_elements("xpath", ".//a")
        hrefs = [link.get_attribute("href") for link in links]

        for i in hrefs:
            time.sleep(5)
            driver.get(i)

            # Extracting title
            title = driver.find_element("xpath", "//span[contains(@class , 'pdp-mod-product-badge-title')]").text

            # Extracting rating
            try:
                rating = driver.find_element("xpath", "//a[contains(@class , 'pdp-review-summary__link')]").text
            except:
                rating = "N/A"

            # Extracting price
            price = driver.find_element("xpath", "//span[contains(@class , 'pdp-price')]").text

            # Extracting review
            review = "N/A"
            review_elements = driver.find_elements("xpath",
                                                   "//div[contains(@class , 'review-content')]//div[contains(@class , 'review-content-sl')]")
            if review_elements:
                review = "\n".join([element.text for element in review_elements])

            # Writing data to CSV file
            print({'Title': title, 'Rating': rating, 'Price': price, 'Review': review})
            writer.writerow({'Title': title, 'Rating': rating, 'Price': price, 'Review': review})

# Close the browser
driver.quit()
