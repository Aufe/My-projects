USE movies_db;

DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    movies_id   INT             NOT NULL        AUTO_INCREMENT,
    movie_id    INT             NOT NULL,
    title       VARCHAR(255)    NOT NULL,
    year        INT             NOT NULL,
    rating      FLOAT(5,4)      NOT NULL,
    genre       VARCHAR(20)     NOT NULL,

    CONSTRAINT PK_movies PRIMARY KEY (movies_id)
);