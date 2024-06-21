# Narya
Narya is a simple web scraper that fetches popular news articles from the Good News Network's World News section.

## Features
Scrapes the Good News Network's World News section for popular articles
Extracts the links of the articles
Stores the links in a PostgreSQL database
Requirements
Python 3.6+
PostgreSQL
Python libraries: requests, BeautifulSoup, psycopg2, python-dotenv

## Setup
Clone the repository:
Set up your PostgreSQL database and add the connection details to a .env file in the project root:
DB_NAME=your_database_name
DB_USER=your_username
DB_PASS=your_password
DB_HOST=your_host
DB_PORT=your_port

## Usage
Run the main script:
python main.py
This will scrape the Good News Network's World News section, extract the links of the popular articles, and store them in your PostgreSQL database.
