import requests
from bs4 import BeautifulSoup


yc_url = 'https://news.ycombinator.com/'
greatest_movies_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

def yc_scrapper(url):
    response = requests.get(url)

    yc_web_page = response.text
    soup = BeautifulSoup(yc_web_page, 'html.parser')

    links = [
        a for span in soup.find_all('span', class_='titleline') 
        for a in span.find_all('a', recursive=False)
    ]

    for link in links:
        print(f'Link: {link.get('href')}')
        print(f'Title: {link.getText()}')



def movies_scrapper(url):
    response = requests.get(url)
    movies_page = response.text

    soup = BeautifulSoup(movies_page, 'html.parser')

    movies = soup.find_all('h3', class_='title')

    for movie in movies:
        print(f'Title: {movie.getText()}\n')

    # print(movies)


# yc_scrapper(yc_url)
movies_scrapper(greatest_movies_url)