import requests
from bs4 import BeautifulSoup

def capitalize_each_word(topic):
    return "_".join(word.capitalize() for word in topic.split())

def scrape_wikipedia_page(topic):
    while True:
        # Capitalize each word in the topic
        formatted_topic = capitalize_each_word(topic)
        url = f"https://en.wikipedia.org/wiki/{formatted_topic}"
        
        # Send a GET request to the Wikipedia page
        response = requests.get(url)
        
        # If the request was successful, parse the content
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find(id="firstHeading").text
            paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text().strip()]
            
            # Ensure we have at least one paragraph to print
            if paragraphs:
                first_paragraph = paragraphs[0]
                # If the first paragraph is empty, use the second one (if available)
                if not first_paragraph.strip() and len(paragraphs) > 1:
                    first_paragraph = paragraphs[1]
                return {
                    "title": title,
                    "first_paragraph": first_paragraph
                }
        
        # Try capitalizing words one by one if the initial request fails
        words = topic.split()
        for i in range(len(words)):
            capitalized_words = words[:]
            capitalized_words[i] = capitalized_words[i].capitalize()
            formatted_topic = "_".join(capitalized_words)
            url = f"https://en.wikipedia.org/wiki/{formatted_topic}"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.find(id="firstHeading").text
                paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text().strip()]
                
                # Ensure we have at least one paragraph to print
                if paragraphs:
                    first_paragraph = paragraphs[0]
                    # If the first paragraph is empty, use the second one (if available)
                    if not first_paragraph.strip() and len(paragraphs) > 1:
                        first_paragraph = paragraphs[1]
                    return {
                        "title": title,
                        "first_paragraph": first_paragraph
                    }
        
        # Prompt the user for a new topic if no valid page is found
        topic = input("No Wikipedia page found for the given topic. Please enter a new topic: ")

# Example usage
topic = input("Enter a topic: ")
result = scrape_wikipedia_page(topic)

if "error" in result:
    print(result["error"])
else:
    print(f"Title: {result['title']}")
    print(f"{result['first_paragraph']}")
