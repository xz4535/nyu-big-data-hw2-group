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
    
    # Question 1:Which tracks (ids and names) have a lyricist whose name begins with "W"?
    print('Question 1:')
    
    # implement your solution to q1
    
    print('---')
    
    # Question 2:What are the values that can be taken by the track.track_explicit field?
    print('Question 2:')
    
    # implement your solution to q2
    
    print('---')
    
    # Question 3:Which track (id and title) has the most listens?
    print('Question 3:')
    
    # implement your solution to q3
    
    print('---')
    
    # Question 4:How many artists have "related projects"?
    print('Question 4:')
    
    # implement your solution to q4
    
    print('---')
    
    # Question 5:Which non-null language codes have exactly 4 tracks?
    print('Question 5:')
    
    # implement your solution to q5
    
    print('---')
    
    # Question 6:How many tracks are by artists known to be active only within the 1990s?
    print('Question 6:')
    
    # implement your solution to q6
    
    print('---')
    
    # Question 7:Which three artists have worked with the largest number of distinct album producers?
    print('Question 7:')
    
    # implement your solution to q7
    
    print('---')
    
    # Question 8:Which track (include id, title, and artist name) has the largest difference between the number of album listens and track listens?
    print('Question 8:')
    
    # implement your solution to q8
    
    print('---')
