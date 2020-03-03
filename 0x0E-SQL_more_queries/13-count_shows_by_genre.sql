-- Just one select and could use Join
-- Just do it
SELECT tv_genres.name, COUNT(*) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
