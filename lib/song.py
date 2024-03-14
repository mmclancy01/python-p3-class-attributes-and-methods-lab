class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {"Rap": 0, "Pop": 0, "Rock": 0}
    artist_count = {"Jay Z":0, "Beyonce":0, "Nirvana":0, "Hall and Oates": 0 }
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1


   
    




