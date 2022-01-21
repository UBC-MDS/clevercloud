# author: Adrianne Leung
# date: Jan 2022

from clevercloud.CleverStopwords import CleverStopwords
import pytest

def test_CleverStopwords():
    """Test length of new stopwords"""
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    
    # NLTK English stopwords
    stopwords = set(stopwords.words("english"))
    expected = 181
    actual = len({"would", "aaa"}) + len(stopwords)
    assert actual == expected, "Duplicate words are added incorrectly."
    assert len(CleverStopwords({"the", "aaa"})) == len(stopwords) + 1, "Duplicate words are added incorrectly."

def test_CleverStopwords_error():
    """Check TypeError raised when input is not a set"""
    with pytest.raises(TypeError):
        words = ["would", "aaa"]
        CleverStopwords(words)
