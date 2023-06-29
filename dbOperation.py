import mysql.connector

def create_table(connection):
    try:
        cursor = connection.cursor()

        create_query = """
            CREATE TABLE IF NOT EXISTS facebook (
                id INT AUTO_INCREMENT PRIMARY KEY,
                page_id VARCHAR(500),
                access_token VARCHAR(500),
                message TEXT,
                image LONGBLOB,
                timestamp TEXT
            )
        """
        cursor.execute(create_query)

        connection.commit()

        cursor.close()

    except mysql.connector.Error as e:
        print("Table creation error:", e)


def insert_data(page_id, access_token, message, image_bytes, timestamp):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='12345678',
            database='socialdesktop'
        )

        create_table(connection)

        cursor = connection.cursor()

        insert_query = "INSERT INTO facebook (page_id, access_token, message, image, timestamp) VALUES (%s, %s, %s, %s, %s)"
        values = (page_id, access_token, message, image_bytes, timestamp)
        cursor.execute(insert_query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return True

    except mysql.connector.Error as e:
        print("Database error:", e)
        return False


def get_all_rows():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='12345678',
            database='socialdesktop'
        )

        cursor = connection.cursor()

        select_query = "SELECT * FROM facebook"
        cursor.execute(select_query)

        rows = cursor.fetchall()
        row_count = len(rows)

        cursor.close()
        connection.close()

        return row_count

    except mysql.connector.Error as e:
        return 0
