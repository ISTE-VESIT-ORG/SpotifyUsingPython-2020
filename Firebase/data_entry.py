from config import *

def set_track(track_title, track_genre, track_location, track_artist, language):
    collection = db.collection(u'Tracks').document(track_title)
    collection.set({
        'artist': track_artist,
        'genre': track_genre,
        'location': track_location,
        'title': track_title,
        'like_count': 0,
        'Language': language
    })
    print('Track added successfully')
    return True
