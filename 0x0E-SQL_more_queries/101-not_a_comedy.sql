-- Just one select and could use Join
-- Just do it
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
     SELECT tv_shows.id
     FROM tv_shows
     JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
     JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
     WHERE tv_genres.name="Comedy"
     ORDER BY tv_shows.title ASC
) AS ti_comedy
ON tv_shows.id=ti_comedy.id
WHERE ti_comedy.id IS NULL
ORDER BY tv_shows.title;
