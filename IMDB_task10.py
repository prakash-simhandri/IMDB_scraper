from IMDB_task8_9 import Movies_Dict
import json
from pprint import pprint

# Task 10   

def analyse_language_and_directors(Dict):

	list_1=[]
	for i in Dict:
		a=(i["director"])
		for j in a:
			if j not in list_1:
				list_1.append(j)
	# print(list_1)
	director_dict={}
	for k in list_1:
		list_2=[]
		list_3=[]

		for l in Dict:
			b=(l["director"])
			for m in b:
				if m==k:
					language_1=(l["language"])
					# print(language_1)
					for n in language_1:
						list_2.append(n)
						if n not in list_3:
							list_3.append(n)
		dict_language={}
		for p in list_3:
			counter=0
			for q in list_2:
				if q==p:
					counter=counter+1
				dict_language[p]=counter
		director_dict[k]=dict_language
	return(director_dict)
	# pprint(director_dict)

# pprint(analyse_language_and_directors(Movies_Dict))