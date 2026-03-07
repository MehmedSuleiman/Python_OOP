from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos : list[list[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(ceil(photos_count // PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, photo: str) -> str:
        for i, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                self.photos[i].append(photo)
                return f"{photo} photo added successfully on page {i +1} slot {len(page)}"
        return "No more free slots"

    def display(self) ->str:
        sep = "-"*11 + "\n"
        result = sep
        for page in self.photos:
            result +=" ".join("[]" for i in page) + "\n"
            result += sep

        return result.strip()



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

