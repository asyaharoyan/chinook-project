import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "artist " table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "name" column from the "artist " table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only the "name" column from the "artist " table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only the "name" column from the "artist " table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query 5 - select only the "name" column from the "artist " table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select only the "name" column from the "artist " table
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# Query 7 - select only the "name" column from the "artist " table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["AC/DC"])

# Query 8 - select only the "name" column from the "artist " table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["SOAD"])


# fetch the results(multiple)
# results = cursor.fetchall()

# fetch the results(multiple)
results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
