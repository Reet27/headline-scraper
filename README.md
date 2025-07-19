# headline-scraper
# Web Scraper for News Headlines

This project is a part of the Python Developer Internship and focuses on building a web scraper that collects the latest news headlines from a public news website using Python.

## Objective

Scrape top news headlines from a news website and save them into a `.txt` file using Python.

## Tools Used

- Python
- requests
- BeautifulSoup (bs4)

## Deliverables

- Python script: `headline_scarper.py`
- Output file: `headlines.txt`

## How It Works

1. The script sends a GET request to the news website using the `requests` library.
2. The HTML content is parsed using `BeautifulSoup`.
3. Headline tags (like `<h1>`, `<h2>`, and `<h3>`) are extracted.
4. Cleaned headlines are written to a `.txt` file.

## Setup Instructions

### 1. Clone or Download the Repository

You can clone this repository or download the Python script directly.

### 2. Install Dependencies

Run the following command in your terminal to install required packages:

```bash
pip install requests beautifulsoup4
