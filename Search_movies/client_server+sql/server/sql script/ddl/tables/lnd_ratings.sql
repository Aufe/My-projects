USE lnd_db;

DROP TABLE IF EXISTS lnd_ratings;

CREATE TABLE lnd_ratings (
    lnd_ratings_id  INT             NOT NULL    AUTO_INCREMENT,
    user_id         VARCHAR(10),
    movie_id        VARCHAR(10),
    rating          VARCHAR(10),
    timestamt       VARCHAR(20),

    CONSTRAINT PK_lnd_ratings   PRIMARY KEY (lnd_ratings_id)
);