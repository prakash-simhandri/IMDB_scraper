from IMDB_task1 import movie_list
from pprint import pprint

#Task_2

def group_by_year(movies):
	movie_by_year={}
	for movie in movies:
		movie_by_year[movie['year']]=[]
	# print(movie_by_year)

	for year_key in movie_by_year:
		for movie_ in movies:
			year=movie_['year']
			if year==year_key:
				movie_by_year[year].append(movie_)
	# pprint.pprint(movie_by_year)
	return movie_by_year

group_by_year_analysis=group_by_year(movie_list)
# pprint(group_by_year_analysis)