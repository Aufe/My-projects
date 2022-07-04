USE lnd_db;

INSERT INTO lnd_ratings (`user_id`, movie_id, rating, timestamt)
VALUES (%s, %s, %s, %s);