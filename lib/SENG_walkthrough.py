class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
        type(self).add_to_genre_count(genre)
        type(self).add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre_to_add):
        if genre_to_add not in cls.genres:
            cls.genres.append(genre_to_add)

    @classmethod
    def add_to_artists(cls, artist_to_add):
        if artist_to_add not in cls.artists:
            cls.artists.append(artist_to_add)

    @classmethod
    def add_to_genre_count(cls, genre):
        #! The next line is an alternative for line 33
        # if cls.genre_count.get(genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def find_artist_with_most_songs(cls):
        # sort in desc order and then pluck first el if any
        try:
            return max(
                cls.artist_count, key=lambda artist_name: cls.artist_count.get(artist_name, 0)
            )
        except Exception as e:
            print(e)
            return False

# s1 = Song("99 Problems", "Jay Z", "Rap")
# s2 = Song("Halo", "Beyonce", "Pop")
# s3 = Song("I was here", "Beyonce", "Pop")
# s4 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
print('done')