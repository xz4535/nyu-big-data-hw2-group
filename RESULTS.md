# Homework 1 results

Your name: 

## Part 1
Paste the results of your queries for each question given in the README below:

1.<br>Track ID: 22344, Track Name: Wesley Willis
<br>Track ID: 66084, Track Name: Wayne Myers
<br>Track ID: 66096, Track Name: Wayne Myers

2.
<br>value:(None,)
<br>value:('Radio-Safe',)
<br>value:('Radio-Unsafe',)
<br>value:('Adults-Only',)
3.

4.

5.

6.

7.

8.

## Part 2

- Execution time before optimization: (mean: 0.062, best:0.012)
- Execution time after optimization: (mean:0.048, best:0.009)

- Briefly describe how you optimized for this query:
<ul>
I have created a composite index "idx_art_alb_id" on the "track" table which includes two columns:"artist_id" and "album_id". This is because both track.artist_id and track.album_id columns are involved in the two INNER JOIN commands in the given query, so it is a good idea to create a composite index for these two columns so that the query can quickly use this composite index to find rows that matches both INNER JOIN conditions. I have also created indexes "idx_art_id" and "idx_alb_id" for the columns artist.id and album.id respectively, because these columns are used in GROUP BY and INNER JOIN commands, and they are being used frequently. As a result, creating the three indexes above is the optimal choise I have found so far.
</ul>

- Did you try anything other approaches?  How did they compare to your final answer?
<ul>Yes. I have tried five approaches in total.
<br>1st approach: I have first created one index for track.artist_id, one index for track.album_id, one index for artist.id, and one index for album.id, and my result was (mean: 0.052 best:0.010), which is slower than my final answer.
<br>2nd approach: I have removed the index for artist.id and created a composite index for artist.id & artist.artist_name instead based on the 1st approach, and this does not improve my result from the 1st approach (their result are the same).
<br>3rd approach: I have used a composite index for track.artist_id & track.album_id and used indexes for artist.id and album.id respectively. The result was (mean:0.048, best:0.009) and this is what I kept as the final optimal answer.
<br>4th approach: I have removed the index for album.id and created a composite index for album.id & album.album_listens instead based on the 3rd approach, and its result is the same as the result of the 3rd approach.
<br>5th approach: I have added a single index for album.album_listens based on the 3rd approach, and its result equals the result of the 3rd approach so there is no improvement.
</ul>
