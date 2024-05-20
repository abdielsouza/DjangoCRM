import sqlite3.dbapi2 as sqlite

try:
    database = sqlite.connect('./db.sqlite3')

    cursorObject = database.cursor()

    cursorObject.execute("DROP DATABASE IF EXISTS crmdata")
    cursorObject.execute("CREATE DATABASE crmdata")
    print("All done!")
except:
    raise Exception("Failed to init database!")