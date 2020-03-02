from IMDB_task5 import get_movie_list_details
from pprint import pprint

#Task_7

def analyse_movies_directors(director_data):
	Director_dict={}
	director_list=[]
	for director in director_data:
		for film_Director in director['director']:
			if film_Director not in director_list:
				director_list.append(film_Director)
	# print(director_list)
	for All_directors in director_list:
		count=0
		for director_ in director_data:
			for film_Director_ in director_['director']:
				if All_directors == film_Director_:
					count+=1
		Director_dict[All_directors]=count
	return(Director_dict)

movie_10_director=analyse_movies_directors(get_movie_list_details)
# pprint(movie_10_director)
