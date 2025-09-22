import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/" # example: random quotes

# Send requests with headers 
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Parsing HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extracting quotes
quotes = []
for q in soup.select(".quote"):
    text = q.select_one(".text").get_text(strip=True) if q.select_one(".text") else None
    author = q.select_one(".author").get_text(strip=True) if q.select_one(".author") else None

    if text and author:
        quotes.append({"title": text, "company": author})

# Save to CSV
df = pd.DataFrame(quotes)
df.to_csv("quotes.csv", index=False)
print(f"Scrapped len({quotes}) jobs and saved to job.csv")