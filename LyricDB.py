from pymongo import MongoClient, ASCENDING
from datetime import datetime


class LyricDB:

    def __init__(self, db_uri=None, db_name=None):
        """
        Initialize the database connection details.

        :param db_uri: MongoDB connection URI string (optional).
        :param db_name: Name of the database to use (optional).
        """
        self.db_uri = db_uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.collection_name = []

    def __str__(self):
        # Return a string representation of the database connection details and all the collections.

        if self.client:
            collection_names = self.db.list_collection_names()
            return f"Database: {self.db_name} at {self.db_uri}\nCollections: {collection_names}"

    def connect(self, db_uri=None, db_name=None):
        """
        Establish a connection to the MongoDB database.

        :param db_uri: MongoDB connection URI string (optional if provided during class initialization).
        :param db_name: Name of the database to use (optional if provided during class initialization).
        """
        # Allow overriding or setting db_uri and db_name during connection
        if db_uri:
            self.db_uri = db_uri
        if db_name:
            self.db_name = db_name

        if not self.db_uri or not self.db_name:
            raise ValueError(
                "Database URI and name must be provided either during initialization or when calling connect.")

        self.client = MongoClient(self.db_uri)
        self.db = self.client[self.db_name]
        print(f"Connected to database: {self.db_name} at {self.db_uri}")

    def init_song_details_collection(self):
        """
        Initialize the Song_Details collection with an index on 'track_id'.
        """
        if self.collection_name not in self.db.list_collection_names():
            collection = self.db[self.collection_name]

            # # Optionally define a sample document structure and insert it. Uncomment the next lines if needed.
            # sample_document = {
            #     "track_id": "example_track_id",
            #     "added_on": datetime.utcnow(),
            #     "album_id": "example_album_id",
            #     "album_name": "Example Album Name",
            #     "artist_name": "Example Artist",
            #     "release_date": "2023-01-01",
            #     "track_name": "Example Track Name",
            #     "duration_ms": 240000,
            #     "explicit": False,
            #     "danceability": 0.5,
            #     "energy": 0.8,
            #     "genres": ["pop", "dance"]
            # }
            # collection.insert_one(sample_document)

            collection.create_index([("track_id", ASCENDING)], unique=True)

            print(f"Collection '{self.collection_name}' initialized with an index on 'track_id'.")
        else:
            print(f"Collection '{self.collection_name}' already exists.")

    def init_song_lyrics_collection(self):
        collection_name = 'songLyrics'
        if collection_name not in self.db.list_collection_names():
            collection = self.db[collection_name]
            # Creating an index on 'track_id' to optimize lookups
            collection.create_index([("track_id", ASCENDING)], unique=True)
            print(f"Collection '{collection_name}' initialized with an index on 'track_id'.")
        else:
            print(f"Collection '{collection_name}' already exists.")

    def init_lyricIndex_collection(self):
        collection_name = 'lyricIndex'
        if collection_name not in self.db.list_collection_names():
            collection = self.db[collection_name]
            # Creating an index on lyric to optimize lookups
            collection.create_index([("lyric", ASCENDING)], unique=True)
            print(f"Collection '{collection_name}' initialized with an index on 'lyric'.")
        else:
            print(f"Collection '{collection_name}' already exists.")

    def init_album_details_collection(self):
        # album_id, album_name, artist_name, release_date, genres
        collection_name = 'albumDetails'
        if collection_name not in self.db.list_collection_names():
            collection = self.db[collection_name]
            # Creating an index on album_id to optimize lookups
            collection.create_index([("album_id", ASCENDING)], unique=True)
            print(f"Collection '{collection_name}' initialized with an index on 'album_id'.")
        else:
            print(f"Collection '{collection_name}' already exists.")

    # track_id, album_id, added_on, album_name, artist_name, release_date, track_name, duration_ms, explicit, danceability, energy, genres
    def insert_song_details(self, track_id, album_id, album_name, artist_name, release_date, track_name, duration_ms,
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
