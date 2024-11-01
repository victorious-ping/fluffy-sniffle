import requests
from bs4 import BeautifulSoup

# Function to fetch HTML content
def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to parse HTML and extract desired data
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Example: Find all links on the page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.get_text(strip=True)
        print(f"Link text: {text} | URL: {href}")

# Main script
if __name__ == "__main__":
    url = "https://example.com"  # Replace with the target URL
    html_content = fetch_html(url)
    if html_content:
        parse_html(html_content)
