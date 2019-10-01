from Using_sleep_function import*
from pprint import pprint

def get_genres(movies_detail):
    genre_list=[]
    for movie in movies_detail:
        genres=movie["genres"]
        genre_list.extend(genres)
    return genre_list
all_genres=get_genres(movie_details)
# pprint(all_genres)

def removing_duplicate_genres(genres):
    count_genre=[]
    for genre in genres:
        if genre not in count_genre:
            count_genre.append(genre)
    return count_genre
duplicate_genre=removing_duplicate_genres(all_genres)
# pprint(duplicate_genre)

genres={}
def analyse_movies_genre(total_genre,dupicates_genre):
    for genre in dupicates_genre:
        count=0
        for particular_genre in total_genre:
            if genre==particular_genre:
                count=count+1
        genres[genre]=count
    # pprint(genre)
    return genres
counting_genre = analyse_movies_genre(all_genres,duplicate_genre)
pprint(counting_genre)