from IMDB_task1 import movie_list
from IMDB_task4 import scrape_movie_details
from pprint import pprint

# Task_5

def get_movie_list_details(movies_list):
	movie_url_list=[]
	ten_movie_url=(movies_list[:10])
	for All_url in ten_movie_url:
		movie_url_li=scrape_movie_details(All_url['url'])
		movie_url_list.append(movie_url_li)
	return movie_url_list
get_movie_list_details = get_movie_list_details(movie_list)
# pprint(get_movie_list_details)