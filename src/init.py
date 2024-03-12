import LyricDB

if __name__ == '__main__':

    try:
        # Create a new LyricDB object
        lyric_db = LyricDB.LyricDB()

        # Connect to the MongoDB server
        lyric_db.connect('localhost', 'lyrics_db')

        # Initialize the Song_Details collection
        lyric_db.init_song_details_collection()

        # Print the database connection details
        print(lyric_db)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Exiting...")