from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgressql:///chinook")

meta = MetaData(db)

# create variable for "artist" table
artist_table = Table(
    "artist", meta,
)

# making the connection
with db.connect() as connection: