import LyricDB

if __name__ == '__main__':

    try:
        # Create a new LyricDB object
        lyric_db = LyricDB.LyricDB()

        #init
        lyric_db.init('localhost','LyricDB')

        # Print the database connection details
        print(lyric_db)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Exiting...")