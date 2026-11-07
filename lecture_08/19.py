class Movie:

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_details(self):
        print("Movie:", self.title)
        print("Director:", self.director)
        print("Rating:", self.rating, "/10")


movie1 = Movie("Inception", "Christopher Nolan", 8.8)

movie1.display_details()
