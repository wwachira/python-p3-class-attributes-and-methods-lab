#!/usr/bin/env python3
#creation of Song objects, in song.py displayed in the attributes
#added method to reset `out_of_touch.title` the attribute is named title, not name

from song import Song

class TestSong:
    '''Class "Song" in song.py'''

    def setUp(self):
        Song.count = 0
        Song.genre_count = {}
        Song.artist_count = []
        Song.genres = []
        Song.artists = []

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.title == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert(Song.count == 3)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 4)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert("Jay Z" in Song.artists)
        assert("Beyonce" in Song.artists)
        assert("Nirvana" in Song.artists)

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 2)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        Song("Out of Touch", "Hall and Oates", "Pop")
        assert(Song.artist_count["Jay Z"] == 1)
        assert(Song.artist_count["Beyonce"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count["Hall and Oates"] == 2)