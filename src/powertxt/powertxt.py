from pathlib import Path

class PowerTxt:
    """A simple text handling class."""	
    
    # class methods
    def __init__(self, filename):
        self.path = Path(filename)
        self.data = self.load()

    def __str__(self):
        return self.data
    
    # public methods

    def load(self, filename):
        """Load a new text file."""
        self.path = Path(filename)
        self.data = self.path.read_text().splitlines()

    def save(self):
        """Save the current text file."""
        self.path.write_text(self.data)

    def save_as(self, filename):
        """Save the current text file as a new file."""
        self.path = Path(filename)
        self.save()

    def append_line(self, text):
        """Append new text line to the current file."""
        self.data += '\n' + text + '\n'

    def get_line(self, line_number):
        """Get line from current text."""
        if line_number < 0 or line_number >= len(self.data):
            return None
        
        return self.data[line_number]
    
    def set_line(self, line_number, text):
        """Set line in current text."""
        if line_number < 0 or line_number >= len(self.data):
            return
        
        self.data[line_number] = text

    def delete_line(self, line_number):
        """Delete line from current text."""
        if line_number < 0 or line_number >= len(self.data):
            return
        
        del self.data[line_number]

    def get_all_words(self):
        """Get all words from current text."""
        return self.data.split()
    
    def get_unique_words(self):
        """Get unique words from current text."""
        return set(self.data.split())
    
    def get_word_count(self):
        """Get word count from current text."""
        return len(self.data.split())
    
    def get_line_count(self):
        """Get line count from current text."""
        return len(self.data)
    