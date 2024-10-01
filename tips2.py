import requests
from bs4 import BeautifulSoup

def scrape_quick_facts(url):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200: 
        soup = BeautifulSoup(response.content, 'html.parser')
        quick_facts_section = soup.find('div', class_='quick-facts')
        if quick_facts_section:
            quick_facts_lines = quick_facts_section.text.strip()
            return quick_facts_lines
        else:
            print("Quick facts section not found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

