from project.song import Song


class Album:
    def __init__(self, name:str, *songs):
        self.name = name
        self.published : bool = False
        self.songs : list[Song] = [*songs]

    def add_song(self, song: Song) -> str:
        if self.published:
            return  "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        song = next((song for song in self.songs if song.name == song_name), None)
        if self.published:
            return "Cannot remove songs. Album is published."
        if not song:
            return "Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = [f"Album {self.name}",]
        for song in self.songs:
            result.append(f"== {song.get_info()}")

        return "\n".join(result)