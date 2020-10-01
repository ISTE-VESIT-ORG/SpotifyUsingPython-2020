from config import *
import traceback

def get_all_tracks():
		collection = db.collection(u'Tracks')
		return list(map(lambda x: x.to_dict(), collection.stream()))

for track in get_all_tracks():
	print()
	for key,value in track.items():
		print(key, "-->", value)
