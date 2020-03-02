from IMDB_task4 import scrape_movie_details
from IMDB_task1 import movie_list
from pprint import pprint
import os.path,json,time,random
# Task 8 and 9
timer = random.randint(1,3)
def movies_json():
    all_movies_dicts=[]
    for all_movies in movie_list:
        movie_url = all_movies['url']
        ID=''
        for _id in movie_url[27:]:
            if '/' not in _id:
                ID+=_id
            else:
                break
        file_name = ID
        if os.path.exists('IMD_data/'+file_name+'.json'):
            with open('IMD_data/'+file_name+'.json',"r")as open_file:
                data = json.load(open_file)
                all_movies_dicts.append(data)
                # pprint(data)
        else:
            time.sleep(timer)
            movie_details_dict=scrape_movie_details(movie_url)

            with open('IMD_data/'+file_name+'.json','w')as data:
                json.dump(movie_details_dict,data)
    return all_movies_dicts

Movies_Dict=movies_json()