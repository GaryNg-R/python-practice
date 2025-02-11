import requests
from bs4 import BeautifulSoup


# Define the stock URL (Example: Apple - AAPL)
stock_symbol = "AAPL"
url = f"https://finance.yahoo.com/quote/{stock_symbol}"

# Fetch the webpage
headers = {"User-Agent": "Mozilla/5.0"}  # Prevent being blocked
response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract the stock price
price_tag = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
if price_tag:
    print(f"{stock_symbol} Current Price: ${price_tag.text}")
else:
    print("Failed to fetch stock price.")
