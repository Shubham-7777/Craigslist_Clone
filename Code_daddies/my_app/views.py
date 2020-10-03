from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
import re

BASE_CRAIGSLIST_URL = 'https://ahmedabad.craigslist.org/search/sss?query={}'

BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


# Create your views here.


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get("search")
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")
    full_post = soup.find_all('li', {'class': 'result-row'})

    final_post = []

    for post in full_post:
        post_title = post.find('a', {'class': 'result-title'}).text
        post_link = post.find('a').get('href')
        if post.find('a', {'class': 'result-image'}).get('data-ids'):
            image_id = post.find('a', {'class': 'result-image gallery'}).get('data-ids').split(',')[0].split(':')[1]
        else:
            image_id = 'https://craigslist.org/images/peace.jpg'

        final_image_post = BASE_IMAGE_URL.format(image_id)

        """.split(':')[1]"""

        if post.find('span', {'class': 'result-price'}):
            post_price = post.find('span', {'class': 'result-price'}).text
        else:
            post_price = "N/A"

        final_post.append((post_title, post_price, post_link,final_image_post))

    stuff_for_frontend = {
        'search': search,
        'final_post': final_post,

    }
    return render(request, "my_app/new_search.html", stuff_for_frontend)


""" else:
    post_image_url = 'https://craigslist.org/images/peace.jpg'
    final_postings.append((post_title, post_url, post_price, post_image_url))
a = soup.find_all('a', {'class': 'result-title'})
    b = soup.find_all('span', {'class': 'result-price'})
    c = soup.find_all('span', {'class': 'result-price'})

    print(a[0].get('href'))
    print(a[0].text)
"""
"""
    for i in a:
        product_titles = i.text
        print(product_titles)
    for x in b:
        product_prices = x.text
        print(product_prices)
"""
"""        post_title = post.find(class_= 'result-title').text
        post_link = post.find('a').get('href')
        if post.find(class_= 'result-price'):
            post_price = post.find(class_= 'result-price').text
        else:
            post_price = "N/A"""
