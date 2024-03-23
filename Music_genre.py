#создаем таблицу "Music_genre" с атрибутами id и названием жанра
CREATE TABLE IF NOT EXISTS Music_genre(
    id SERIAL PRIMARY KEY,
    genre VARCHAR(40) NOT NULL
)

#создаем таблицу "Artist" с id и именем(псевдонимом)
CREATE TABLE IF NOT EXISTS Artist(
    id SERIAL PRIMARY KEY,
    name VARCHAR(60) NOT NULL
)

#создаем промужуточную таблицу "Artist_Genre" в которой укажем исполнителей и их жанры
CREATE TABLE IF NOT EXISTS Artist_Genre(
    genre_id INTEGER NOT NULL REFERENCES Music_genre(id),
    artist_id INTEGER NOT NULL REFERENCES Artist(id),
    CONSTRAINT pk PRIMARY KEY (music_id, artist_id)
)

#создадим таблицу в которой укажем альбомы исполнителей
CREATE TABLE IF NOT EXISTS Album(
    id SERIAL PRIMARY KEY,
    album_name VARCHAR(60) NOT NULL
    release_year INTEGER NOT NULL
)

#теперь создадим промежуточную таблицу которая содержит исполинителей и их алюбомы с годом выпуска
CREATE TABLE IF NOT EXISTS Artist_Album(
    id SERIAL PRIMARY KEY
    artist_id SERIAL NOT NULL REFERENCES Artist(id),
    album_id SERIAL NOT NULL REFERENCES Album(id)
)

#в данной таблице будут храниться треки и их длительность и указано к каким альбомам они приндадлежат
CREATE TABLE IF NOT EXISTS Track(
    id SERIAL PRIMARY KEY,
    album_id SERIAL NOT NULL REFERENCES Album(id),
    track_name VARCHAR(60) NOT NULL,
    lenght VARCHAR(20) NOT NULL
)

#данная промежуточная таблица будет сборником, в которой хранятся треки и альбом к которому они принадлежат
CREATE TABLE IF NOT EXISTS Collection(
    id SERIAL PRIMARY KEY,
    collection_name VARCHAR(60) NOT NULL,
    release_year INTEGER NOT NULL,
    track_id SERIAL NOT NULL REFERENCES Track(id),
)