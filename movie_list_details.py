from pprint import pprint
from Top_Indian_Movie_List import*
from Movie_details import*



def Scrap_Movie_list_detail(movies):
        total_movies=[]
        for url in movies[:10]:
                movie_url=url["url"]
                particular_movie=Scrap_Movie_Detail(movie_url)
                total_movies.append(particular_movie)
        pprint(total_movies)
movie_list_detail1=(Scrap_Movie_list_detail(all_movies)) 
pprint(movie_list_detail1)