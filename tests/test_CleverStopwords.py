# author: Adrianne Leung
# date: Jan 2022

from clevercloud.CleverStopwords import CleverStopwords
import pytest
import nltk
from nltk.corpus import stopwords

def test_CleverStopwords():
    """Test length and output of new stopwords"""
    nltk.download('stopwords')
    
    # NLTK English stopwords
    stopwords = set(stopwords.words("english"))
    expected = 181
    actual = len({"would", "aaa"}) + len(stopwords)
    assert actual == expected, "Duplicate words are added incorrectly."
    assert len(CleverStopwords({"the", "aaa"})) == len(stopwords) + 1, "Duplicate words are added incorrectly."
    assert isinstance(CleverStopwords({"the", "aaa"}), set), "Output is not a set."

def test_CleverStopwords_error():
    
    """Check TypeError raised when input is not a set"""
    with pytest.raises(TypeError):
        words = ["would", "aaa"]
        CleverStopwords(words)

    """Check TypeError raised when input value in the set is not a string"""
    with pytest.raises(TypeError):
        words = {12, "aaa"}
        CleverStopwords(words)

    
