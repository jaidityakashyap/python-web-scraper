# Libraries used for web scraping and data handling
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URLs
url = "https://www.allstag.com/collections/shop-all"
base_url = "https://www.allstag.com"

# send request to the website
response = requests.get(url)

# Check whether the website responded successfully
print(response.status_code)

#parse the HTML content of website
soup = BeautifulSoup(response.text,"html.parser")

# Store the scraped product information
product_data = []

# Find all links that have an href attribute
products = soup.find_all("a",href = True)

# Go through each link one by one
for product in products:
    name = product.get_text(strip = True)

    # Keep only links that point to products and have a product name
    if "/products/" in product["href"] and name:

        # Extract and clean the current selling price
        price = product.parent.find("span", class_= "product--actual-price")
        price_text = price.get_text(strip = True)
        price_text = float(price_text.replace("Rs. ", ""))

        # Extract and clean the original price
        original_price = product.parent.find("span", class_="product--cut-price")
        original_price_text = original_price.get_text(strip = True)
        original_price_text = float(original_price_text.replace("Rs. ","").replace(",",""))

        # Calculate discount percentage
        discount = round(((original_price_text - price_text)/original_price_text)*100,2)

        # Store the product information
        product_data.append({
        "Name": name,
        "price": price_text,
        "original_price": original_price_text,
        "Discount%": discount,
        "link": base_url+product["href"]
        })

# Convert the scraped data into a Pandas DataFrame
df = pd.DataFrame(product_data)

# Display the data in the terminal
print(df)

# Save the data as a CSV file
df.to_csv("web_scraper_CVS", index=False)

