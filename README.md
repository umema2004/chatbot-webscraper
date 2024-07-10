# Wikipedia Scraper

This project provides a Python script that scrapes Wikipedia pages based on user input, extracts the title and a relevant paragraph, and processes the content using NLTK for further analysis.

## Features
- Scrapes Wikipedia pages by constructing appropriate URLs based on user input.
- Tries various capitalizations to find the correct Wikipedia page.
- Extracts and prints the first non-empty paragraph from the Wikipedia page.
- Identifies and highlights important words in the extracted content.

## Requirements
- Python 3.x
- requests library
- beautifulsoup4 library
- nltk library

## Setup
1. Install the required libraries:
    bash
    pip install requests beautifulsoup4 nltk
    
2. Download necessary NLTK data files:
    python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    

## Usage
1. Run the script:
    python
    python wikipedia_scraper.py
    
2. Enter a topic when prompted. The script will try to find and scrape the Wikipedia page for the given topic, extract the title and the first relevant paragraph, and print them.

## Script Explanation

### Helper Functions
- capitalize_each_word(topic): Capitalizes the first letter of each word in the topic and joins them with underscores.
- scrape_wikipedia_page(topic): Attempts to scrape the Wikipedia page for the given topic, trying various capitalizations if the initial request fails. Extracts the title and the first relevant paragraph from the page.

### Main Functionality
- Prompts the user for a topic and tries to find the corresponding Wikipedia page.
- Extracts and prints the title and the first non-empty paragraph.
- If no page is found, prompts the user to enter a new topic.

## Notes
- Ensure you have a stable internet connection while running the script, as it relies on real-time requests to Wikipedia.
- The script currently extracts and prints only the first relevant paragraph from the Wikipedia page. This can be extended to include more content or other elements as needed.
