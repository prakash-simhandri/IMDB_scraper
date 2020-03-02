from IMDB_task8_9 import Movies_Dict
from pprint import pprint

# Task_11

def analyse_movies_genre(movie_data):
	genres_list=[]
	for genres in movie_data:
		for one_genres in genres['genre']:
			if one_genres not in genres_list:
				genres_list.append(one_genres)
	total_value={}
	All_genres=[]
	for genres_ in movie_data:
		for one_genres_ in genres_['genre']:
			All_genres.append(one_genres_)
	for genre_1 in genres_list:
		total=All_genres.count(genre_1)
		total_value[genre_1]=total
	return(total_value)

All_movie_genre=analyse_movies_genre(Movies_Dict)
# pprint(All_movie_genre)