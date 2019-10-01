from movie_list_details import movies_detail
from pprint import pprint


def get_languages(movies_list):
        languages=[]
        for movie in movies_list:
                languages.extend(movie["Languages"])
        return languages
language_list=get_languages(movies_detail)


def removing_duplicate_language(language_list):
        languages=[]
        for i in language_list:
                if i not in languages:
                        languages.append(i)
        return languages
duplicate_list=removing_duplicate_language(language_list)


def analyse_movies_language(language_list,list):
        counting_language={}
        for language in language_list:
                count_language=0
                for particular_language in list:
                        if language == particular_language:
                                count_language=count_language+1
                counting_language[language]=count_language
        return counting_language
movie_languages=analyse_movies_language(duplicate_list,language_list)
pprint(movie_languages)
