import argparse
import configparser
import mysql.connector


config = configparser.ConfigParser()
config.read('config.ini')
db = config['db']
host_name = db['host_name']
user_name = db['user_name']
user_password = db['user_password']
db_name = db['db_name']
delimetr = config['output']['delimetr']
get_movies_proc = config['procedures']['get_movies_proc']


def get_args():
    """
    Getting user's args.
    """
    parser = argparse.ArgumentParser(description="This program will search the movies by various filters.")

    parser.add_argument('--regexp', metavar='<title>', help="title filter")
    parser.add_argument('--year_from', metavar='<min_year>', help="min year filter")
    parser.add_argument('--year_to', metavar='<max_year>', help="max year filter")
    parser.add_argument('--genres', metavar='"<some_genre|some_genre>"', help="genre filter")
    parser.add_argument('--N', metavar='<number>', help="number of movies of each genre")

    return parser.parse_args()


def get_movies(args, cursor):
    """
    Getting final movies.
    """
    regexp = args.regexp
    year_from = args.year_from
    year_to = args.year_to
    genres = args.genres
    N = args.N
    cursor.callproc(get_movies_proc, (regexp, year_from, year_to, genres, N))


def show_movies(cursor):
    """
    Showing movies to user.
    """
    print('genre', 'title', 'year', 'rating', sep=delimetr)
    for movies in cursor.stored_results():
        for movie in movies.fetchall():
            movie = f'{delimetr}'.join(map(str, movie))
            print(movie)


def create_connection(host_name, user_name, user_password, db_name):
    """
    Connecting to MySQL server.
    """
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = db_name
    )
    return connection



def main():
    args = get_args()
    connection = create_connection(host_name, user_name, user_password, db_name)
    cursor = connection.cursor()
    get_movies(args, cursor)
    show_movies(cursor)

    

if __name__ == "__main__":
    main()