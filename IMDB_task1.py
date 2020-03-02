import requests	
from bs4 import BeautifulSoup
from pprint import pprint
url='https://www.imdb.com/india/top-rated-indian-movies/'
movie=requests.get(url)
suop=BeautifulSoup(movie.text,"html.parser")

# Task_1

def scrape_top_list():

	movie_div=suop.find("div", class_='lister')
	table_=movie_div.find("tbody",class_='lister-list')
	movie_tr=table_.find_all("tr")
	All_movie_list=[]
	for tr in movie_tr:
		name=tr.find("td",class_='titleColumn')
		film_name=name.get_text().strip().split(".")
		# return film_name
		movie_names=name.find("a").get_text()
		# print(movie_names)
		movie_year=name.find("span").get_text()
		# print(movie_year)
		movie_position=film_name[0]
		# print(movie_position)
		movie_url=name.find("a").get("href")
		movie_link="https://www.imdb.com"+movie_url
		
		rating_in_movie=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()


		movie_details={'name':'','url':'','position':'','rating':'','year':''}

		movie_details['name']=movie_names
		movie_details['url']=movie_link
		movie_details['position']=int(movie_position)
		movie_details['rating']=float(rating_in_movie)
		movie_details['year']=int (movie_year.strip("()"))
		All_movie_list.append(movie_details)
	return All_movie_list

movie_list=scrape_top_list()
# pprint(movie_list)