USE lnd_db;

INSERT INTO lnd_movies (movie_id, title, genres)
VALUES (%s, %s, %s);