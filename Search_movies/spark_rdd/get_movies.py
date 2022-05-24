#!usr/bin/env python3
from pyspark import SparkConf
from pyspark import SparkContext
import re
import argparse
from config import *


def get_args():
     '''
     Get user's arguments.
     '''
     parser = argparse.ArgumentParser()

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
     parser.add_argument('--N',
                         metavar='<number>',
                         help="number of movies of each genre")

     return parser.parse_args()


def split_rdd_movies(one_movie):
     '''
     Split src movies on title, year and genres.
     '''
     try:
          r = r'(\d+),\"?(.+)[ ]\((\d{4})\)\"?,(.+)'
          one_movie = re.split(r, one_movie)
          one_movie = list(filter(bool, one_movie))
          movie_id, title, year, genres = one_movie
          if genres is not "(no genres listed)":
               genres_list = genres.split('|')
               return [(int(movie_id), (title, int(year), genre)) for genre in genres_list]
     except:
          pass


def split_rdd_ratings(one_vote):
     '''
     Split row of src rating on movieId and rating.
     '''
     try:
          _, movie_id, rating, _ = one_vote.split(',')
          return (int(movie_id), float(rating))
     except:
          pass


def get_average_rating(list):
     '''
     Get avg rating on movie.
     '''
     return sum(list) / len(list)


def get_out_format(rdd, header, sc):
     '''
     Transform our rdd in csv like format.
     '''
     rdd_header = sc.parallelize([header])
     rdd = rdd.map(lambda x: ','.join(map(str, x)))
     rdd_out = rdd_header.union(rdd)
     return rdd_out


def get_movies(args, sc, movies_file, ratings_file):
     '''
     Get movies_rdd with user parameters.
     '''
     rdd_movies = sc.textFile(movies_file)
     rdd_ratings = sc.textFile(ratings_file)

     rdd_movies_split = rdd_movies.map(split_rdd_movies).filter(lambda x: x)
     rdd_ratings_split = rdd_ratings.map(split_rdd_ratings).filter(lambda x: x).groupByKey().mapValues(get_average_rating)

     rdd_filtred_movies = rdd_movies_split.flatMap(lambda y: filter(lambda x: bool(True if args.regexp is None else (re.search(str(args.regexp), x[1][0], re.IGNORECASE)) \
                         and (args.year_from if args.year_from is not None else True) <= x[1][1] \
                         and x[1][1] <= (args.year_to if args.year_to is not None else True) \
                         and any(map(lambda z: z in x[1][2], str(args.genres).split('|'))) if args.genres is not None else True), y))
     
     rdd_filtred_movies_with_ratings = rdd_filtred_movies.join(rdd_ratings_split) \
                                                         .mapValues(lambda x: (x[0][2], x[0][0], x[0][1], x[1])) \
                                                         .map(lambda x: x[1]) \
                                                         .sortBy(lambda x: (-x[3], -x[2], x[1])) \
                                                         .groupBy(lambda x: x[0]).flatMap(lambda x: tuple(x[1])[:args.N]).sortBy(lambda x: x[0])
               
     return rdd_filtred_movies_with_ratings


def main():
     args = get_args()
     
     sconf = SparkConf()
     sc = SparkContext(conf=sconf)
     rdd = get_movies(args, sc, movies_file, ratings_file)

     get_out_format(rdd, header, sc).saveAsTextFile(path)


if __name__ == "__main__":
     main()