from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Billboard:
    
    def ask_for_date(self):
        format = "%Y-%m-%d"
        response = input('Which year do you want to travel to? Type the date in the format YYYY-MM-DD:')
        try: 
            datetime.strptime(response, format)
        except: 
            print('Incorrect format, try again.')
            self.ask_for_date()
        else:
            print(f'You provided the date: {response}')
            self.user_response = response
            
    def get_top_100(self):
        url = f'https://www.billboard.com/charts/hot-100/{self.user_response}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
        self.song_titles = [value.get_text().strip() for value in titles]
        artists = soup.find_all(name="span", class_="u-max-width-330")
        self.artist_names = [name.get_text().strip() for name in artists]
        self.songs = {}
        for n in range(len(self.song_titles)):
            self.songs[n+1] = {
                'title':self.song_titles[n],
                'artist':self.artist_names[n]
            }