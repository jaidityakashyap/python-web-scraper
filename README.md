# Python Web Scraper

A Python-based web scraper that extracts product information from the AllStag website using Requests, BeautifulSoup, and Pandas.

## Project Overview

This project demonstrates how Python can be used to collect structured product data from a website and save the results for further analysis.

The scraper collects product information from the AllStag Shop All page.

## Features

- Extracts product names
- Extracts current selling prices
- Extracts original prices
- Calculates discount percentages
- Extracts product links
- Stores the scraped data in a Pandas DataFrame
- Saves the final data as a CSV file

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## How It Works

1. Sends a request to the AllStag website using `Requests`.
2. Parses the webpage HTML using `BeautifulSoup`.
3. Finds product links and product information.
4. Extracts and cleans the prices.
5. Calculates the discount percentage.
6. Stores the information in a Pandas DataFrame.
7. Saves the scraped data as a CSV file.

## Installation

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 pandas
