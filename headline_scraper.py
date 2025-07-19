import requests
from bs4 import BeautifulSoup

# Step 1: Set the URL of the news website
url = 'https://www.bbc.com/news'  # You can change this to any other news site

# Step 2: Set headers with a User-Agent to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

# Step 3: Fetch the webpage
response = requests.get(url, headers=headers)

# Step 4: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 5: Find all headline tags (commonly <h2> or <h3>)
headlines = soup.find_all(['h1', 'h2', 'h3'])

# Step 6: Extract and clean text
headline_texts = []
for tag in headlines:
    text = tag.get_text(strip=True)
    if text and len(text) > 10:  # Filter out very short headings
        headline_texts.append(text)

# Step 7: Save to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as f:
    for line in headline_texts:
        f.write(line + '\n')

print("✅ Headlines saved to 'headlines.txt'")
