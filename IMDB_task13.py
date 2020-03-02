from IMDB_task12 import All_movie_cast
from pprint import pprint
import os ,json
files=os.listdir("./IMD_data")
files_count = 0
for file_name in files:
    if os.path.exists('IMD_data/'+file_name):
        with open('IMD_data/'+file_name,'r')as file:
            information = json.load(file)
            information['cast']=All_movie_cast[files_count]
            pprint(information)

            with open('IMD_data/'+file_name,'w')as data:
                json.dump(information,data)

            files_count+=1
    else:
        print("Error")
