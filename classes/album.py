# -*- encoding:utf-8 -*-
from random import choice # used in class album

# 歌曲
class Song(object):
    """docstring for Song"""
    def __init__(self, title, music_file,  artist="",play_time="", genre=""):
        self.title  = title
        self.artist = artist
        self.music_file = music_file
        self.play_time  = play_time
        self.genre  = genre
    def __str__(self):
        return "<<{}>>".format(self.title +self.artist)


    def play_song(self):
        print "Playing song {}".format(self.__str__())


# 专辑
class Album(object):
    """
        song_list : A list of songs
        artists   : A list of artists
    """
    def __init__(self,song_list,artists,label,publish_yaer):
        self.song_list  = song_list
        self.artists    = artists
        self.label  = label
        self.publish_yaer   = publish_yaer
    def __str__(self):
        s = "label:{}\n".format(self.label)
        s += ("{}\nsongs:\n".format("-"*30))
        for song in self.song_list:
            s+= "{}\n".format(song)
        return s

    def get_random_song(self):
        return choice(self.song_list)


song = Song(title = "Here I am", music_file = "G:\\Here I am.mp3")
song2 = Song(title = "season in the sun", music_file = "/path/Season in the sun.mpe")
album = Album(song_list = [song, song2], artists=["Who"], label = "no such album",
    publish_yaer = "2017")
# function
def get_random_song():
    return song
#
def get_random_album():
    return album