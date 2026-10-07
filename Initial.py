from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    genre: str
    year: int
    rating: float


class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, year, rating):
        self.movies.append(Movie(title, genre, year, rating))

    def search(self, query):
        return [
            movie for movie in self.movies
            if query.lower() in movie.title.lower()
            or query.lower() in movie.genre.lower()
        ]

    def top_movies(self, limit=5):
        return sorted(
            self.movies,
            key=lambda movie: movie.rating,
            reverse=True
        )[:limit]

    def show(self):
        print("Movie Manager")
        print("=============")

        for movie in sorted(self.movies, key=lambda item: item.year, reverse=True):
            print(
                f"{movie.title} | "
                f"{movie.genre} | "
                f"{movie.year} | "
                f"Rating: {movie.rating:.1f}"
            )


manager = MovieManager()

manager.add_movie("Inception", "Sci-Fi", 2010, 8.8)
manager.add_movie("Interstellar", "Sci-Fi", 2014, 8.7)
manager.add_movie("The Dark Knight", "Action", 2008, 9.0)
manager.add_movie("The Matrix", "Sci-Fi", 1999, 8.7)
manager.add_movie("Gladiator", "Drama", 2000, 8.5)

manager.show()

print("\nTop Movies")
print("----------")

for movie in manager.top_movies(3):
    print(f"{movie.title}: {movie.rating:.1f}")

print("\nSearch Results")
print("--------------")

for movie in manager.search("sci-fi"):
    print(f"{movie.title} ({movie.year})")