SET @start_time = ROUND(UNIX_TIMESTAMP(CURTIME(4)) * 1000);
 
#some sql query to capture time
 
SELECT (@end_time - @start_time) AS difference;
