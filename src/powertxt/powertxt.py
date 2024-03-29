from pathlib import Path
from powertxt.constants import P_MARKS

class PowerTxt:
    """A simple text handling class."""	
        
    # class methods
    def __init__(self, filename):
        self.load(filename)
        self.lines = self.text.splitlines()

        text_no_marks = self.text
        for p in P_MARKS:
            text_no_marks = text_no_marks.replace(p, " ")
        
        self.words = text_no_marks.split()

    def __str__(self):
        return self.text

    # public methods

    # file management
    def load(self, filename):
        """Load a new text file."""
        self.path = Path(filename)
        self.text = self.path.read_text()

    def save(self):
        """Save the current text file."""
        self.path.write_text(self.text)

    def save_as(self, filename):
        """Save the current text file as a new file."""
        self.path = Path(filename)
        self.save()


    # text manipulation
    def append_line(self, text):
        """Append new text line to the current file."""
        self.text += '\n' + text + '\n'

    def get_line(self, line_number):
        """Get line from current text."""
        if line_number < 0 or line_number >= len(self.text):
            return None
        
        return self.text[line_number]
    
    def set_line(self, line_number, text):
        """Set line in current text."""
        if line_number < 0 or line_number >= len(self.text):
            return
        
        self.text[line_number] = text

    def delete_line(self, line_number):
        """Delete line from current text."""
        if line_number < 0 or line_number >= len(self.text):
            return
        
        del self.text[line_number]

    def get_all_words(self):
        """Get all words from current text."""
        return self.words
    
    def get_unique_words(self):
        """Get unique words from current text."""
        return set(self.words)
    
    def get_word_count(self):
        """Get word count from current text."""
        return len(self.words)
    
    def get_line_count(self):
        """Get line count from current text."""
        return len(self.lines)
    
    def get_top_x_words(self, top = 10, min_lenght = 1):
        """Get top x words from current text."""
        word_count = {}
        for word in self.words:
            if len(word) >= min_lenght:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                
        return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:top]
    