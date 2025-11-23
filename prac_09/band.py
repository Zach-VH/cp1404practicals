"""
Prac 9
Band Class
"""

class Band():
    """Represent an instance of a band"""
    def __init__(self,band_name=""):
        """Initialise a band instance"""
        self.name = ""
        self.musicians = []

    def __str__(self):
        """Return string instance of a band"""
        return f"{self.name} ({",".join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def play(self):
        """Return a string showing the list of musicians and their first instrument"""
        if not self.musicians:
            return f"This Band is empty... Add some musicians!"
        return "\n".join([musician.play() for musician in self.musicians])

    def add(self,musician):
        """Add a musician to band"""
        self.musicians.append(musician)

if __name__ == '__main__':
    from guitar import Guitar
    from musician import Musician

    band = Band()
    assert band.name == ""
    assert band.musicians == []
    print(band.play())

    band.name = "Extreme"
    band.musicians.append(Musician("Nuno Bettencourt"))
    band.musicians[0].instruments.append(Guitar("Washburn N4",1990,2499.95))
    band.musicians[0].instruments.append(Guitar("Takamine acoustic", 1986, 1200.00))

    band.musicians.append(Musician("Gary Cherone"))

    band.musicians.append(Musician("Pat Badger"))
    band.musicians[2].instruments.append(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    band.musicians.append(Musician("Kevin Figueiredo"))

    print(band)
    print(band.play())
