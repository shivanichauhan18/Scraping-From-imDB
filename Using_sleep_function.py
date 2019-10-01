from pprint import pprint
from Top_Indian_Movie_List import*
from Movie_details import*
import random
import time
import os.path

def writting_data(fileName,scrap_data):
    with open (fileName,"w") as files:
        dumps_file=json.dumps(scrap_data)
        files.write(dumps_file)

def read_scrap_data(fileName):
    with open (fileName,"r") as Rdata:
        read_data=Rdata.read()
        load_data=json.loads(read_data)
    return load_data

def Scrap_Movie_list_detail(movies):
    count=0
    total_movie=[]
    for movies_link in movies:
        url=movies_link["url"]
        spliting=url.split("/")
        get_id=spliting[4]
        fileName="movies_detail/"+get_id+".json"

        if os.path.exists(fileName):
            reading=read_scrap_data(fileName)
            print ("----------------------------------------------")
            pprint(reading)
            total_movie.append(reading)
        else:
            movie_detail=Scrap_Movie_Detail(url)
            writtingFile=writting_data(fileName,movie_detail)
            print ("writting data")
            pprint(movie_detail)
            random_num=random.randint(1,3)
            time.sleep(random_num)
    return total_movie
        
movie_details=Scrap_Movie_list_detail(all_movies)
pprint(movie_details)