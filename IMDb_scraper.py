import requests	
from bs4 import BeautifulSoup
import pprint,os.path
import time,random,json
from urllib.request import urlopen
url='https://www.imdb.com/india/top-rated-indian-movies/'
movie=requests.get(url)
# print (movie.text)
suop=BeautifulSoup(movie.text,"html.parser")
# print (suop.title)

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
		# print(rating_in_movie)

		movie_details={'name':'','url':'','position':'','rating':'','year':''}

		movie_details['name']=movie_names
		movie_details['url']=movie_link
		movie_details['position']=int(movie_position)
		movie_details['rating']=float(rating_in_movie)
		movie_details['year']=int (movie_year.strip("()"))
		All_movie_list.append(movie_details)
	return All_movie_list

movie_list=scrape_top_list()
# print (movie_list)

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
# print(group_by_year_analysis)

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
# print(group_by_decade_analysis)



#Task_12

def scrape_movie_cast(movie_caste_url):
	ID=''
	for _id in movie_caste_url[27:]:
		if '/' not in _id:
			ID+=_id
		else:
			break
	film_name = ID
	# print(film_name)
	movie_caste=requests.get(movie_caste_url)
	suop_1=BeautifulSoup(movie_caste.text,"html.parser")
	All_details=suop_1.find_all('div',class_='see-more')
	casts_list=[]
	for i in All_details:
		if (i.text).strip() == 'See full cast »':
			connect_url=urlopen('https://www.imdb.com/title/'+film_name+'/'+i.find('a').get('href'))
			soupa=BeautifulSoup(connect_url,"html.parser")
			caste_tabal=soupa.find('table',class_='cast_list')
			te_body=caste_tabal.find_all('tr')
			for td in te_body:
				actors_name=td.find_all('td',class_='')
				for actor in actors_name:
					imdb_id=actor.find('a').get('href')[6:15]
					# print(imdb_id)
					names=actor.find('a').get_text()
					# print(names.text)
					cast={'name':names.strip(),
						'imdb_id':imdb_id}
					casts_list.append(cast)
			# pprint.pprint(casts_list)
			return(casts_list)
# All_movie_cast=scrape_movie_cast(movie_list[0]['url'])
# pprint.pprint(All_movie_cast)

# Task_4

def scrape_movie_details(movie_url):
	#Task_9
	timer = random.randint(1,3)
	#Task_8
	ID=''
	for _id in movie_url[27:]:
		if '/' not in _id:
			ID+=_id
		else:
			break
	file_name = ID
	if os.path.exists('IMD_data/'+file_name+'.json'):
		with open('IMD_data/'+file_name+'.json',"r")as open_file:
			data=json.load(open_file)
			return (data)
	else:
		time.sleep(timer)
		movie_downlod=requests.get(movie_url)
		suop=BeautifulSoup(movie_downlod.text,'html.parser')

		movie_title=suop.find('div',class_='title_bar_wrapper')
		movie_name=movie_title.find('h1').get_text()
		film_=movie_name.split()
		film_.pop()
		film_tital=' '.join(film_)
		# print(film_tital)


		Director_div=suop.find('div',class_='plot_summary')
		second_div=Director_div.find('div',class_='credit_summary_item')
		Director_=second_div.find_all('a')
		Directors_list=[Director.text for Director in Director_]
		# print(Directors_list)

		movie_bio=Director_div.find('div',class_='summary_text').get_text().strip()
		# print(movie_bio)

		# movie_image = suop.find('div',class_='slate_wrapper')


		movie_postar = suop.find('div',class_='poster').a.img['src']
		# print(movie_postar)
		

		Genre_list=[]
		film_details=suop.find('div',attrs ={'class':'article','id':'titleStoryLine'})
		Genre=film_details.find_all('div',class_='see-more inline canwrap')
		for movie_g in Genre:
			if movie_g.find('h4').text == 'Genres:':
				gen=movie_g.find_all('a')
				for g in gen:
					Genre_list.append(g.text)
		# print(Genre_list)




		movie_detail=suop.find('div',{'class':'article','id':'titleDetails'})
		list_of_div=movie_detail.find_all('div',class_='txt-block')
		movie_Country=''
		movie_Language=[]
		for h4 in list_of_div:
			div=(h4.find_all('h4',class_='inline'))
			for div_list in div:
				if div_list.text in 'Country:':
					movie_Country=(h4.find('a').text)
				if div_list.text in 'Language:':
					movie_languags=(h4.find_all('a'))
					for language in movie_languags:
						movie_Language.append(language.text)
		# print(movie_Country)
		# print(movie_Language)

		movie_time=suop.find('div',class_='title_wrapper')
		time_data=movie_time.find('div',class_='subtext')
		data_time=time_data.find('time').get_text().split()
		minutes=0
		for minet in data_time:
			if 'h' in minet:
				hours_to_movie=int(minet.strip('h'))*60
				# print(hours_to_movie)
			elif 'min' in minet:
				minutes+=int(minet.strip('min'))
		runtime=hours_to_movie+minutes
		# print(runtime)

		movie_details_dict = {'name':'','director':'',"country":'',
			"language":'',"poster_image_url":'',"bio":'',"runtime":'',"genre":''
			}
		movie_details_dict['cast']=scrape_movie_cast(movie_url)
		movie_details_dict['name']= film_tital
		movie_details_dict['director']= Directors_list
		movie_details_dict['country']= movie_Country
		movie_details_dict['language']= movie_Language
		movie_details_dict['poster_image_url']= movie_postar
		movie_details_dict['bio']= movie_bio
		movie_details_dict['runtime']= runtime
		movie_details_dict['genre']= Genre_list
		
		with open('IMD_data/'+file_name+'.json','w')as data:
			json.dump(movie_details_dict,data)

		return movie_details_dict

# movie_details_ten=scrape_movie_details(movie_list[4]['url'])
# pprint.pprint(movie_details_ten)


# Task_5


def get_movie_list_details(movies_list):
	movie_url_list=[]
	ten_movie_url=(movies_list[:250])
	for All_url in ten_movie_url:
		movie_url_li=scrape_movie_details(All_url['url'])
		movie_url_list.append(movie_url_li)
	return movie_url_list
get_movie_list_details=get_movie_list_details(movie_list)
pprint.pprint(get_movie_list_details)

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


# movie_10_language=analyse_movies_language(get_movie_list_details)
# pprint.pprint(movie_10_language)

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

# movie_10_director=analyse_movies_directors(get_movie_list_details)
# pprint.pprint(movie_10_director)


#Task_10

def analyse_language_and_directors(movies_list):
	Directors_All_movies={}
	for driector in movies_list:
		for one_driector in (driector['director']):
				Directors_All_movies[one_driector]={}
	# pprint.pprint(Directors_All_movies)

	for run in range(len(movies_list)):
		for Director_m in Directors_All_movies:
			if Director_m in movies_list[run]['director']:
				for film_language in movies_list[run]['language']:
					Directors_All_movies[Director_m][film_language]=0

	for run in range(len(movies_list)):
		for Director_m in Directors_All_movies:
			if Director_m in movies_list[run]['director']:
				for film_language in movies_list[run]['language']:
					Directors_All_movies[Director_m][film_language]+=1
	return(Directors_All_movies)


# Directors_All_movies_details=analyse_language_and_directors(get_movie_list_details)
# pprint.pprint(Directors_All_movies_details)

#Task_11

def analyse_movies_genre(movies_list):
	genres_list=[]
	for genres in movies_list:
		for one_genres in genres['genre']:
			if one_genres not in genres_list:
				genres_list.append(one_genres)
	total_value={}
	All_genres=[]
	for genres_ in movies_list:
		for one_genres_ in genres_['genre']:
			All_genres.append(one_genres_)
	for genre_1 in genres_list:
		total=All_genres.count(genre_1)
		total_value[genre_1]=total
	return(total_value)

# All_movie_genre=analyse_movies_genre(get_movie_list_details)
# pprint.pprint(All_movie_genre)


#Task_14

def analyse_co_actors(movies_list):
	analyse_actors={}
	for All_cast in movies_list:
		movie_IMDb=(All_cast['cast'][0]['imdb_id'])
		lead_actor=(All_cast['cast'][0]['name'])
		# print(movie_IMDb,"= ",lead_actor)
		analyse_actors[movie_IMDb]={'name':lead_actor,'frequent_co_actors':[]}
	# pprint.pprint(analyse_actors)
	for actors_key in analyse_actors:
		five_actors=[] 
		for All_film_cast in movies_list:
			only_cast=All_film_cast['cast']
			for Actor_imdb_id in All_film_cast['cast']:
				if actors_key == Actor_imdb_id['imdb_id']:
					index=1
					while index <= 5:
						five_actors.append(only_cast[index])
						index+=1
					for five_actors_list in five_actors:
						actor_id=(five_actors_list['imdb_id'])
						actor_name=(five_actors_list['name'])
						complet={"imdb_id":actor_id,"name":actor_name}
						return(analyse_actors[actors_key])
						# for All_analyse_actors in analyse_actors:
						# 	print(All_analyse_actors)
							# if actors_key == 


# movie_actors=analyse_co_actors(get_movie_list_details)
# pprint.pprint(movie_actors)

			#Task_15

def film_analyse_actors(movies_list):
	All_movies_details=[]
	new_list=[]
	analyse_actors_dict={}
	for cast_movie in movies_list:
		for All_movies_cast in cast_movie['cast']:
			new_list.append(All_movies_cast['name'])
	# return(new_list)
	for cast_dict in movies_list:
		cast_list=(cast_dict['cast'])
		index=0
		while index < 5:
			top_five_name=(cast_list[index]['name'])
			total_count=0
			# print(top_five_name)
			top_five_ID=(cast_list[index]['imdb_id'])
			# print(top_five_ID)
			index+=1
			for value in new_list:
				if top_five_name == value:
					total_count+=1
			analyse_actors_dict[top_five_ID]={'name':top_five_name,'num_movies':total_count}
		else:
			All_movies_details.append(analyse_actors_dict)
	return(All_movies_details)

# movie_analyse_actors=film_analyse_actors(get_movie_list_details)
# pprint.pprint(movie_analyse_actors)