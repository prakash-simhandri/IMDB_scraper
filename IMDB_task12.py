from IMDB_task1 import movie_list
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
# Task 12
def scrape_movie_cast(movie_caste_url):
    All_movies_cast_list = []
    count=0
    for caste_url in movie_caste_url:
        M_caste_url=caste_url['url']
        ID=''
        for _id in M_caste_url[27:]:
            if '/' not in _id:
                ID+=_id
            else:
                break
        film_name = ID

        movie_caste=requests.get(M_caste_url)
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
                All_movies_cast_list.append(casts_list)

                # print(casts_list)

                count+=1
                print(count)
    return(All_movies_cast_list)
        

All_movie_cast=scrape_movie_cast(movie_list)
# pprint(All_movie_cast)