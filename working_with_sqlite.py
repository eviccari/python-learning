import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    delete = "delete from movies"
    conn.execute(delete)
    conn.commit()

    insert = "insert into Movies values(?, ?, ?)"
    for movie in movies:
        conn.execute(insert, tuple(movie.values()))
    conn.commit()

    select = "select * from movies"
    cursor = conn.execute(select)

    movies = cursor.fetchall()
    [print(movie) for movie in movies]
