#-*- encoding: utf-8 -*-

class MusicLibrary(object):
    # three lists
    def __init__(self, albumlist = [], songlist=[], playlists = []):
        self.albumlist  = albumlist
        self.songlist   = songlist
        self.playlists  = playlists


    def __str__(self):
        if not self.albumlist and not self.songlist and not self.playlists:
            return "<Empty Music Library>"
        else:
            s = "Albums:\n{}\n".format("_"*40)
            for album in self.albumlist:
                s += "{}\n".format(album)
            s+="\n"

            s += "Songs:\n{}\n".format("_"*40)
            for song in self.songlist:
                s += "{}\n".format(song)
            s+="\n"

            s += "PlayLists:\n{}\n".format("_"*40)
            for playlist in self.playlists:
                s += "{}\n".format(playlist)
            return s
