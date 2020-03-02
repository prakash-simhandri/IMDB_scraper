from IMDB_task1 import movie_list
from pprint import pprint

# Task_3

def group_by_decade(movies):
	movie_by_decade={}
	for years in movies:
		division=years['year']
		decade=division // 10
		divisi=decade*10
		movie_by_decade[divisi]=[]
	for de_year in movie_by_decade:
		for movie in movies:
			_division=movie['year']
			_decade=_division // 10
			_divisi=_decade*10
			if de_year == divisi:
				movie_by_decade[de_year].append(movie)
	# pprint.pprint(movie_by_decade)
	return movie_by_decade

group_by_decade_analysis=group_by_decade(movie_list)
# pprint(group_by_decade_analysis)