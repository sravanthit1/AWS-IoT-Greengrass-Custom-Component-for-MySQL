import pymysql 
import random
import time

# MySQL connection
conn_mysql = pymysql.connect(db="tsdb", user="admin", password="password")
cur_mysql = conn_mysql.cursor()

# Create the table if not exists
cur_mysql.execute("""CREATE TABLE IF NOT EXISTS time_series (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        tag_name VARCHAR(255),
                        date_time DATETIME,
                        value FLOAT,
                        quality BOOLEAN
                    );""")
conn_mysql.commit()

while True:
    # Inserting records with random data
    tag_name = "example_tag"
    date_time = time.strftime('%Y-%m-%d %H:%M:%S')
    value = random.uniform(0, 100)
    quality = bool(random.getrandbits(1))

    # MySQL insertion
    cur_mysql.execute("INSERT INTO time_series (tag_name, date_time, value, quality) VALUES (%s, %s, %s, %s);", (tag_name, date_time, value, quality))
    conn_mysql.commit()
    print(f"name: {tag_name}, date_time: {date_time}, value: {value}, quality: {quality}")



    # Sleep for 1 second
    time.sleep(1)

# Close connections
cur_mysql.close()
conn_mysql.close()
