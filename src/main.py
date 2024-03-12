import json

from pymongo import MongoClient
from LyricDB import LyricDB

if __name__ == '__main__':

    lyricDB = LyricDB()
    lyricDB.connect('mongodb://localhost:27017/', 'LyricDB')

    # Read json from file and put it in the database
    with open('../src/data/spotify_tracks_data.json') as f:
        data = json.load(f)

    lyricDB.put_update_from_json(data)