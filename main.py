from pymongo import MongoClient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # "added_on", "album_id", "album_name", "artist_name", "release_date", "track_id", "track_name", "duration_ms", "explicit", "danceability", "energy", "genres"

    # Connect to the MongoDB server (default is localhost on port 27017)
    client = MongoClient('localhost', 27017)

    # Create a new database or connect to an existing one
    db = client['example_db']

    # Create a new collection or connect to an existing one
    collection = db['example_collection']

    # Insert a document into the collection
    document = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    collection.insert_one(document)

    print("Document inserted into the collection")