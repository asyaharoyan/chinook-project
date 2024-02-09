from sqlalchemy import (
    create_engine, Column, Float, ForeginKey, Integer, String
)

from sqalchemy.ext.declarative import declarative_base
from sqalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Artist(base):
    __tablenae__ = "artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Album(base):
    __tablenae__ = "album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeginKey(Artist.ArtistId))

class Track(base):
    __tablenae__ = "track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeginKey(Album.AlbumId))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)


# Instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine(the db)
Session = session(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.createall(db)

    
# Query 1 - select all records from the "Artist" table
artists = session.query(Artist)

for artist in artists:
    print(artist.ArtistId, artist.name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# select_query = artist_table.select().with_only_columns([artist_table.c.name])

# Query 3 - select only 'Queen' from the "Artist" table
# select_query = artist_table.select().where(artist_table.c.name == "Queen")

# Query 4 - select only by 'ArtistId' #51 from the "Artist" table
# select_query = artist_table.select().where(artist_table.c.artist_id == 51)

# Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
# select_query = album_table.select().where(album_table.c.artist_id == 51)

# Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
# select_query = track_table.select().where(track_table.c.composer == "Queen")

# Query 7 - select all tracks where the composer is 'AC/DC' from the "Track" table
# select_query = track_table.select().where(track_table.c.composer == "AC/DC")