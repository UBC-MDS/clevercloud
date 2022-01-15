def CleverLemStem(text):
    """
    A preprocessor to conduct lemmatinzation and stemming on the text.   
    
    Parameters
    ----------
    text : numpy.array
        Input an array of text / strings 
    
    Returns
    -------
    numpy.array
        The lemmatized and stemmed text 
    
    Examples
    --------
    >>> sample_text = numpy.array('went to Paris it was beautiful')
    >>> CleverLemStem(sample_text)
    'go to Paris it is beauty'   
    
    """
