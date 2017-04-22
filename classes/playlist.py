# -*- encoding:utf-8 -*-

class PlayList(object):
    def __init__(self, title="", song_list = []):
        self.title = title
        self.song_list = song_list
    def __str__(self):
        s = "PlayList:{}".format(self.title)
        if not self.song_list:
            s += "<empty list>"
        return s
    def edit_song_list():
        # 这个，我想不到该怎么实现
        a = 0
