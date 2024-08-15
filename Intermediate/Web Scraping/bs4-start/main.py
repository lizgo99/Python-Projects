from bs4 import BeautifulSoup
import requests

live_website = "https://news.ycombinator.com/news"
static_website = "https://appbrewery.github.io/news.ycombinator.com/"

response = requests.get(live_website)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.find_all(name="span", class_="titleline")
article_upvotes = soup.find_all(name="span", class_="score")
texts = [tag.find("a").getText() for tag in article_tags]
links = [tag.find("a").get("href") for tag in article_tags]
upvotes = [int(score.getText().split()[0]) for score in article_upvotes]

i = upvotes.index(max(upvotes))
print(texts[i])
print(links[i])

