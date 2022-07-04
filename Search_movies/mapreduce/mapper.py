import sys
import re
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="This program will search the movies by various filters.")

    parser.add_argument('--regexp',
                        metavar='<title>',
                        help="title filter")
    parser.add_argument('--year_from',
                        metavar='<min_year>',
                        help="min year filter")
    parser.add_argument('--year_to',
                        metavar='<max_year>',
                        help="max year filter")
    parser.add_argument('--genres',
                        metavar='"<some_genre|some_genre>"',
                        help="genre filter")
    return parser.parse_args()


def row_split(row):
    try:
        r_line = r'(\d+),(".*"|.+),(.+)'
        movie_src = list(filter(bool, re.split(r_line, row)))
        title_year = movie_src[1]
        r_year = r'\s\(\d{4}\)'
        year = re.search(r_year, title_year)
        if year is None:
            return None
        year = year[0][2:-1]
        title = re.sub(r_year, '', title_year)
        genres = movie_src[2]
        if genres == "(no genres listed)":
            return None
        return [genres, title, year]
    except Exception:
        return None


def parse_user_genres(args_genres):
    genres = args_genres.split("|")
    return genres


def get_sort_movies(args, row):
    row = row_split(row)
    if row:
        genres, title, year = row
        filter = True
        while filter == True:
            if args.regexp and args.regexp.lower() not in title.lower():
                filter = False
                continue
            if args.year_from and int(args.year_from) > int(year):
                filter = False
                continue
            if args.year_to and int(args.year_from) < int(year):
                filter = False
                continue
            genres = genres.split('|')
            if args.genres:
                genres_user = parse_user_genres(args.genres)
                for genre in genres:
                    if genre in genres_user:
                        yield genre, title, year
                filter = False
            else:
                for genre in genres:
                    yield genre, title, year
                filter = False


def mapper(rows):
    args = get_args()
    for row in rows:
        for genre, title, year in get_sort_movies(args, row.rstrip()):
            key = genre
            value = f"{title}$${year}"
            yield key, value


def main():
    for key, value in mapper(sys.stdin):
        print(f"{key}\t{value}")


if __name__ == "__main__":
    main()
