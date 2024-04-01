# Заполняем таблицу Music_genre
INSERT INTO Music_genre(id, genre)
VALUES(1, 'Джаз')

INSERT INTO Music_genre(id, genre)
VALUES(2, 'Рок')

INSERT INTO Music_genre(id, genre)
VALUES(3, 'Хип-хоп')

INSERT INTO Music_genre(id, genre)
VALUES(4, 'Поп-музыка')

# Заполняем таблицу Artist
INSERT INTO Artist(id, artist)
VALUES(1, 'Луи Армстронг')

INSERT INTO Artist(id, artist)
VALUES(2, 'The Beatles')

INSERT INTO Artist(id, artist)
VALUES(3, 'Eminem')

INSERT INTO Artist(id, artist)
VALUES(4, 'Майкл Джексон')

# Заполняем таблицу Artist_Genre
INSERT INTO Artist_Genre(genre_id, artist_id)
VALUES(1, 1)

INSERT INTO Artist_Genre(genre_id, artist_id)
VALUES(2, 2)

INSERT INTO Artist_Genre(genre_id, artist_id)
VALUES(3, 3)

INSERT INTO Artist_Genre(genre_id, artist_id)
VALUES(4, 4)

# Заполняем таблицу Album
INSERT INTO Album(id, album_name, release_year)
VALUES(1, 'Porgy and Bess', 1957)

INSERT INTO Album(id, album_name, release_year)
VALUES(2, 'Satchmo in Style', 1959)

INSERT INTO Album(id, album_name, release_year)
VALUES(3, 'Yellow Submarine', 1969)

INSERT INTO Album(id, album_name, release_year)
VALUES(4, 'Abbey Road', 1969)

INSERT INTO Album(id, album_name, release_year)
VALUES(5, 'The Slim Shady LP', 1999)

INSERT INTO Album(id, album_name, release_year)
VALUES(6, 'Recovery', 2010)

INSERT INTO Album(id, album_name, release_year)
VALUES(7, 'Music to be murdered by', 2020)

INSERT INTO Album(id, album_name, release_year)
VALUES(8, 'Thriller', 1982)

#Заполняем таблцицу Artist_Album
INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(1, 1, 1)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(2, 2, 2)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(3, 2, 3)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(4, 2, 4)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(5, 3, 5)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(6, 3, 6)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(7, 3, 7)

INSERT INTO Artist_Album(id, artist_id, album_id)
VALUES(8, 4, 8)

#Заполняем таблицу Track
INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(1, 1, 'Summertime', 298)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(2, 1, 'Buzzard Song', 178)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(3, 2, 'Chloe', 186)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(4, 2, 'If', 206)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(5, 3, 'Hey Bulldog', 192)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(6, 3, 'All you need is Love', 227)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(7, 4, 'Come Together', 259)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(8, 4, 'Something', 182)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(8, 4, 'Something', 182)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(9, 5, 'Im Shady', 221)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(10, 5, 'My Name Is', 270)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(11, 6, 'On Fire', 213)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(12, 6, 'Not Afraid', 250)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(13, 7, 'Godzilla', 210)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(14, 8, 'Billie Jean', 293)

INSERT INTO Track(id, album_id, track_name, lenght)
VALUES(15, 8, 'Beat It', 251)

#Заполняем таблицу Collection
INSERT INTO Collection(id, collection_name, release_year)
VALUES(1, 'all_time_classic', 2020)

INSERT INTO Collection(id, collection_name, release_year)
VALUES(2, 'active', 2024)

INSERT INTO Collection(id, collection_name, release_year)
VALUES(3, '1980-2000', 2020)

INSERT INTO Collection(id, collection_name, release_year)
VALUES(4, 'Big Artist', 2022)

#Заполняем таблицу Collection_Track
INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(1, 1, 2)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(2, 1, 4)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(3, 2, 9)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(4, 2, 11)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(5, 2, 12)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(6, 3, 14)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(7, 3, 15)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(8, 4, 1)

INSERT INTO Collection_Track(id, id_collection, id_track)
VALUES(9, 4, 10)