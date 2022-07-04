USE lnd_db;

DROP TABLE IF EXISTS numbers;

CREATE TABLE numbers (
  n INT PRIMARY KEY);

INSERT INTO numbers VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10);

INSERT INTO movies_db.movies(movie_id, title, year, rating, genre)

WITH cte_rating AS(
	SELECT
		movie_id,
		ROUND(SUM(rating) / COUNT(rating), 4) rating
	FROM
		lnd_ratings
	GROUP BY
		movie_id
)
SELECT
	movie_id,
	IF (REGEXP_SUBSTR(title, '[[:space:]][(][0-9]{4}[)]') IS NOT NULL, REPLACE(title, REGEXP_SUBSTR(lnd_movies.title, '[[:space:]][(][0-9]{4}[)]'), ''), title) title,
    SUBSTR(REGEXP_SUBSTR(title, '[(][0-9]{4}[)]'), 2, 4) year,
    rating,
	SUBSTRING_INDEX(SUBSTRING_INDEX(genres, '|', n), '|', -1) genre
	
FROM
	numbers INNER JOIN lnd_movies
	ON CHAR_LENGTH(genres) - CHAR_LENGTH(REPLACE(genres, '|', ''))>=n-1
    JOIN cte_rating USING (movie_id)
WHERE genres NOT LIKE "%no genre%" AND SUBSTR(REGEXP_SUBSTR(title, '[(][0-9]{4}[)]'), 2, 4) IS NOT NULL
ORDER BY
	movie_id, title, genre;

DROP TABLE IF EXISTS numbers;