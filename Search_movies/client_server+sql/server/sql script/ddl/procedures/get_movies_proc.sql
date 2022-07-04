CREATE PROCEDURE movies_db.get_movies(
	regex		VARCHAR(255),
    year_from	INT,
    year_to		INT,
    genres		VARCHAR(255),
    N			INT
)
WITH cte_number AS(

SELECT
	genre,
    title,
    year,
    ROUND(rating, 2) rating,
    RANK() OVER (
		PARTITION BY genre
        ORDER BY
			rating DESC,
			year DESC,
			title
	) nuber_rank
FROM
	movies
where
	(year >= year_from OR year_from IS NULL)
    AND (year <= year_to OR year_to IS NULL)
    AND (INSTR(genres, genre) > 0 OR genres IS NULL)
    AND (INSTR(title, regex) > 0 OR regex IS NULL)
)

SELECT genre,
		title,
		year,
		rating

FROM cte_number

WHERE 
	nuber_rank <= N OR N IS NULL