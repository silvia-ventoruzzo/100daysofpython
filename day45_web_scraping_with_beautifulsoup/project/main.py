import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

top_movies = [title.get_text() for title in soup.find_all(name="h3", class_="title")]
# Have to fix number 12 since it's using : instead of ) after number
top_movies[top_movies.index('12: The Godfather Part II')] = '12) The Godfather Part II'
top_movies = {int(movie.split(")")[0]):movie.split(")")[1].strip() for movie in top_movies}
top_movies = dict(sorted(top_movies.items()))

top_movies_text = '\n'.join(f'{key}) {value}' for key, value in top_movies.items())
with open("./day45_web_scraping_with_beautifulsoup/project/movies.txt", "w") as file:
    file.write(top_movies_text)
