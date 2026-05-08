import os

import psycopg2
import psycopg2.extras


def query(query_object, query_values=None):
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT"),
        user=os.environ.get("POSTGRES_USER"),
        dbname=os.environ.get("POSTGRES_DB"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )
    try:
        with conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        ) as cursor:
            cursor.execute(query_object, query_values)
            result = cursor.fetchall()
        conn.commit()
    finally:
        conn.close()
    return result
