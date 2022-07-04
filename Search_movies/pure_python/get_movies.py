import argparse
import re
from config import *


def get_args():
    parser = argparse.ArgumentParser(description="This program will search the movies by various filters.")

    parser.add_argument('--regexp', metavar='<title>', help='title title')
    parser.add_argument('--year_from', metavar='<min_year>', help='min year filter')
    parser.add_argument('--year_to', metavar='<max_year>', help='max year filter')
    parser.add_argument('--genres', metavar='"<some_genre|some_genre>"', help='genre filter')
    parser.add_argument('--N', metavar='<number>', help='number of movies of each genre')

    return parser.parse_args()


def parse_src_title(src_title):
    r_year = r" \(\d{4}\)"
    try:
        year = int(re.search(r_year, src_title)[0][2:-1])
        title = re.sub(r_year, "", src_title)
    except TypeError:
        title = src_title
        year = None
    return [title, year]


def parse_user_genres(args_genres):
    genres = args_genres.split("|")
    for genre in genres:
        genre.capitalize()
    return genres


def parse_src_genres(src_genres):
    genres = src_genres.split("|")
    return genres


def get_movie_rating():
    with open(file_rating) as ratings:
        rating_dict = {}
        not_sort_all_ratings = ratings.read().split('\n')
        for row in not_sort_all_ratings[1:-1]:
            row_sp = row.split(',')
            movie_id, rating = row_sp[1], float(row_sp[2])
            if movie_id not in rating_dict:
                vote = 1
                rating_dict[movie_id] = (rating, vote)
            else:
                current_rating, current_vote = rating_dict[movie_id]
                rating += current_rating
                vote = current_vote + 1
                rating_dict[movie_id] = (rating, vote)
        
        return rating_dict


def add_movie_to_movies_dict(movies_dict, genre, movie):
    if genre not in movies_dict:
        movies_dict[genre] = []
        movies_dict[genre].append(movie)
    else:
        movies_dict[genre].append(movie)
    return movies_dict


def get_filtered_movies(args, rating_dict):
    with open(file_movies) as movies:
        not_sort_all_movies = movies.read().split('\n')
        movies_dict = {}
        if args.genres:
            genres_user = parse_user_genres(args.genres)
        for movie in not_sort_all_movies[1:-1]:
            r_movie_split = r'^(\d+),(".*"|.+),(\S+)$'
            movie = re.split(r_movie_split, movie)
            try:
                movie_id, src_title, src_genres = movie[1], movie[2], movie[3]
            except IndexError:
                continue
            title, year = parse_src_title(src_title)
            if not year:
                continue
            if args.regexp and args.regexp.lower() not in title.lower():
                continue
            if args.year_from and int(args.year_from) > year:
                continue
            if args.year_to and int(args.year_to) < year:
                continue
            if movie_id not in rating_dict:
                continue
            sum_ratings, vote = rating_dict[movie_id]
            rating = round(sum_ratings / vote, 4)
            if not rating:
                continue
            genres = parse_src_genres(src_genres)
            movie = [title, year, rating]
            if args.genres:
                for genre in genres:
                    if genre in genres_user:
                        movies_dict = add_movie_to_movies_dict(movies_dict, genre, movie)
            else:
                for genre in genres:
                    movies_dict = add_movie_to_movies_dict(movies_dict, genre, movie)

        return movies_dict


def sort_genres_movies(movies_dict):
    genres_movies = list(movies_dict.keys())
    genres_movies.sort()
    return genres_movies


def sort_movies(movies):
    sorted_movie = sorted(movies, key=lambda x: (-x[2], -x[1], x[0]))
    return sorted_movie


def print_filtered_movies(movies_dict, genres_movies, n):
    print("genre", "title", "year", "rating", sep=';')
    films_number = int(n) if n else -1 
    for genre in genres_movies:
        sorted_movies = sort_movies(movies_dict[genre])
        for film in sorted_movies[:films_number]:
            title, year, rating = film
            print(genre, title, year, rating, sep=';')


def main():
    args = get_args()
    rating_dict = get_movie_rating()
    movies_dict = get_filtered_movies(args, rating_dict)
    genres_movies = sort_genres_movies(movies_dict)
    print_filtered_movies(movies_dict, genres_movies, args.N)


if __name__ == "__main__":
    main()
    