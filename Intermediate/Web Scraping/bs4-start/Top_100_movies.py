from bs4 import BeautifulSoup
import requests

link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(link)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
movie_titles = movie_titles[::-1]

with open("/Users/lizgokhvat/Desktop/Projects/Python_Projects/Intermediate/Web Scraping/bs4-start/movies.txt", "w") as movies_file:
    for title in movie_titles:
        movies_file.write(title + '\n')
    

