import re
import configparser
import mysql.connector


config = configparser.ConfigParser()
config.read('config.ini')
db = config['db']
host_name = db['host_name']
user_name = db['user_name']
user_password = db['user_password']
data_path = config['data_path']
file_movies = data_path['file_movies']
file_rating = data_path['file_rating']
sql_path = config['sql_path']
lnd_db = sql_path['lnd_db']
lnd_movies = sql_path['lnd_movies']
lnd_ratings = sql_path['lnd_ratings']
movies_db = sql_path['movies_db']
movies = sql_path['movies']
load_lnd_movies = sql_path['load_lnd_movies']
load_lnd_ratings = sql_path['load_lnd_ratings']
load_movies = sql_path['load_movies']
start_get_movies_proc = sql_path['start_get_movies_proc']


def create_connection(host_name, user_name, user_password):
    """
    Connecting to MySQL server.
    """
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = user_password
    )
    return connection


def execute_query(connection, sql_file):
    """
    Execution of SQL query.
    """
    cursor = connection.cursor()
    with open(sql_file, 'r') as sql_file:
        query = sql_file.read()
        multi_query = cursor.execute(query, multi=True)
        for query in multi_query:
            query
        connection.commit()


def execute_load_lnd_table(connection, sql_file, value):
    """
    Loading data into a SQL table.
    """
    cursor = connection.cursor()
    with open(sql_file, 'r') as sql_file:
        querys = sql_file.read()
        query = querys.split(';')
        use_db_query = query[0]
        load_table = query[1]
        cursor.execute(use_db_query)
        cursor.executemany(load_table, value)
        connection.commit()


def get_lnd_movies():
    """
    Getting array of src movies.
    """
    with open(file_movies) as movie_file:
        movies = movie_file.read().split('\n')
        r_movie_split = r'(\d+),(".*"|.+),(.+)'
        movies =  [tuple(re.split(r_movie_split, el)[1:-1]) for el in movies[1:-1]]
        return movies


def get_lnd_ratings():
    """
    Getting array of src ratings.
    """
    with open(file_rating) as ratings_file:
        ratings = ratings_file.read().split('\n')
        ratings = [tuple(el.split(',')) for el in ratings[1:-1]]
        return ratings


def main():
    connection = create_connection(host_name, user_name, user_password)
    execute_query(connection, lnd_db)                                               #create database lnd_db
    execute_query(connection, lnd_movies)                                           #create table lnd_movies
    execute_query(connection, lnd_ratings)                                          #create table lnd_ratings
    execute_query(connection, movies_db)                                            #create database movies_db
    execute_query(connection, movies)                                               #create table movies
    execute_load_lnd_table(connection, load_lnd_movies, get_lnd_movies())           #load table lnd_movies
    execute_load_lnd_table(connection, load_lnd_ratings, get_lnd_ratings())         #load table lnd_ratigs
    execute_query(connection, load_movies)                                          #load table movies
    execute_query(connection, start_get_movies_proc)                                #start get_movies procedure
    

if __name__ == "__main__":
    main()