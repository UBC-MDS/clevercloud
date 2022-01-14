def CleverClean(text):
    """
    A preprocessor to convert all the letters to lower case and remove punctuations.   
    
    Parameters
    ----------
    text : numpy.array
        Input an array of text / strings 
    
    Returns
    -------
    numpy.array
        The cleaned array of text 
    
    Examples
    --------
    >>> sample_text = numpy.array('Apple is MY favorite!')
    >>> CleverClean(sample_text)
    'apple is my favorite'   
    
    """