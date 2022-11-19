SET @start_time = ROUND(UNIX_TIMESTAMP(CURTIME(4)) * 1000);
 
select film_id FROM sakila.film where film_id = 250;
SET @end_time = ROUND(UNIX_TIMESTAMP(CURTIME(4)) * 1000);
 
SELECT (@end_time - @start_time) AS time_taken;
