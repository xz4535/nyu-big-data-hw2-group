# !/usr/bin/env python
# -*- encoding: utf-8 -*-

# USAGE:
#   python lab1_part1.py music_small.db

import sys
import sqlite3


# The database file should be given as the first argument on the command line
# Please do not hard code the database file!
db_file = sys.argv[1]

# We connect to the database using 
with sqlite3.connect(db_file) as conn:
    # This query counts the number of artists who became active in 1990
    year = (1990,)
    for row in conn.execute('SELECT count(*) FROM artist WHERE artist_active_year_begin=?', year):
        # Since there is no grouping here, the aggregation is over all rows
        # and there will only be one output row from the query, which we can
        # print as follows:
        print('Tracks from {}: {}'.format(year[0], row[0]))
        
        # The [0] bits here tell us to pull the first column out of the 'year' tuple
        # and query results, respectively.

    # ADD YOUR CODE STARTING HERE
    
    # Question 1:
    print('Question 1:Which tracks (ids and names) have a lyricist whose name begins with "W"?')
    # implement your solution to q1
    for row in conn.execute("""SELECT track.id, track.track_lyricist 
                            FROM track 
                            WHERE track.track_lyricist LIKE 'W%'"""):
        track_id, track_name = row 
        print(f"Track ID: {track_id}, Track Name: {track_name}")
    print('---')

    
    # Question 2:
    print('Question 2:What are the values that can be taken by the track.track_explicit field?')
    # implement your solution to q2
    for a in conn.execute("SELECT DISTINCT track_explicit FROM track"):
            print(f"value:{a}")
    print('---')
    
    # Question 3:
    print('Question 3:Which track (id and title) has the most listens?')
    
    # implement your solution to 3
    for row in conn.execute("""SELECT track.id, track.track_title 
                            FROM track 
                            ORDER BY track_listens DESC LIMIT 1"""):
        track_id, track_name = row  # Unpacking the row into track_id and track_name
        print(f"Track ID: {track_id}, Track title: {track_name}")
    print('---')
    
    # Question 4:
    print('Question 4:How many artists have "related projects"?')
    
    # implement your solution to q4
    for row in conn.execute("""SELECT count(DISTINCT id) 
                            FROM artist 
                            WHERE artist_related_projects"""):
        print(f"Number:{row}")
    print('---')
    
    # Question 5:
    print('Question 5:Which non-null language codes have exactly 4 tracks?')
    
    # implement your solution to q5
    for row in conn.execute("""SELECT track_language_code 
                                FROM track 
                                WHERE track_language_code IS NOT NULL 
                                GROUP BY track_language_code
                                HAVING COUNT(*) = 4"""):
        print(f"language codes:{row}")
    print('---')
    
    # Question 6:
    print('Question 6:How many tracks are by artists known to be active only within the 1990s?')
    
    # implement your solution to q6 ???
    for row in conn.execute("""SELECT count(*)
                            FROM track
                            INNER JOIN artist ON artist.id = track.artist_id 
                            WHERE artist_active_year_begin = 1990
                            OR artist_active_year_end = 1990"""):
        print(f"number of track:{row}")
    print('---???')
    
    # Question 7:
    print('Question 7:Which three artists have worked with the largest number of distinct album producers?')
    
    # implement your solution to q7
    for row in conn.execute("""SELECT artist_name, count(DISTINCT album.album_producer)
                            FROM artist
                            JOIN track ON artist.id = track.artist_id 
                            LEFT JOIN album ON album.id = track.album_id
                            GROUP BY artist_id 
                            ORDER BY count(DISTINCT album.album_producer) DESC LIMIT 3"""):
        a,b = row
        print(f"artist:{a}, number of album producers:{b}")
    print('---')
    
    # Question 8:
    print('Question 8:Which track (include id, title, and artist name) has the largest difference between the number of album listens and track listens?')
    
    # implement your solution to q8
    for row in conn.execute("""SELECT track.id, track.track_title, artist.artist_name, ABS(album.album_listens-track.track_listens) AS diff
                            FROM track
                            JOIN artist ON artist.id = track.artist_id 
                            LEFT JOIN album ON album.id = track.album_id
                            ORDER BY diff DESC LIMIT 1"""):
        a,b,c,d = row
        print(f"id:{a}, title:{b}, artist name:{c}, difference:{d}")
    print('---')
