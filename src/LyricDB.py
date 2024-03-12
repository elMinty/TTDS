from pymongo import MongoClient, ASCENDING
from datetime import datetime
from LyricDBinit import *


class LyricDB():

    def __init__(self):
        """
        Initialize the database connection details.

        :param db_uri: MongoDB connection URI string (optional).
        :param db_name: Name of the database to use (optional).
        """

        self.connected = False
        self.client = None
        self.db = None
        self.db_uri = None
        self.db_name = None

    def __str__(self):
        # Return a string representation of the database connection details and all the collections.

        if self.client:
            collection_names = self.db.list_collection_names()
            return f"Database: {self.db_name} at {self.db_uri}\nCollections: {collection_names}"

    def init(self, db_uri, db_name):
        """
        Calls initialization methods from LyricDBinit to set up the database.
        """
        self.connect(db_uri, db_name)
        init_track_details_collection(self.db)
        init_lyrics_collection(self.db)
        init_albums_collection(self.db)
        init_update_track_collection(self.db)


    def connect(self, db_uri=None, db_name=None):
        """
        Establish a connection to the MongoDB database.

        :param db_uri: MongoDB connection URI string (optional if provided during class initialization).
        :param db_name: Name of the database to use (optional if provided during class initialization).
        """
        # Allow overriding or setting db_uri and db_name during connection
        if db_uri and db_name:
            self.db_uri = db_uri
            self.db_name = db_name
            self.client = MongoClient(self.db_uri)
            self.db = self.client[self.db_name]
            print(f"Connected to database: {self.db_name} at {self.db_uri}")
            self.connected = True

        if not self.db_uri or not self.db_name:
            raise ValueError(
                "Database URI and name must be provided either during initialization or when calling connect.")

    def put_update_from_json(self, json):
        """
        Insert or update a document in the Update_Track collection.
        :param json:

        """

        """
        JSON ITEMS: added_on album_id album_cover album_name artist_name release_date track_id track_name track_link duration_ms explicit danceability energy genres lyrics
        """
        for item in json:
            collection = self.db['updateTrack']
            document = {
                "added_on": item['added_on'],
                "album_id": item['album_id'],
                "album_cover": item['album_cover'],
                "album_name": item['album_name'],
                "artist_name": item['artist_name'],
                "release_date": item['release_date'],
                "track_id": item['track_id'],
                "track_name": item['track_name'],
                "track_link": item['track_link'],
                "duration_ms": item['duration_ms'],
                "explicit": item['explicit'],
                "danceability": item['danceability'],
                "energy": item['energy'],
                "genres": item['genres'],
                "lyrics": item['lyrics']
            }
            try:
                collection.insert_one(document)
            except Exception as e:
                print(f"An error occurred: {e}")


    def insert_song_details(self, track_id, album_id, album_name, artist_name, release_date, track_name,
                            duration_ms,
                            explicit, danceability, energy, genres):

        """
        Insert a new document into the Song_Details collection.

        :param track_id: Spotify track ID.
        :param album_id: Spotify album ID.
        :param album_name: Album name.
        :param artist_name: Artist name.
        :param release_date: Album release date.
        :param track_name: Track name.
        :param duration_ms: Track duration in milliseconds.
        :param explicit: Explicit content flag.
        :param danceability: Danceability score.
        :param energy: Energy score.
        :param genres: List of genres.
        """
        collection = self.db[self.collection_name]

        document = {
            "track_id": track_id,
            "album_id": album_id,
            "added_on": datetime.utcnow(),
            "album_name": album_name,
            "artist_name": artist_name,
            "release_date": release_date,
            "track_name": track_name,
            "duration_ms": duration_ms,
            "explicit": explicit,
            "danceability": danceability,
            "energy": energy,
            "genres": genres
        }

        try:
            collection.insert_one(document)

            # if album_id not in self.db['albumDetails'].find_one({"album_id": album_id}):
            # else add the track to the album details
            if not self.db['albumDetails'].find_one({"album_id": album_id}):
                self.__insert_new_album_details(album_id, album_name, artist_name, genres, [track_id])

            else:
                self.__update_album_tracks(album_id, track_id)
        except Exception as e:
            print(f"An error occurred: {e}")

    def __insert_new_album_details(self, album_id, album_name, artist_name, genres, tracks=[]):

        collection = self.db['albumDetails']
        document = {
            "album_id": album_id,
            "album_name": album_name,
            "artist_name": artist_name,
            "genres": genres,
            "tracks": tracks
        }
        try:
            collection.insert_one(document)
        except Exception as e:
            print(f"An error occurred: {e}")

    def __update_album_tracks(self, album_id, track_id):
        collection = self.db['albumDetails']
        collection.update_one({"album_id": album_id}, {"$push": {"tracks": track_id}})

    def insert_song_lyrics(self, track_id, lyrics):

        collection = self.db['songLyrics']
        document = {
            "track_id": track_id,
            "lyrics": lyrics
        }
        try:
            collection.insert_one(document)
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_or_update_lyricIndex(self, word, track_id, positions):
        """
        Insert or update a word with associated track ID and positions in the wordPositions collection.
        """
        collection = self.db['wordPositions']
        update_result = collection.update_one(
            {"word": word, "occurrences.track_id": track_id},
            {"$set": {"occurrences.$.positions": positions}},
            upsert=False
        )
