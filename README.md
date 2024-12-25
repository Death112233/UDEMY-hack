---

# Udemy Link Extractor - README

## Overview
**Udemy Link Extractor** is a Python-based web scraper tool that extracts Udemy course links (along with coupons) from a given website. This tool uses the `requests` library to send HTTP requests and `BeautifulSoup` from `bs4` to parse HTML and extract the necessary links. The tool allows recursive scraping of webpages up to a specified depth.

This tool is ideal for extracting Udemy course links from coupon and course-sharing websites.

## Features
- Extracts Udemy links from a webpage and its linked pages.
- Supports recursive scraping to a specified depth.
- Unique link filtering to avoid duplicates.
- Friendly display with helpful messages and a banner.
- Customizable maximum scraping depth.

## Installation
To use this script, you'll need Python installed on your machine along with the following dependencies:

1. **requests** – For sending HTTP requests.
2. **beautifulsoup4** – For parsing HTML and extracting links.
3. **urllib** – For URL parsing and manipulation.

### Step-by-step installation:

1. **Install Python** (if not already installed):
   - Download Python from [python.org](https://www.python.org/downloads/).

2. **Install required dependencies**:
   Run the following command to install the necessary libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Download the script**:
   - Save the provided Python script (e.g., `udemy_link_extractor.py`) on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder where the script is saved.
3. Run the script using Python:

   ```bash
   python udemy_link_extractor.py
   ```

4. Follow the on-screen prompts:
   - Enter the URL of the website to scrape (e.g., `https://coursevania.com`).
   - Enter the maximum scraping depth (between 1 and 6).

   Example:
   ```
   Enter the website URL (e.g., https://coursevania.com): https://example.com
   Enter the maximum scraping depth (1-6): 3
   ```

5. The script will begin scraping the provided website and its linked pages for Udemy links. The results will be displayed in the terminal with a count of total Udemy links found.

## Script Explanation

### 1. **display_banner()**
   This function prints a banner to the console that includes a description of the tool, as well as social media links.

### 2. **extract_udemy_links(url)**
   - This function extracts Udemy links from the provided URL.
   - It searches for all anchor tags (`<a>`) with `href` attributes containing "udemy.com".
   - It returns a list of unique Udemy links.

### 3. **scrape_links(base_url, max_depth, current_depth=0, visited=None)**
   - This function performs the recursive scraping.
   - It checks for Udemy links on the current page and continues scraping any internal links (links that belong to the same domain) up to the specified depth.

### 4. **main()**
   - This is the entry point of the script. It initializes the scraping process by calling the `scrape_links` function and prints out the results.

## Example Output

```
**************************************
*    Udemy Link Extractor            *
*    Extract Udemy Coupons Easily    *
*                                    *
*    Join Telegram:                  *
*    https://t.me/Udemydeath         *
*    https://t.me/English_chating0   *
*                                    *
*    WhatsApp:                       *
*    https://whatsapp.com/channel/0029VaCBM8AKGGG9l6g6Lz0b *
**************************************

Enter the website URL (e.g., https://coursevania.com): https://example.com
Enter the maximum scraping depth (1-6): 3

[INFO] Scraping https://example.com for Udemy links up to depth 3...

[INFO] Scraping at depth 0...
[INFO] Scraping at depth 1...
[INFO] Scraping at depth 2...
[INFO] Scraping at depth 3...

==================================================
[RESULTS] Scraping Completed!
[STATS] Total Udemy Links Found: 15
==================================================

01. https://www.udemy.com/course/example-course-1/
02. https://www.udemy.com/course/example-course-2/
03. https://www.udemy.com/course/example-course-3/
...
```

## Important Notes

- **Rate Limiting**: The script adds a 1-second delay between scraping different pages to prevent being rate-limited or blocked by the website.
- **Error Handling**: The script handles errors, including failed requests or parsing errors, and will display an error message without crashing.
- **Depth Limit**: The maximum depth is set between 1 and 6 to avoid excessive recursion and to ensure the script performs efficiently.

## Disclaimer

- The tool is intended for educational purposes and should be used responsibly. Do not scrape websites that prohibit scraping in their `robots.txt` or terms of service.
- The creator is not responsible for misuse of the tool or any legal consequences.

## Support & Contact

If you encounter any issues or have questions, you can join the following communities for support:

- **Telegram**: [Udemydeath](https://t.me/Udemydeath)
- **WhatsApp**: [Click here](https://whatsapp.com/channel/0029VaCBM8AKGGG9l6g6Lz0b)

Happy scraping! 🎉
