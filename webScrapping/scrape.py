from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

def scrapeStory(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        html = page.inner_html("#website")
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find('h1').text.strip()
        author = soup.find('h2').text.strip()

        genre_soup = BeautifulSoup(page.inner_html(".genres"), 'html.parser')
        genre = [line.text.strip() for line in genre_soup.find_all('span')]

        story_soup = BeautifulSoup(page.inner_html(".story_text "), 'html.parser')
        story = [line.text.strip() for line in story_soup.find_all('p')]

        data = {
            "title": title,
            "author": author,
            "genre": genre,
            "story": story
        }

        json_data = json.dumps(data, indent=2)

        file_name = "_".join(title.split())

        with open(f'stories/{file_name}.json', 'w') as file:
            file.write(json_data)

        print(f"Story data has been successfully scraped and stored in '{file_name}.json'")
        


if __name__ == "__main__":
    scrapeStory('https://www.libraryofshortstories.com/onlinereader/an-adventure-in-futurity')
    scrapeStory('https://www.libraryofshortstories.com/onlinereader/the-apple')