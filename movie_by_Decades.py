from pprint import pprint
from Top_Indian_movies_by_year import years_data

sorted_year=years_data["sort_list"]
years_data=years_data["years_group"]

def group_by_decade(years,movie_group_of_year):
    movies_by_decade={}

    for year in movie_group_of_year:
        years_list=[]
        mod=year%10
        decade_year=year-mod
        range_year=decade_year+10
        for j in range(decade_year,range_year):
            if j in movie_group_of_year:
                years_list.extend(years[j])
        movies_by_decade[decade_year]=years_list
    return movies_by_decade

movieDecades=group_by_decade(years_data,sorted_year)
pprint(movieDecades)