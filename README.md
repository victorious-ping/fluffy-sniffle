# fluffy-sniffle

A simple boilerplate for a web scraper using `BeautifulSoup` and `requests`.
The script sets up the basic structure, handles HTTP requests, and parses HTML content:

### How It Works
1. **`fetch_html(url)`:** Takes a URL, sends a GET request, and returns the HTML content.
   - Adds a user-agent header to mimic a real browser.
   - Handles exceptions for HTTP errors and other request-related issues.

2. **`parse_html(html_content)`:** Uses BeautifulSoup to parse the HTML and perform actions.
   - In this example, it finds and prints all the links on the page with their text and URLs. Modify this as needed to capture specific data.

3. **`if __name__ == "__main__":** Initializes the script and calls the fetch and parse functions.

This boilerplate is a flexible foundation for building more complex scrapers.