#Задание 2
#1. Название и продолжительность самого длительного трека
SELECT track_name, lenght
FROM Track
ORDER BY lenght DESC
LIMIT 1

#2 Название треков, продолжительность которых не менее 3,5 минут
SELECT track_name, lenght
FROM Track
WHERE lenght >= 210

#3 Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT collection_name, release_year
FROM Collection
WHERE release_year BETWEEN 2018 AND 2021

#4 Исполнители, чьё имя состоит из одного слова
SELECT artist
FROM Artist
WHERE name NOT LIKE '% %'

#5 Название треков, которые содержат слово «мой» или «my»
SELECT track_name
FROM Track
WHERE track_name LIKE '%My%' OR track_name like '%мой%'

#Задание 3
#1 Количество исполнителей в каждом жанре
SELECT genre_id, COUNT(artist_id)
FROM Artist_Genre
GROUP BY genre_id

#2 Количество треков, вошедших в альбомы 2019–2020 годов
select album_id, COUNT(track_name)
from track t
join album a on t.album_id = a.id
where release_year > 2018 and release_year < 2021
GROUP by t.album_id

#3 Средняя продолжительность треков по каждому альбому
select album_id, a.album_name, AVG(lenght)
from track t
join album a on t.album_id = a.id
GROUP BY t.album_id, a.album_name

#4 Все исполнители, которые не выпустили альбомы в 2020 году
select name, album_name, release_year
from artist_album aa
join artist a on a.id = aa.artist_id
join album al on al.id = aa.album_id
group by a.name, al.album_name, al.release_year
having al.release_year != 2020

#5 Названия сборников, в которых присутствует конкретный исполнитель ('Eminem')
select c.collection_name , ar.name, t.track_name
from collection c
join collection_track ct on ct.id_collection = c.id
join track t on t.id = ct.id_track
join album al on al.id = t.album_id
join artist_album aa on aa.album_id = al.id
join artist ar on ar.id = aa.artist_id
group by c.collection_name, ar.name, t.track_name
having ar.name = 'Eminem'

#Задание 4
#1 Названия альбомов, в которых присутствуют исполнители более чем одного жанра
select a.album_name, ar.name
from album a
join artist_album aa on aa.album_id = a.id
join artist ar on ar.id = aa.artist_id
join artist_genre ag on ag.artist_id = ar.id
join music_genre mg on mg.id = ag.genre_id
group by ar.name, a.album_name
having count(ag.genre_id) > 1

#2 Наименования треков, которые не входят в сборники
select t.track_name, ct.id_collection
from track t
left join collection_track ct on ct.id_track = t.id
group by ct.id_collection, t.track_name
order by ct.id_collection desc
limit 6

#3 Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько
select name, min(t.lenght)
from artist a
join artist_album aa on aa.artist_id = a.id
join album al on al.id = aa.album_id
join track t on t.album_id  = al.id
group by name
order by min(t.lenght)
limit 1

#4 Названия альбомов, содержащих наименьшее количество треков
select a.album_name, count(t.track_name)
from album a
join track t on t.album_id = a.id
group by a.album_name
order by count(t.track_name)
limit 1