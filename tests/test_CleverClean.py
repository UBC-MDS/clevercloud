def test_CleverClean():
    #importing pandas and pytest
    import pandas as pd 
    from clevercloud.CleverClean import CleverClean
    from pytest import raises
    
    #Error check
    with raises(TypeError) as e:
        CleverClean("This is not a panda series")
    assert str(e.value) == "Input 'text' should be a panda series containing only strings"
    
    #Branch 1: Testing whether pandas.series is stored in string form
    assert CleverClean(pd.Series(["hello", "world"])) == "hello world "
    
    #Branch 2: Testing whether strings are converted to lower case 
    assert CleverClean(pd.Series(["HELLO", "WORLD"])) == "hello world "
    
    #Branch 3: Test to see if all digits have been removed from the strings
    assert CleverClean(pd.Series(["hello123", "456world"])) == "hello world "
    
    #Branch 4: Test to see if all punctuation has been removed
    assert CleverClean(pd.Series(["hello world," " welcome"])) == "hello world welcome "