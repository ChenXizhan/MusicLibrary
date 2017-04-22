这是《Python入门经典 Katie Cunningham著》第十四章的练习题，在本章正文中，规划了一个音乐库程序，设计了一些类和函数，并做了适当的分拆，然后编写了一个主程序来调用它们。现在的任务实现这个计划，不需要实际的功能，只要确认是否能入期望的那样调用这些属性和方法。
--------------------------------------------------------------------------------
管理音乐收藏家的音乐库程序如下。
先是两个类和他们各自的属性,

Song
-----
Title
Artist
Music file
Play time
Genre

Album
-----
A list of songs
Artist(S)
Label
Year published
注：album n 唱片集，专辑

随后，需要让程序做些事情，比如
Play a song
Play a random song off an album
Play a random album
这些函数有的属于一个类，有的则独立于这些类，于是，得到下面的设计

Song
--------------------
Attributes:
    Title
    Artist
    Music file
    Play time
    Genre (类型，流派)
Functions：
    Play song

Album
--------------------
Attributes:
    A list of songs
    Artist(s)
    Label
    Year published
Functions:
    Get a random song

General functions:
--------------------
Get a random song
Get a random album

这些类和函数相关性很强，歌曲总是要在专辑中，专辑总是要包含歌曲，得到随机的专辑和歌曲既需要歌曲又需要专辑。故而，这两个类和两个单独的方法放在同一个文件中

哦，要是再有一个播放列表就更好了，这里把播放列表放在单独的文件中
PlayList
----------------------------------------
Title
Song list
Edit song list

倒数第二项，需要考虑如何保存所有这些歌曲、专辑和播放列表。于是，需要一个分类的库，专门为它创建一个文件
Music Library
-------------
Album list
Song list
Playlist list

最后，就是主程序，主程序需要做什么？导入Song、Album、和Playlist，需要有一些让用户播放歌曲的方法。

Main Program
-------------
Load Library
Play a random song / album
Play a selected song / album playlist

以上内容照抄书本，但是，我有些不理解其中的一些做法，受作者的启发，我对建立音乐库有一些自己的想法
--------------------------------------------------------------------------------


