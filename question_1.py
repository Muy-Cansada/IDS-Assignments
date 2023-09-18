# -*- coding: utf-8 -*-
"""Question#1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19kJ8cysRT2PuiZIdCGl16NbQdiek3fQq
"""

# 18-09-2023
# CSC461 – Assignment1 – Web Scraping
# Hamna Shahbaz
# Fa21-bse-048
# In question number one i will be extracting movie titles and ratings by using imdb URLs through BeautifulSoup Library.
# Result: I was not able to achieve proper results because of inexperience in the syntax of a new language and relatively new concepts. I also couldn't
# export the data into an excel spreadsheet
import requests
import time
from bs4 import BeautifulSoup

urls = [
    "https://www.imdb.com/title/tt8946378/?ref_=fn_al_tt_1",
    "https://www.imdb.com/title/tt8523042/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_vagabond",
    "https://www.imdb.com/title/tt2560140/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_Attac",
    "https://www.imdb.com/title/tt5323662/?ref_=nv_sr_srsg_1_tt_7_nm_0_q_a%2520silent%2520",
    "https://www.imdb.com/title/tt7236034/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_i%2520want%2520to%2520eat%2520"
    ]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
responses = []
soups = []
for url in urls:
  response = requests.get(url, headers=headers)
  responses.append(response)
  time.sleep(1)

  soup = BeautifulSoup(response.content, 'html5lib')
  soups.append(soup)

movie_titles = []
movie_ratings = []

for soup in soups:
  movie_title = soup.find('span', class_="sc-afe43def-1 fDTGTb")
  movie_rating = soup.find('span', class_="sc-bde20123-1 iZlgcd")
  movie_titles.append(movie_title)
  movie_ratings.append(movie_rating)

for i in range(len(urls)):
    print(f"URL: {urls[i]}")
    print(f"Movie Title: {movie_title}")
    print(f"Movie Rating: {movie_rating}")
    print()