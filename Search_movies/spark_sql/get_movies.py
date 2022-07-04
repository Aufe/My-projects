#!usr/bin/env python3
from pyspark.sql import SparkSession
import argparse
from config import *


def get_args():
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


def get_movies(args, movies_file, ratings_file, spark, path_database):
    regexp = args.regexp if args.regexp is not None else ''
    year_from = int(args.year_from) if args.year_from is not None else 0
    year_to = int(args.year_to) if args.year_to is not None else 10**4
    genres = args.genres
    x = '>' if genres else '>='
    n = int(args.N) if args.N is not None else 10**8
    
    spark.sql(f"CREATE DATABASE IF NOT EXISTS moviesdb LOCATION '{path_database}'")

    spark.sql("USE moviesdb")

    spark.sql("DROP VIEW IF EXISTS movies")

    spark.sql(
        f'''
        CREATE TEMPORARY VIEW movies (
            movieId INT,
            title STRING,
            genres STRING
        )
        USING csv
        OPTIONS (
            HEADER=TRUE,
            PATH='{movies_file}'
        )
        '''
    )

    spark.sql("DROP VIEW IF EXISTS ratings")

    spark.sql(
        f'''
        CREATE TEMPORARY VIEW ratings (
            userId INT,
            movieId INT,
            rating FLOAT,
            timestam INT
        )
        USING csv
        OPTIONS (
            HEADER=TRUE,
            PATH='{ratings_file}'
        )
        '''
    )

    spark.sql("DROP TABLE IF EXISTS results")

    spark.sql(
        f'''
        CREATE TABLE results (
            genre STRING,
            title STRING,
            year INT,
            rating FLOAT
        )
        USING csv
        '''
    )

    title_split = '(.+)[ ][(](\\\d{4})[)]'

    spark.sql(
        f'''
        with rating_cte AS
        (
            SELECT movieId, AVG(rating) as rating
            FROM ratings
            GROUP BY movieId
        ),
        movies_cte AS
        (
            SELECT movieId,
                regexp_extract(title, '{title_split}', 1) AS title,
                regexp_extract(title,'{title_split}', 2) AS year,
                explode(split(genres, "[|]")) AS genre
            FROM movies
        ),   
        results_cte AS
        (
        SELECT movies_cte.genre AS genre,
            movies_cte.title AS title,
            movies_cte.year AS year,
            ROUND(rating_cte.rating, 2) AS rating,
            RANK() OVER
            (
                PARTITION BY genre
                ORDER BY rating DESC,
                            year DESC,
                            title
            ) number_rank
        FROM movies_cte
        INNER JOIN rating_cte ON movies_cte.movieId = rating_cte.movieId
        WHERE instr(title, '{regexp}') > 0 AND  
            year >= {year_from} AND
            year <= {year_to} AND
            genre <> '(no genres listed)' AND
            instr('{genres}', genre) {x} 0
        )
        INSERT INTO results        
        SELECT genre, title, year, rating
        FROM results_cte
        WHERE number_rank <= '{n}'
        '''
    )
    

def main():
    agrs = get_args()
    spark = SparkSession.builder.appName("Get movies").getOrCreate()
    get_movies(agrs, movies_file, ratings_file, spark, path_database)
    


if __name__ == "__main__":
    main()
