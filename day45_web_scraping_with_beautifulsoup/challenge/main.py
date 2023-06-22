import os 
from bs4 import BeautifulSoup
import requests

os.chdir('./day45_web_scraping_with_beautifulsoup/challenge')

# With html file
with open('website.html', 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)
[a.get_text() for a in soup.find_all(name="a")]
[a.get("href") for a in soup.find_all(name="a")]

soup.select_one(selector="p a")

# From website
response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

article_title = [a.get_text() for a in soup.select(".titleline")]
article_link = [a.get("href") for a in soup.select(".titleline a")]
article_upvote = [int(a.get_text().split(' ')[0]) for a in soup.select(".score")]

upvote_order = [b[0] for b in sorted(enumerate(article_upvote),key=lambda i:i[1])]
article_ordered = {}
for n in range(len(upvote_order)):
    article_ordered[n+1] = {
        'title':article_title[upvote_order[n]],
        'link':article_link[upvote_order[n]],
        }
    
# root/robots.txt to see what's not allow to scrape in a specific website