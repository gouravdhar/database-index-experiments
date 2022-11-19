import string
import mysql.connector
import json
import time
import random


mydb = mysql.connector.connect(
  host='localhost',
  user='<enter the database usernam>',
  password='<enter the database password>',
  database='sakila',
  port=3306
)



def insert_row(cursor):
    year = random.randint(2000,2022)
    rental_duration = random.randint(1,8)
    rental_rate = random.randint(5,18)
    length = random.randint(50,900)
    replacement_cost = random.randint(50,900)
    random_title = str(''.join(random.choices(string.ascii_lowercase + string.digits, k=9)))
    random_description = str(''.join(random.choices(string.ascii_lowercase + string.digits, k=9)))

    sql_select_Query = "insert into film(title,description,release_year,language_id,rental_duration, rental_rate, length, replacement_cost,rating,special_features) values('"+random_title+"','"+random_description+"',"+str(year)+", 1, "+str(rental_duration)+","+ str(rental_rate)+","+ str(length)+","+ str(replacement_cost)+", 'G', 'Deleted Scenes');"
    
    cursor.execute(sql_select_Query)
    result = cursor.fetchall()
    for voice_session_id in result:
        print(voice_session_id[0])
    
        
def insert_multiple_rows(n):
    cursor = mydb.cursor()
    for i in range(0,n):
        insert_row(cursor)
        print('Inserted row : '+str(i))
    mydb.commit()

insert_multiple_rows(10000)


