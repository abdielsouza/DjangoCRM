import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MintMaster123"
    )

    cursorObject = database.cursor()

    cursorObject.execute("CREATE DATABASE crmdata")
    print("All done!")
except:
    raise Exception("Failed to init database!")