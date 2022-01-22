#import packages
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from clevercloud.CleverLemStem import CleverLemStem
from pytest import raises

def test_CleverLemStem():
  """test CleverLemStem function"""
  
  # Check error 
  with raises(TypeError) as e:
    CleverLemStem("This is not a string")
  assert str(e.value) == "Input text should be a string"

  # Test whether the output is stored in a string
  assert CleverLemStem("good night") == "good night"

  # Test whether the lemmatization worked 
  assert CleverLemStem("runs running") == "run run"

  # Test whether the stemming worked
  assert CleverLemStem("Maximum feet") == "maxim foot"
