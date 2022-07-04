## Get-movies

This program will search the movies by various filters.

## Running

```
python get_movies.py [--regexp <title>] | [--year_from <min_year>] | [--year_to <max_year>] | [--genre "<some_genre|some_genre>"] [--N <number>] [--help]
```

## Command line options

```
-   --regexp    - title filter.
-   --year_from - min year filter.
-   --year_to   - max year filter.
-   --genre     - genre filter.
-   --N         - number of movies of each genre.
-   --help      - show message about options of program.
```

## Examples

```
python get_movies.py --regexp rock --genre "Action|Comedy"  (Will search the movies with title has "rock" and genres "Action" or "Comedy")

```