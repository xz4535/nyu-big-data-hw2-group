#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# USAGE:
#   python lab1_part2.py music_small.db

import sys
import sqlite3
import timeit


# The database file should be given as the first argument on the command line
# Please do not hard code the database file!
db_file = sys.argv[1]


# The query to be optimized is given here
# It finds all the artists (ids and names) for which all of their albums received at least 50K listens
MY_QUERY = """SELECT artist.id, artist.artist_name, MIN(album.album_listens) as listens
	      FROM artist
	      INNER JOIN track ON track.artist_id = artist.id
	      INNER JOIN album ON track.album_id = album.id
	      GROUP BY artist.id
	      HAVING listens >= 50000"""

NUM_ITERATIONS = 100

def run_my_query(conn):
    for row in conn.execute(MY_QUERY):
        pass
    

"""
1.original: (mean:0.062 best:0.012)
2.create index for each column in track and album.id and artist.id, not using any composite index: (mean: 0.052 best:0.010)
3.using composite index for artist.id & artist.artist_name: no faster than 2
4.(optimal)create composite index for track.artist_id & track.album_id based on 2: (mean: 0.048 best:0.009)
5.using composite index for both track table and album table: no faster than 4
6.add index for album.album_listens:no faster than 4
"""

# We connect to the database using
with sqlite3.connect(db_file) as conn:
    # We use a "cursor" to mark our place in the database.
    cursor = conn.cursor()

    # We could use multiple cursors to keep track of multiple
    # queries simultaneously.

    orig_time = timeit.repeat('run_my_query(conn)', globals=globals(), number=NUM_ITERATIONS)
    print("Before optimization:")

    print(f'Mean time: {sum(orig_time)/NUM_ITERATIONS:.3f} [seconds/query]')
    print(f'Best time: {min(orig_time)/NUM_ITERATIONS:.3f} [seconds/query]')

    # MAKE YOUR MODIFICATIONS TO THE DATABASE HERE

    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_art_alb_id
                   ON track (artist_id, album_id)""")
    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_art_id
                   ON artist (id)""")     
    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_alb_id
                   ON album (id)""")


    new_time = timeit.repeat('run_my_query(conn)', globals=globals(), number=NUM_ITERATIONS)
    print("After optimization:")

    print(f'Mean time: {sum(new_time)/NUM_ITERATIONS:.3f} [seconds/query]')
    print(f'Best time   : {min(new_time)/NUM_ITERATIONS:.3f} [seconds/query]')
    #then remove indexes to restore the database
    cursor.execute("""DROP INDEX idx_art_alb_id""")
    cursor.execute("""DROP INDEX idx_art_id""")
    cursor.execute("""DROP INDEX idx_alb_id""")
