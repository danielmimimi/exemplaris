CREATE TABLE babe
(
    id        SERIAL,
    proc_name TEXT,
    date      DATE,
    result    TEXT,
    data      TEXT,
    PRIMARY KEY (id)
);

INSERT INTO babe(proc_name, "date", result, data)
VALUES ('Bitwolf', to_timestamp(1613579807000/1000)::date, 'joe', 'DuisBibendum.jpeg'),
       ('Otcom', to_timestamp(1620163521000/1000)::date, 'mama', 'VelNislDuis.xls'),
       ('Sonsig', to_timestamp(1642620047000/1000)::date, 'joe', 'AtFeugiatNon.mp3'),
       ('Latlux', to_timestamp(1598849712000/1000)::date, 'mama', 'EtUltrices.mp3'),
       ('Konklab', to_timestamp(1620494255000/1000)::date, 'joe', 'EtUltricesPosuere.avi');
