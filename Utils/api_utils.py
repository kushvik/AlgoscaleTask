from src.Service import dbConnection
from twitter import *


def getUserDetails():
    t = Twitter(
        auth=OAuth("770886120707993600-kK8x0EkZRQtVsIu3AKC7wAisOz36YhV",
                   "4B1YR9Sq2uLHlCzcb73kNoHHI20FRJyEHQiZxsjDIzhrZ", "593OYxE0d1PA27aGdp5el4quD",
                   "SIzT6CDrm5LeF6uLjcgGOWMRoHRRe8uhTQTIwUWl0BgyUQyWkz"))

    # Get your "home" timeline
    userDetails = t.statuses.home_timeline(count=5)  # count can be change
    return userDetails


def getFriends():
    t = Twitter(
        auth=OAuth("770886120707993600-kK8x0EkZRQtVsIu3AKC7wAisOz36YhV",
                   "4B1YR9Sq2uLHlCzcb73kNoHHI20FRJyEHQiZxsjDIzhrZ", "593OYxE0d1PA27aGdp5el4quD",
                   "SIzT6CDrm5LeF6uLjcgGOWMRoHRRe8uhTQTIwUWl0BgyUQyWkz"))
    friendsFav = {}
    friendsList = t.friends.ids()
    if 'ids' in friendsList:
        for ids in friendsList['ids']:
            fav = t.favorites.list(count=2, user_id=ids)  # count can be change accouding to redord want to featch
            friendsFav[str(ids)] = fav
        db_connection = dbConnection.dbConnection()
        db = db_connection.connection_start()
        collections = db.favData
        try:
            object_result = collections.insert_one(friendsFav)
            db_connection.connection_close()
        except Exception as e:
            print(e)
            db_connection.connection_close()
    return friendsFav
