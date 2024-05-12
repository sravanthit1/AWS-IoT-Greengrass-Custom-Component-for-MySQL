import pymysql
import boto3
from datetime import datetime, timedelta
import json
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_database():
    try:
        # Connect to MySQL database
        return pymysql.connect(host='localhost', user='admin', password='password', database='tsdb')
    except pymysql.Error as e:
        logger.error("Error connecting to the database: %s", e)
        raise

def fetch_data(connection):
    try:
        # Fetch data for the last 10 minutes
        query = "SELECT * FROM time_series WHERE date_time >= %s;"
        start_time = datetime.now() - timedelta(minutes=10)
        with connection.cursor() as cursor:
            cursor.execute(query, (start_time,))
            rows = cursor.fetchall()
        formatted_data = []
        for row in rows:
            # Ensure that the datetime column is converted to a datetime object
            date_time = row[1]  # Assuming date_time is in the second column
            if not isinstance(date_time, datetime):
                try:
                    date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    logger.warning("Unable to parse date_time: %s", date_time)
                    continue
            formatted_data.append((row[0], date_time, row[2], row[3]))  # Assuming other_field is in the third column
        return formatted_data
    except pymysql.Error as e:
        logger.error("Error fetching data from the database: %s", e)
        raise

def convert_to_json(data):
    try:
        # Convert data to list of dictionaries
        formatted_data = []
        for item in data:
            formatted_item = {
                'tag_name': item[0], 
                'date_time': item[1].isoformat(),  # Assuming the first element is the datetime
                'value': item[2],  # Adjust this according to your data structure
                'quality': item[3],  # Adjust this according to your data structure
                # Add more fields as necessary
            }
            formatted_data.append(formatted_item)

        # Convert data to JSON format
        return json.dumps(formatted_data)
    except Exception as e:
        logger.error("Error converting data to JSON: %s", e)
        raise

def upload_to_s3(json_data):
    try:
        # Upload data to S3   
        s3 = boto3.client('s3', 
                      aws_access_key_id='XXXX', 
                      aws_secret_access_key='XXXXXXXXX')
        bucket_name = 'ddi-ggbucket-data'
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        key = f'data_{timestamp}.json'

        s3.put_object(Body=json_data, Bucket=bucket_name, Key=key)
        logger.info("Data uploaded to S3 successfully.")
    except Exception as e:
        logger.error("Error uploading data to S3: %s", e)
        raise

def main():
    while True:
        try:
            # Connect to database
            connection = connect_to_database()

            # Fetch data
            data = fetch_data(connection)

            # Convert to JSON
            json_data = convert_to_json(data)

            # Upload to S3
            upload_to_s3(json_data)

            # Close database connection
            connection.close()

            # Sleep for 10 minutes
            time.sleep(60)  # Sleep for 10 minutes
        except Exception as e:
            logger.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()