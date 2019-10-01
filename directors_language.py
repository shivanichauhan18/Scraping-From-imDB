from Count_director import*
from Using_sleep_function import*

director_language={}
for dir in directors:
        language_list=[]
        for movie in movie_details:
                if dir in movie["director"]:
                        language_list.extend(movie["Languages"])

# this program for dublicate 
        dir_language=[]
        for language in language_list:
                if language not in dir_language:
                        dir_language.append(language)

#this program for counting language
        dictionary={}
        for language in dir_language:
                count=0
                for lang in language_list:
                    if language == lang:
                        count=count+1
                dictionary[language]=count

        director_language[dir]=dictionary
pprint(director_language)