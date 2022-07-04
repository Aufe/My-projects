## Get-movies

This program will search the movies by various filters.

## Running

local
```
./get_movies_local.sh [-regexp <title>] [-year_from <min_year>] [-year_to <max_year>] [-genre "<some_genre|some_genre>"] [-N <number>]
```
with mapreduce
```
./get_movies_hadoop.sh [-regexp <title>] [-year_from <min_year>] [-year_to <max_year>] [-genre "<some_genre|some_genre>"] [-N <number>]
```

## Command line options

```
-   -regexp    - title filter.
-   -year_from - min year filter.
-   -year_to   - max year filter.
-   -genre     - genre filter.
-   -N         - number of movies of each genre.
```

## Examples

```
./get_movies_local.sh -regexp rock -genre "Action|Comedy"  (Will search the movies with title has "rock" and genres "Action" or "Comedy")

```
