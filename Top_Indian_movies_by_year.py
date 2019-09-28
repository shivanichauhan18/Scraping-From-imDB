from pprint import pprint
from Top_Indian_Movie_List import*

def getMoviesYearList(total_movies):
    years=[]
    for index in total_movies:
        movie_year=index["year"]
        if movie_year not in years:
            years.append(movie_year)
    return years
years_list=getMoviesYearList(all_movies)

def group_by_year(movies,years_list):
    years={}
    for year in years_list:
        particular_year=[]
        for particularYear in movies:
            if year == particularYear["year"]:
                particular_year.append(particularYear)
        years[year]=particular_year

    return years
yearsDetail=group_by_year(all_movies,years_list)
pprint(yearsDetail)

def data_list(sorted_list,group_of_year):
    data={}
    data["sort_list"]=sorted_list
    data["years_group"]=group_of_year
    return data
years_data=data_list(years_list,yearsDetail)
# pprint(years_data)
