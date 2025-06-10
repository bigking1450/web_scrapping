import requests
from bs4 import BeautifulSoup


yc_url = 'https://news.ycombinator.com/'
greatest_movies_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

def hacker_news_scraper(url):
    response = requests.get(url)

    yc_web_page = response.text
    soup = BeautifulSoup(yc_web_page, 'html.parser')

    links = [
        a for span in soup.find_all('span', class_='titleline') 
        for a in span.find_all('a', recursive=False)
    ]

    # article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]


    for link in links:
        print(f'Link: {link.get('href')}')
        print(f'Title: {link.getText()}')



def empire_movie_scraper(url):
    response = requests.get(url)
    movies_page = response.text

    soup = BeautifulSoup(movies_page, 'html.parser')

    movies = soup.find_all('h3', class_='title')

    # displaying the movies from 100 to 1 to the console
    for movie in movies:
        print(f'Title: {movie.getText()}\n')

    # =========================================
    # displaying the movies from 1 t0 100 and writing the movies to a text file.
    movie_titles = [movie.getText() for movie in movies]
    all_movies = movie_titles[::-1]

    with open('movies.txt', mode='w', encoding='utf-8') as file:
        for movie in all_movies:
            file.write(f'{movie}\n')
    


hacker_news_scraper(yc_url)
# empire_movie_scraper(greatest_movies_url)