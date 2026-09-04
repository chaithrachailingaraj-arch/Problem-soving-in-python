class Movie:
    def __init__(self, title, rating ):
        self.title = title
        self.rating = rating

    def display(self):
        print(f"{self.title} rating {self.rating}")

M1 = Movie("KGF","4.5 star")
M2 = Movie("Tagaru","4 star")
M1.display()
M2.display()