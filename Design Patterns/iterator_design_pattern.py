from typing import List
from abc import ABC,abstractmethod

class Song():
    def __init__(self,song) -> None:
        self.song=song
    def get_song_name(self):
        return self.song

class Iterator:
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class PlayListIterator(Iterator):
    def __init__(self,playlist) -> None:
        self.__playlist=playlist
        self.position=0

    def has_next(self):
        return self.position<len(self.__playlist)
    def next(self)->Song|None:
        if self.has_next():
            res=self.__playlist[self.position]
            self.position+=1
            return res
        return None
        print("No next song present")

class PlayList():
    def __init__(self) -> None:
        self.playlist:List[Song]=[]

    def add_song(self,song:Song):
        self.playlist.append(song)

    def create_iterator(self)->PlayListIterator:
        return PlayListIterator(self.playlist)

playlist=PlayList()
playlist.add_song(Song("song one"))
playlist.add_song(Song("song two"))
playlist.add_song(Song("song onesdfa"))
playlist.add_song(Song("song two32"))
playlist.add_song(Song("song oneafsfwe"))
playlist.add_song(Song("song twofasd"))

playlistiterator=playlist.create_iterator()

while playlistiterator.has_next():
    song=playlistiterator.next()
    print(song.get_song_name())
print(playlistiterator)