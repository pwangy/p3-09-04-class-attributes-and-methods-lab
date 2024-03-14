class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def init(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self)._add_entity_to_list(self.genre, type(self).genres)
        type(self)._add_entity_to_list(self.artist, type(self).artists)
        type(self)._add_to_count_and_dict(self.genre, type(self).genre_count)
        type(self)._add_to_count_and_dict(self.artist, type(self).artist_count)
        type(self).add_song_to_count()

    @classmethod
    def _add_entity_to_list(cls, entity, entity_list):
        if entity not in entity_list:
            entity_list.append(entity)

    @classmethod
    def _add_to_count_and_dict(cls, key, count_dict):
        count_dict[key] = count_dict.get(key, 0) + 1

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1