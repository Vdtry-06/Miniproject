import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the MySQL server
        conn = psycopg2.connect("dbname=miniproject user=root password=root")
        conn = psycopg2.connect(
            host="localhost",
            database="miniproject",
            user="root",
            password="root",
            port="3308"
        )
        with psycopg2.connect(**config) as conn:
            print('Connected to the MySQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)