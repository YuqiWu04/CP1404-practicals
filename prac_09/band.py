class Band:
    """Band class for storing details of a band with musicians."""

    def __init__(self, name):
        """initial value of band name and musician list"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """display a musicians detail from band"""
        musicians_data = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_data})"

    def play(self):
        """display each musician playing their instruments."""
        messages = []
        for musician in self.musicians:
            messages.append(musician.play())
        return "\n".join(messages)