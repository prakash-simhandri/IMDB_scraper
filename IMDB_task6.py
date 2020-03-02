from pprint import pprint
from IMDB_task5 import get_movie_list_details
#Task_6

def analyse_movies_language(movies_list):
	language_dict={}
	Languages=[]
	for language in movies_list:
		for lan in language['language']:
			if lan not in Languages:
				Languages.append(lan)

	for Languages_list in Languages:
		count=0
		for language_ in movies_list:
			for lan_ in language_['language']:
				if Languages_list == lan_:
					count+=1
		language_dict[Languages_list]=count
	return(language_dict)


movie_10_language=analyse_movies_language(get_movie_list_details)
# pprint(movie_10_language)