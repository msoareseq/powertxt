from pathlib import Path

class PowerTxt:
    """A simple text handling class."""	
    def __init__(self, filename):
        self.path = Path(filename)
        self.data = self.load()

    def load(self, filename):
        """Load a new text file."""
        self.path = Path(filename)
        self.data = self.path.read_text()

    def save(self):
        """Save the current text file."""
        self.path.write_text(self.data)

    def save_as(self, filename):
        """Save the current text file as a new file."""
        self.path = Path(filename)
        self.save()

    