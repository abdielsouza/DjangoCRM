import psycopg2

try:
    db_connection = psycopg2.connect(
        dbname="verceldb",
        user="default",
        password="jQf6WlJD0HhI",
        host="ep-lively-unit-a42hu5mi-pooler.us-east-1.aws.neon.tech",
        port="5432"
    )
    print("successfully connected to database!")
except Exception as e:
    raise print(f"CONNECTION ERROR: {e}")