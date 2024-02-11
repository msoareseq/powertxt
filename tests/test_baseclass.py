import pytest
from powertxt.powertxt import PowerTxt

@pytest.fixture
def power_txt():
    return PowerTxt("D:\\Projetos\\powertxt\\tests\\text1.txt")

def test_get_lines(power_txt):
    lines = power_txt.get_line_count()
    assert isinstance(lines, int)
    assert lines == 7

def test_get_word_count(power_txt):
    word_count = power_txt.get_word_count()
    assert isinstance(word_count, int)
    assert word_count == 43

def test_get_word_frequency(power_txt):
    word_frequency = power_txt.get_top_x_words()
    top_words = [('I', 5), ('is', 2), ('a', 2), ('cat', 2), ('and', 2), ('sleep', 2), ('My', 1), ('name', 1), ('Honda', 1), ('m', 1)]
    assert len(word_frequency) == 10
    assert word_frequency == top_words

def test_get_unique_words(power_txt):
    unique_words = power_txt.get_unique_words()
    all_words = power_txt.get_all_words()
    assert len(unique_words) < len(all_words)

# Add more test functions for other methods of the PowerTxt class



