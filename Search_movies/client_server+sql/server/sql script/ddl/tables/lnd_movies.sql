USE lnd_db;

DROP TABLE IF EXISTS lnd_movies;

CREATE TABLE lnd_movies (
    lnd_movies_id   INT             NOT NULL    AUTO_INCREMENT,
    movie_id        VARCHAR(10),
    title           VARCHAR(255),
    genres          VARCHAR(255),

    CONSTRAINT PK_lnd_movies PRIMARY KEY (lnd_movies_id)
);