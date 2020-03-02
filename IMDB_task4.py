from IMDB_task1 import movie_list
from pprint import pprint
import requests
from bs4 import BeautifulSoup

def scrape_movie_details(movie_url):
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
		movie_details_dict['name']= film_tital
		movie_details_dict['director']= Directors_list
		movie_details_dict['country']= movie_Country
		movie_details_dict['language']= movie_Language
		movie_details_dict['poster_image_url']= movie_postar
		movie_details_dict['bio']= movie_bio
		movie_details_dict['runtime']= runtime
		movie_details_dict['genre']= Genre_list
        
		return movie_details_dict

# movie_details_ten=scrape_movie_details(movie_list[4]['url'])
# pprint(movie_details_ten)