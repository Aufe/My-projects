import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--N', metavar='<number>', help="number of movies of each genre")
    return parser.parse_args()


def shuffle():
    genres_list = []
    movies_list = []
    key = None
    for row in sys.stdin:
        genre, movie = row.split("\t")
        title, year = movie.split("$$")
        if genre != key and key != None:
            genres_list.append((key, movies_list))
            movies_list = []
        movies_list.append((title, int(year)))
        key = genre
    genres_list.append((key, movies_list))
    return genres_list


def get_sort_movies(genres):
    for genre in genres:
        movies = genre[1]
        movies.sort(key=lambda x: (-x[1], x[0]))
    return genres


def reducer(key, value):
    args = get_args()
    n = int(args.N) if args.N else -1
    for movie in value[:n]:   
        yield key, movie
   

def main():
    genres = shuffle()
    for genres in get_sort_movies(genres):
        key, value = genres
        for genre, movie in reducer(key, value):
            title, year = movie
            print(f"{genre}, {title}, {year}")


if __name__ == "__main__":
    main()
