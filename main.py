import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import psycopg2
from db import Database


database_connection = Database()

# URL of the page to scrape
url = 'https://www.goodnewsnetwork.org/category/news/world/?filter_by=popular'

with Database() as database_connection:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the article links
        articles = soup.find_all('h3', class_='entry-title')
        
        # Extract the links from the articles
        links = []
        for article in articles:
            link = article.find('a', href=True)
            if link:
                links.append(link['href'])
        
        # Print the extracted links
        for link in links:
            database_connection.save_data(link)
            print(link)
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')
