import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
# from task12 import*

def getRequests(movie_url):
    res=requests.get(movie_url)
    return BeautifulSoup(res.text,"html.parser")

movie_details={}
def Scrap_language_and_country(imdb_data):
    for i in range(1):
        try:
            articleDiv=imdb_data.find("div",class_="article",id="titleDetails")
            txtDiv=articleDiv.find_all("div",class_="txt-block")
            language=[]
            for div in txtDiv[:5]:
                h4_data=div.find("h4",class_="inline").get_text()
                if h4_data == "Language:":
                    aTags=div.findAll("a")
                    for teg in aTags:
                        particular_language=teg.get_text()
                        language.append(particular_language)
                if h4_data == "Country:":
                    country=div.a.get_text()
        except AttributeError: 
            continue
    movie_details["Languages"]=language
    movie_details["country"]=country

def Scrap_movie_bio_and_director(imdb):
    bio_main_div=imdb.find("div",class_="plot_summary")
    bio_data=bio_main_div.find("div",class_="summary_text").get_text().strip()

    credits_div=bio_main_div.find("div",class_="credit_summary_item")
    a_tegs=credits_div.findAll("a")
    directors=[]  



    for teg in a_tegs:
        director_index=teg.get_text()
        directors.append(director_index)
        
    movie_details["director"]=directors
    movie_details["bio"]=bio_data
    
def Scrap_movie_headings(imdb):
    title_div=imdb.find("div",class_="title_wrapper")
    movie_name=title_div.h1.get_text()
    name_split=movie_name.split()
    name=" ".join(name_split[:-1])

    movie_runtime=imdb.find("div",class_="subtext").time["datetime"]
    time=" "     
    for i in movie_runtime:
        if i.isdigit():
            time=time+i
    runtime=int(time)

    subtext_div=imdb.find("div",class_="subtext").findAll("a")
    genres=[]
    for genre in subtext_div[:-1]:
        particular_genre=genre.get_text()
        genres.append(particular_genre)

    movie_details["genres"]=genres
    movie_details["name"]=name
    movie_details["runtime"]=runtime

def Scrap_Movie_Detail(movie_url):
    soup = getRequests(movie_url)  

    Scrap_language_and_country(soup)

    Scrap_movie_headings(soup)

    Scrap_movie_bio_and_director(soup)

    # caste=part_of_movie_cast_url(movie_url)
    # caste1=scrape_movie_cast(caste)

    # movie_details["cast"]=caste1
    
    poster_url=soup.find("div",class_="poster").img["src"]
    movie_details["poster_image_url"]=poster_url
    return movie_details
movie_url1="https://www.imdb.com/title/tt0066763/"
particular_movie_detail=Scrap_Movie_Detail(movie_url1)
# pprint(particular_movie_detail)
