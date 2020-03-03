-- Just one select and could use Join
-- Just do it
SELECT tv_genres.name
FROM tv_genres, tv_show_genres
WHERE tv_genres.id=tv_show_genres.genre_id AND tv_show_genres.show_id=(
      SELECT tv_shows.id
      FROM tv_shows
      WHERE tv_shows.title="Dexter")
-- tv_show_genres.genre_id=tv_genres.id)
ORDER BY tv_genres.name ASC;
