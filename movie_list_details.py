from pprint import pprint
from Top_Indian_Movie_List import*
from Movie_details import*



def Scrap_Movie_list_detail(movies):
        total_movies=[]
        for url in movies[:10]:
                movie_url=url["url"]
                particular_movie=Scrap_Movie_Detail(movie_url)
                movie_detail=particular_movie.copy()
                particular_movie.clear()
                total_movies.append(movie_detail)
        return total_movies
movies_detail=Scrap_Movie_list_detail(all_movies)
# pprint(movies_detail)