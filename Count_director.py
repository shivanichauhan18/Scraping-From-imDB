from movie_list_details import movies_details
from pprint import pprint

def movies_directors(movies_list):
    total_dir=[]
    for index in movies_list:
        total_dir.extend(index["director"])
    return total_dir
total_director=movies_directors(movies_details)

def removing_duplicate_director(dir_list):
    director=[]
    for dir in dir_list:
        if dir not in director:
            director.append(dir)
    return director
directors=removing_duplicate_director(total_director)
# pprint(directors_list)
def analyse_movies_directors(single_dir,total_directors):
    dictionary={}
    for main_dir in single_dir:
        count=0
        for campare_dir in total_directors:
            if main_dir == campare_dir:
                count=count+1
        dictionary[main_dir]=count
    pprint (dictionary)
pprint(analyse_movies_directors(directors,total_director))