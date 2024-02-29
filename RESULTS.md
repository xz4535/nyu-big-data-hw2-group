# Homework 1 results

Your name: Xiaoyu Zhang, Ziqing Peng, Erchi Zhang

## Part 1
Paste the results of your queries for each question given in the README below:

1.<br>Track ID: 22344, Track Name: Wesley Willis
<br>Track ID: 66084, Track Name: Wayne Myers
<br>Track ID: 66096, Track Name: Wayne Myers
<br> We pull track id and track lyricist from track, and in table track we enter queries to find lyricist's name that start with W.

2.<br>value:(None,)
<br>value:('Radio-Safe',)
<br>value:('Radio-Unsafe',)
<br>value:('Adults-Only',)
<br> We follow the question, then use "DISTINCT track_explicit" to find unique value of this field from table track to find metadata.

3.<br>Track ID: 62460, Track title: Siesta
<br> We locate track id and track title from table track and we order them by what we find for track listens, at last we only pick the top one answer.

4.<br>Number:(453,)
<br> Frist we use "DISTINCT id" to find unique id from table artist for related projects, and we demand that related projects to be not null in case those people dont have a related projects

5.<br>language codes:('de',)
<br>language codes:('ru',)
<br> we locate and group track language code, set it to be not null from table track and count them we only want 4.

6.<br>number of track:(1697,)
<br> we count tracks what active from 1990 to 1999 from table track and combine with table artist with let artist id to equal artist id from track. at last we finished counting

7.<br>artist:Ars Sonor, number of album producers:6
<br>artist:U Can Unlearn Guitar, number of album producers:6
<br>artist:Disco Missile, number of album producers:5
<br> First we find artist name form track and count unique album producer with "DISTINCT album.album_producer", and we comnbine table artist with table track with artist id is track.artist id and table album with album id is track.album id, then we group the artist id and order them with the count of distinct album producer with only the top 3.

8.<br>id:76008, title:JessicaBD, artist name:Cody Goss, difference:3561386
<br> we locate track id, track title, track name and name the result of album listens-track listens as diff, from table track, combine with table artist and table album, then we order the result by diff we named and only print out the top one.

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
