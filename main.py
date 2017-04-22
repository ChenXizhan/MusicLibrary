#-*- encoding:utf-8 -*-
from classes.album import Song
from classes.album import Album
from classes.album import get_random_song
from classes.album import get_random_album
from classes.playlist import PlayList
from classes.musiclibrary import MusicLibrary
def test_album():
    song = Song(title = "Here I am", music_file = "G:\\Here I am.mp3")
    song.play_song()

    song2 = Song(title = "season in the sun", music_file = "/path/Season in the sun.mpe")
    song2.play_song()

    album = Album(song_list = [song, song2], artists=["Who"], label = "no such album",
        publish_yaer = "2017")
    print("The album:{}".format(album))
    print("-"*30)
    print("get a random song from album:\n")
    print(album.get_random_song())


# roughly test
def test_fun():
    print("get a random song\n")
    print("type:{}\n".format(type(get_random_song())))
    print("get a random album\n")
    print("type:{}\n".format(type(get_random_album())))

def test_playlist():
    pl = PlayList("Test List")
    print(str(pl))
def test_library():
    mb = MusicLibrary()
    print(str(mb))

    mb2 = MusicLibrary(["songs"]*3, ["Albums"]*3, ["PlayLists"]*3)
    print (str(mb2))
def main():
    #test_album()
    #test_fun()
    #test_playlist()
    test_library()

if __name__ == "__main__":
    main()