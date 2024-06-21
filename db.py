from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

class Database:
    def __init__(self):
        # Establish a database connection and create a cursor
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create the table if it does not exist
        table_creation = '''
        CREATE TABLE IF NOT EXISTS url(
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL UNIQUE
        )
        '''
        self.cursor.execute(table_creation)
        self.connection.commit()

    def save_data(self, url):
        # Insert the URL into the database, ignoring duplicates
        insert_query = "INSERT INTO url (url) VALUES (%s) ON CONFLICT (url) DO NOTHING"
        self.cursor.execute(insert_query, (url,))
        self.connection.commit()

    def close(self):
        # Close the cursor and the connection
        self.cursor.close()
        self.connection.close()

    # Adding context management methods for better resource management
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()