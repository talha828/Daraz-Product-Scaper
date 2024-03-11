# Daraz Product Scraper

![0622341446411c3](https://github.com/talha828/Daraz-Product-Scaper/assets/61588132/760289ce-3cd4-4a42-8288-4ed399639a9c)


## Overview

This is a Python script built for scraping product data from [Daraz.pk](https://www.daraz.pk/) using Selenium with Chrome WebDriver in headless mode.

## Features

- Log in to Daraz account
- Search for products
- Scrapes product data including title, rating, price, and reviews (if available)
- Saves the scraped data into a CSV file

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- webdriver-manager
- csv

You can install the required packages using the following command:

```bash
pip install selenium webdriver-manager
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/daraz-product-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd daraz-product-scraper
   ```
3. Install dependencies:
   ```bash
   cd daraz-product-scraper
   ```
4. Set up your Daraz account credentials and search keyword in the config.py file.
5. Run the script:
   ```bash
   python scraper.py
   ```
## Configuration
You need to configure the following variables in the config.py file:

- email: Your Daraz account email or phone number
- password: Your Daraz account password
- search_Keyword: The keyword you want to search for on Dar

## Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details


