class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def is_recent(self, n):
        return self.year >= (2025 - n)

class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = int(pages)

    def __str__(self):
        return f"Book -> {super().__str__()}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = int(duration)

    def __str__(self):
        return f"Podcast -> {super().__str__()}, Host: {self.host}, Duration: {self.duration} mins"


def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            f.write(f"{item.__class__.__name__},{item.uid},{item.title},{item.year},{','.join(str(x) for x in item.__dict__.values())[len(item.uid)+len(item.title)+len(str(item.year))+3:]}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            type_ = parts[0]
            if type_ == "Book":
                items.append(Book(*parts[1:]))
            elif type_ == "Article":
                items.append(Article(*parts[1:]))
            elif type_ == "Podcast":
                items.append(Podcast(*parts[1:]))
    return items


items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "Python Tricks", 2021, "Dan Bader", 464),
    Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
    Article("A102", "AI in Medicine", 2020, "Lancet", "10.5678/med432"),
    Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
    Podcast("P302", "History Bites", 2019, "John Smith", 30),
]

save_to_file(items, "archive.txt")
loaded_items = load_from_file("archive.txt")

print("\nAll Archive Items:")
for item in loaded_items:
    print(item)

print("\nRecent Items:")
for item in loaded_items:
    if item.is_recent(5):
        print(item)

print("\nArticles with DOI starting '10.1234':")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)
