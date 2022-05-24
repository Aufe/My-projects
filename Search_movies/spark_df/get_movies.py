#!usr/bin/env python3
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import pyspark.sql.types as t
import pyspark.sql.window as w
import argparse
from config import *


def get_args():
     parser = argparse.ArgumentParser()

     parser.add_argument('--regexp',
                        metavar='<title>',
                        nargs="+",
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


def get_movies(args, df_movies, df_ratings):
     regexp = ' '.join(args.regexp) if args.regexp is not None else ''
     year_from = int(args.year_from) if args.year_from is not None else 0
     year_to = int(args.year_to) if args.year_to is not None else 10**4
     genres = args.genres
     n = int(args.N) if args.N is not None else 10**8

     title_split = r'(.+)[ ]\((\d{4})\)'

     df_movies_splited = df_movies.select(
          'movieId',
          f.regexp_extract('title', title_split, 1).alias('title'),
          f.regexp_extract('title', title_split, 2).alias('year'),
          f.explode(f.split('genres', "[|]")).alias('genre')
          )    

     df_ratings_avg = df_ratings.groupBy('movieId').agg(f.avg('rating').alias('rating'))

     df_movies_ratings = df_movies_splited.join(df_ratings_avg, df_movies_splited.movieId == df_ratings_avg.movieId, 'inner')\
          .select(df_movies_splited.genre, df_movies_splited.title, df_movies_splited.year, df_ratings_avg.rating)

     def genre_filter(x):
          try:
               genres_list = genres.split('|')
          except AttributeError:
               return True
          if x not in genres_list:
               return False     
          return True

     filter_genre = f.udf(genre_filter, t.BooleanType())

     df_movies_ratings_filtered = df_movies_ratings.filter(
          (df_movies_ratings.title.rlike(regexp)) & \
          (df_movies_ratings.year >= year_from) & \
          (df_movies_ratings.year <= year_to) & \
          (filter_genre(df_movies_ratings.genre)) & \
          (df_movies_ratings.genre != '(no genres listed)')
          )

     window_genre = w.Window.partitionBy('genre').orderBy(f.col('rating').desc(), f.col('year').desc(), 'title')
     df=df_movies_ratings_filtered.withColumn('row', f.row_number().over(window_genre))

     df_result = df.filter(f.col('row') <= n).select('genre', 'title', 'year', f.round('rating', 2).alias('rating'))
     
     return df_result


def out_to_csv(df, path):
     df.write.options(header=True).csv(path)


def main():
     agrs = get_args()
     spark = SparkSession.builder.appName("Get movies").getOrCreate()
     df_movies = spark.read.options(header=True).csv(movies_file)
     df_ratings = spark.read.options(header=True).csv(ratings_file).select('movieId', f.col('rating').cast('float'))
     df_result = get_movies(agrs, df_movies, df_ratings)
     out_to_csv(df_result, path)



if __name__ == "__main__":
     main()



    