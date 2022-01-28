from clevercloud.CleverWordCloud import CleverWordCloud
from pytest import raises

def test_CleverWordCloud():
  """test CleverWordCloud function"""
  
  # Check error 
  with raises(TypeError) as e:
    CleverWordCloud(123, "hello", "a")
